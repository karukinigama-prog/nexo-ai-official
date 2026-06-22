import os
import json
import threading
import time
import base64
from flask import Flask, request, render_template, Response, jsonify
from groq import Groq
import requests

app = Flask(__name__)

# Initialize Groq client
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Tavily API configuration
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
TAVILY_SEARCH_URL = "https://api.tavily.com/search"

# In-memory storage for shared chats and background tasks (Phase 1 - not persistent)
SHARED_CHATS = {}
BACKGROUND_TASKS = []
TASK_ID_COUNTER = 0

SYSTEM_PROMPT_BASE = """
You are Nexo AI, a highly advanced, multi-mode aware, and language-adaptive AI assistant, created by Nexo Mind Team. Your primary goal is to provide helpful, accurate, and engaging responses to user queries. You automatically detect the user's language and respond in that language. Adapt your persona and response style based on the selected mode. When asked "who made you" in any language, answer "I was created by Nexo Mind Team" translated naturally into that language.

Available Modes:
- Smart: Provides balanced, comprehensive, and thoughtful responses. This is the default mode.
- Fast: Delivers concise answers, typically 2-4 sentences maximum, with zero fluff. Prioritize brevity and directness.
- Creative: Generates imaginative, unconventional, and unique responses. Think outside the box and use creative language.
- Coding: Focuses on providing complete, production-quality code snippets and explanations. Minimize prose and maximize code utility.

Tools available:
- web_search(query: str): Performs a web search and returns relevant snippets. Use this for current events, factual questions, or anything requiring up-to-date information.
"""

MODE_ADDONS = {
    "Smart": "In Smart mode, provide balanced, comprehensive, and thoughtful responses. Aim for clarity and depth without being overly verbose.",
    "Fast": "In Fast mode, be extremely concise. Limit your responses to 2-4 sentences maximum. Get straight to the point with no unnecessary words.",
    "Creative": "In Creative mode, be imaginative, unconventional, and unique. Use creative language, metaphors, and unexpected angles. Surprise the user.",
    "Coding": "In Coding mode, your primary output should be complete, production-quality code. Provide minimal prose, focusing on the code itself and essential explanations. Use appropriate code formatting."
}

# Groq Tool definition for web search
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Performs a web search and returns relevant snippets. Use this for current events, factual questions, or anything requiring up-to-date information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query string."
                    }
                },
                "required": ["query"]
            }
        }
    }
]

