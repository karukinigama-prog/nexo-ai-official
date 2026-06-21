import os
import json
from flask import Flask, request, render_template, Response
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT_BASE = """
You are Nexo AI, a highly advanced, multi-mode aware, and language-adaptive AI assistant. Your primary goal is to provide helpful, accurate, and engaging responses to user queries. You automatically detect the user's language and respond in that language. Adapt your persona and response style based on the selected mode.

Available Modes:
- Smart: Provides balanced, comprehensive, and thoughtful responses. This is the default mode.
- Fast: Delivers concise answers, typically 2-4 sentences maximum, with zero fluff. Prioritize brevity and directness.
- Creative: Generates imaginative, unconventional, and unique responses. Think outside the box and use creative language.
- Coding: Focuses on providing complete, production-quality code snippets and explanations. Minimize prose and maximize code utility.
"""

MODE_ADDONS = {
    "Smart": "In Smart mode, provide balanced, comprehensive, and thoughtful responses. Aim for clarity and depth without being overly verbose.",
    "Fast": "In Fast mode, be extremely concise. Limit your responses to 2-4 sentences maximum. Get straight to the point with no unnecessary words.",
    "Creative": "In Creative mode, be imaginative, unconventional, and unique. Use creative language, metaphors, and unexpected angles. Surprise the user.",
    "Coding": "In Coding mode, your primary output should be complete, production-quality code. Provide minimal prose, focusing on the code itself and essential explanations. Use appropriate code formatting."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    mode = data.get("mode", "Smart")

    # Construct system prompt based on mode
    system_prompt = SYSTEM_PROMPT_BASE + "\n\n" + MODE_ADDONS.get(mode, MODE_ADDONS["Smart"])

    # Prepend system prompt to messages
    full_messages = [{
        "role": "system",
        "content": system_prompt
    }] + messages

    def generate_groq_response():
        try:
            stream = groq_client.chat.completions.create(
                messages=full_messages,
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    text = chunk.choices[0].delta.content
                    yield f"data: {json.dumps({"text": text})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            print(f"Error during Groq API call: {e}")
            yield f"data: {json.dumps({"text": f'Error: {e}'})}\n\n"
            yield "data: [DONE]\n\n"

    return Response(generate_groq_response(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