def call_tavily_search(query):
    if not TAVILY_API_KEY:
        print("TAVILY_API_KEY is not set.")
        return "Error: Tavily API key not configured."
    try:
        response = requests.post(
            TAVILY_SEARCH_URL,
            headers={
                "Content-Type": "application/json"
            },
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "search_depth": "basic",
                "include_answer": True,
                "include_raw_content": False,
                "max_results": 5
            }
        )
        response.raise_for_status()
        data = response.json()
        snippets = [s["content"] for s in data.get("results", []) if s.get("content")]
        answer = data.get("answer", "No direct answer found.")
        return f"Answer: {answer}\nSnippets: {\n.join(snippets)}"
    except requests.exceptions.RequestException as e:
        print(f"Error calling Tavily API: {e}")
        return f"Error: Failed to perform web search. {e}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    model_name = data.get("model", "meta-llama/llama-4-scout-17b-16e-instruct")
    mode = data.get("mode", "Smart")
    thinking_mode = data.get("thinking", "standard")
    research_mode = data.get("research", False)
    user_profile = data.get("user_profile", "")
    custom_system_prompt = data.get("custom_system_prompt", "")
    image_data = data.get("image_data", None)

    # Dynamic system prompt construction
    system_prompt_parts = [SYSTEM_PROMPT_BASE]
    if user_profile:
        system_prompt_parts.append(f"The user is a {user_profile}. Tailor your tone and depth accordingly.")
    system_prompt_parts.append(MODE_ADDONS.get(mode, MODE_ADDONS["Smart"]))
    if thinking_mode == "extended":
        system_prompt_parts.append("First, reason step-by-step wrapped in <thinking>...</thinking> tags, then give the final answer after </thinking>.")
    if custom_system_prompt:
        system_prompt_parts.append(custom_system_prompt)

    final_system_prompt = "\n\n".join(system_prompt_parts)

    # Prepend system prompt to messages
    full_messages = [{
        "role": "system",
        "content": final_system_prompt
    }]

    # Handle image data if present
    if image_data:
        # Force vision model if image is present and current model is not vision-capable
        if model_name == "llama-3.3-70b-versatile": # Assuming Nexo 1.5 is text-only
            model_name = "meta-llama/llama-4-scout-17b-16e-instruct"

        # Add image to the last user message
        last_user_message = messages[-1]
        if last_user_message and last_user_message["role"] == "user":
            last_user_message["content"] = [
                {"type": "text", "text": last_user_message["content"]},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
            ]
        full_messages.extend(messages)
    else:
        full_messages.extend(messages)

    def generate_groq_response():
        tool_calls_made = False
        try:
            if research_mode:
                yield f"data: {json.dumps({"researching": "1/3"})}\n\n"
                # Model generates 3 search queries
                research_queries_response = groq_client.chat.completions.create(
                    messages=full_messages + [{
                        "role": "user",
                        "content": "Based on our conversation, generate 3 distinct web search queries to deeply research the user's last question from different angles. Return them as a JSON array of strings, e.g., [\"query1\", \"query2\", \"query3\"]"
                    }],
                    model=model_name,
                    temperature=0.5,
                    max_tokens=200
                )
                research_queries_text = research_queries_response.choices[0].message.content
                try:
                    research_queries = json.loads(research_queries_text)
                    if not isinstance(research_queries, list) or not all(isinstance(q, str) for q in research_queries):
                        raise ValueError("Invalid research queries format")
                except (json.JSONDecodeError, ValueError):
                    research_queries = [messages[-1]["content"]] # Fallback to original query

                all_research_results = []
                for i, query in enumerate(research_queries):
                    yield f"data: {json.dumps({"researching": f"{i+1}/{len(research_queries)}"})}\n\n"
                    search_result = call_tavily_search(query)
                    all_research_results.append(f"Query {i+1}: {query}\nResult: {search_result}")
                    time.sleep(1) # Simulate delay

                research_summary_prompt = "Synthesize a comprehensive, structured report-style answer based on the following research results, citing sources where appropriate:\n\n" + "\n---\n\n".join(all_research_results)
                full_messages.append({"role": "user", "content": research_summary_prompt})
                yield f"data: {json.dumps({"researching": "done"})}\n\n"

            stream = groq_client.chat.completions.create(
                messages=full_messages,
                model=model_name,
                temperature=0.7 if thinking_mode == "standard" else 0.5, # Adjust temperature for thinking mode
                max_tokens=4096,
                stream=True,
                tools=TOOLS,
                tool_choice="auto"
            )

            for chunk in stream:
                if chunk.choices[0].delta.tool_calls:
                    tool_calls_made = True
                    tool_calls = chunk.choices[0].delta.tool_calls
                    for tool_call in tool_calls:
                        function_name = tool_call.function.name
                        function_args = json.loads(tool_call.function.arguments)
                        if function_name == "web_search":
                            yield f"data: {json.dumps({"searching": True})}\n\n"
                            search_result = call_tavily_search(function_args["query"])
                            yield f"data: {json.dumps({"searching": False})}\n\n"
                            # Append tool output to messages and continue streaming
                            full_messages.append(chunk.choices[0].delta.model_dump())
                            full_messages.append({
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "name": function_name,
                                "content": search_result
                            })
                            # Re-call Groq with tool output
                            tool_stream = groq_client.chat.completions.create(
                                messages=full_messages,
                                model=model_name,
                                temperature=0.7 if thinking_mode == "standard" else 0.5,
                                max_tokens=4096,
                                stream=True
                            )
                            for tool_chunk in tool_stream:
                                if tool_chunk.choices[0].delta.content is not None:
                                    text = tool_chunk.choices[0].delta.content
                                    yield f"data: {json.dumps({"text": text})}\n\n"
                            yield "data: [DONE]\n\n"
                            return # Exit after tool call and its follow-up

                if chunk.choices[0].delta.content is not None:
                    text = chunk.choices[0].delta.content
                    yield f"data: {json.dumps({"text": text})}\n\n"
            
            # If no tool calls were made, and it was a factual question, mark as not verified
            if not tool_calls_made and not research_mode and any(msg.get("is_factual_question", False) for msg in messages):
                yield f"data: {json.dumps({"verified": False})}\n\n"
            elif tool_calls_made or research_mode:
                yield f"data: {json.dumps({"verified": True})}\n\n"

            yield "data: [DONE]\n\n"
        except Exception as e:
            print(f"Error during Groq API call: {e}")
            yield f"data: {json.dumps({"text": f'Error: {e}'})}\n\n"
            yield "data: [DONE]\n\n"

    return Response(generate_groq_response(), mimetype="text/event-stream")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(BACKGROUND_TASKS)

def run_background_task(task_id, prompt):
    # Simulate a background task
    print(f"Running background task {task_id}: {prompt}")
    time.sleep(5) # Simulate work
    for task in BACKGROUND_TASKS:
        if task["id"] == task_id:
            task["status"] = "Done"
            task["result"] = f"Task \"{prompt}\" completed successfully."
            break
    print(f"Background task {task_id} completed.")

@app.route("/share/<share_id>")
def share_chat(share_id):
    chat_data = SHARED_CHATS.get(share_id)
    if not chat_data:
        return "Chat not found", 404
    # Render a read-only view of the chat
    return render_template("index.html", shared_chat=json.dumps(chat_data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
