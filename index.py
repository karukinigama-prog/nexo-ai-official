<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexo AI</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        :root {
            /* Color Palette (Dark theme default) */
            --bg-primary: #0a0a12;
            --sidebar-bg: #0e0e1a;
            --card-panel-bg: rgba(20,19,38,0.95);
            --text-primary: #e8e8f5;
            --text-secondary: #9090b8;
            --text-muted: #4a4a70;
            --border-light: rgba(255,255,255,0.07);
            --border-dark: rgba(139,92,246,0.2);
            --accent-color-1: #7c3aed; /* Primary purple */
            --accent-color-2: #ec4899; /* Pink accent */
            --accent-color-3: #8b5cf6; /* Secondary purple */
            --accent-color-blue: #3b82f6;
            --accent-color-cyan: #22d3ee;
            --accent-color-orange: #f97316;
            --accent-color-red: #ef4444;
            --accent-color-green: #10b981;
            --accent-color-teal: #14b8a6;

            /* Typography */
            --font-inter: 'Inter', sans-serif;
            --font-space-grotesk: 'Space Grotesk', sans-serif;
            --base-font-size: 15px;
            --line-height-base: 1.65;

            /* Font Size Adjustment */
            --chat-text-size: var(--base-font-size);

            /* Light Mode Variables */
            --light-bg-primary: #ffffff;
            --light-sidebar-bg: #f8f8f8;
            --light-card-panel-bg: #ffffff;
            --light-text-primary: #1a1a2e;
            --light-text-secondary: #6b7280;
            --light-text-muted: #9ca3af;
            --light-border-light: rgba(0,0,0,0.07);
            --light-border-dark: rgba(100,100,100,0.2);
        }

        /* Light Mode */
        body.light-mode {
            --bg-primary: var(--light-bg-primary);
            --sidebar-bg: var(--light-sidebar-bg);
            --card-panel-bg: var(--light-card-panel-bg);
            --text-primary: var(--light-text-primary);
            --text-secondary: var(--light-text-secondary);
            --text-muted: var(--light-text-muted);
            --border-light: var(--light-border-light);
            --border-dark: var(--light-border-dark);
            background-color: var(--light-bg-primary);
            color: var(--light-text-primary);
        }

        *,
        *::before,
        *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
            overflow: hidden;
            font-family: var(--font-inter);
            font-size: var(--chat-text-size);
            line-height: var(--line-height-base);
            color: var(--text-primary);
            background-color: var(--bg-primary);
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        body {
            display: flex;
        }

        /* Layout */
        .container {
            display: flex;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }

        .sidebar {
            width: 260px;
            flex-shrink: 0;
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--border-light);
            display: flex;
            flex-direction: column;
            padding: 15px;
            position: relative;
            z-index: 100;
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s ease, border-color 0.3s ease;
        }

        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }

        .right-panel {
            width: 240px;
            flex-shrink: 0;
            background-color: var(--sidebar-bg);
            border-left: 1px solid var(--border-light);
            padding: 15px;
            overflow-y: auto;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }

        /* Starfield Background */
        .starfield {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 0;
        }

        .star {
            position: absolute;
            background-color: var(--text-primary);
            border-radius: 50%;
            opacity: 0;
            animation: twinkle linear infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0; }
            50% { opacity: 0.8; }
        }

        /* Purple Glow Orb */
        .glow-orb {
            position: absolute;
            bottom: -100px;
            left: 50%;
            transform: translateX(-50%);
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, var(--accent-color-1) 0%, rgba(124, 58, 237, 0) 70%);
            filter: blur(80px);
            z-index: 1;
            pointer-events: none;
        }

        /* General UI Elements */
        .btn {
            padding: 10px 15px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--accent-color-1), var(--accent-color-2), var(--accent-color-3));
            color: white;
            box-shadow: 0 4px 10px rgba(124, 58, 237, 0.3);
        }

        .btn-primary:hover {
            opacity: 0.9;
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(124, 58, 237, 0.5);
        }

        .icon-btn {
            background: none;
            border: none;
            color: var(--text-secondary);
            font-size: 1.2em;
            cursor: pointer;
            transition: color 0.2s ease;
        }

        .icon-btn:hover {
            color: var(--accent-color-1);
        }

        .pill {
            background-color: var(--card-panel-bg);
            color: var(--text-secondary);
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 5px;
            border: 1px solid var(--border-light);
        }

        .pill:hover {
            background-color: rgba(var(--accent-color-1), 0.1);
            color: var(--text-primary);
        }

        .pill.active {
            background: var(--accent-color-1);
            color: white;
            box-shadow: 0 4px 10px rgba(124, 58, 237, 0.3);
            border-color: var(--accent-color-1);
        }

        /* Sidebar */
        .sidebar-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }

        .sidebar-header .logo-mark {
            font-family: var(--font-space-grotesk);
            font-weight: 800;
            font-size: 1.5em;
            letter-spacing: 2px;
            background: linear-gradient(90deg, var(--accent-color-1), var(--accent-color-2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-left: 10px;
        }

        .sidebar-new-chat {
            width: 100%;
            margin-bottom: 20px;
        }

        .sidebar-search {
            width: 100%;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid var(--border-light);
            background-color: var(--card-panel-bg);
            color: var(--text-primary);
            margin-bottom: 20px;
        }

        .sidebar-search::placeholder {
            color: var(--text-muted);
        }

        .chat-history-section h4 {
            color: var(--text-secondary);
            font-size: 0.8em;
            margin-top: 15px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }

        .chat-item {
            display: flex;
            align-items: center;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 8px;
            color: var(--text-secondary);
            cursor: pointer;
            transition: background-color 0.2s ease;
            position: relative;
        }

        .chat-item:hover {
            background-color: rgba(var(--accent-color-1), 0.1);
        }

        .chat-item.active {
            background-color: rgba(var(--accent-color-1), 0.2);
            color: var(--text-primary);
        }

        .chat-item-icon {
            margin-right: 10px;
            font-size: 1em;
        }

        .chat-item-title {
            flex-grow: 1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .chat-item-menu {
            position: absolute;
            right: 5px;
            top: 50%;
            transform: translateY(-50%);
            background-color: var(--card-panel-bg);
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            display: none;
            flex-direction: column;
            z-index: 10;
        }

        .chat-item:hover .chat-item-menu {
            display: flex;
        }

        .chat-item-menu button {
            background: none;
            border: none;
            color: var(--text-primary);
            padding: 8px 12px;
            text-align: left;
            cursor: pointer;
            white-space: nowrap;
        }

        .chat-item-menu button:hover {
            background-color: rgba(var(--accent-color-1), 0.1);
        }

        .sidebar-footer {
            margin-top: auto;
            padding-top: 15px;
            border-top: 1px solid var(--border-light);
        }

        .sidebar-footer .user-profile {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .sidebar-footer .user-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background-color: var(--accent-color-1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            margin-right: 10px;
        }

        .sidebar-footer .user-name {
            font-weight: 600;
            color: var(--text-primary);
        }

        .sidebar-footer .settings-btn {
            width: 100%;
            text-align: left;
            padding: 10px;
            color: var(--text-secondary);
        }

        /* Main Chat Header */
        .chat-main-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 15px 20px;
            background-color: var(--sidebar-bg);
            border-bottom: 1px solid var(--border-light);
            z-index: 10;
            flex-wrap: wrap;
        }

        .chat-main-header .left-section {
            display: flex;
            align-items: center;
        }

        .chat-main-header .center-section {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .chat-main-header .right-section {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .chat-main-header .model-selector {
            background-color: var(--card-panel-bg);
            border: 1px solid var(--border-light);
            border-radius: 10px;
            padding: 8px 12px;
            color: var(--text-primary);
            appearance: none;
            -webkit-appearance: none;
            cursor: pointer;
            font-size: 0.9em;
        }

        .incognito-badge {
            background-color: var(--text-muted);
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.8em;
            display: flex;
            align-items: center;
            gap: 5px;
            margin-left: 10px;
        }

        /* Chat Area */
        .chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            position: relative;
            z-index: 2;
            scroll-behavior: smooth;
        }

        .chat-area::-webkit-scrollbar {
            width: 8px;
        }

        .chat-area::-webkit-scrollbar-track {
            background: var(--bg-primary);
        }

        .chat-area::-webkit-scrollbar-thumb {
            background: var(--text-muted);
            border-radius: 4px;
        }

        .message-bubble {
            display: flex;
            margin-bottom: 20px;
            opacity: 0;
            transform: translateY(10px);
            animation: message-fade-up 0.3s ease-out forwards;
        }

        @keyframes message-fade-up {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .message-bubble.user {
            justify-content: flex-end;
        }

        .message-bubble .avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background-color: var(--accent-color-1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1em;
            flex-shrink: 0;
        }

        .message-bubble.ai .avatar {
            margin-right: 10px;
        }

        .message-content-wrapper {
            max-width: 66%; /* Desktop default */
            display: flex;
            flex-direction: column;
        }

        .message-content {
            padding: 15px;
            border-radius: 15px;
            position: relative;
            word-wrap: break-word;
            background-color: var(--card-panel-bg);
            color: var(--text-primary);
        }

        .message-bubble.ai .message-content {
            border-bottom-left-radius: 0;
        }

        .message-bubble.user .message-content {
            background: linear-gradient(135deg, var(--accent-color-1), var(--accent-color-2));
            color: white;
            border-bottom-right-radius: 0;
        }

        .message-actions {
            display: flex;
            gap: 10px;
            margin-top: 5px;
            font-size: 0.9em;
            color: var(--text-muted);
            visibility: hidden;
            opacity: 0;
            transition: visibility 0s, opacity 0.3s linear;
        }

        .message-bubble:hover .message-actions {
            visibility: visible;
            opacity: 1;
        }

        .message-actions button {
            background: none;
            border: none;
            color: inherit;
            cursor: pointer;
            padding: 3px 5px;
            border-radius: 5px;
        }

        .message-actions button:hover {
            background-color: rgba(var(--accent-color-1), 0.1);
        }

        .message-timestamp {
            font-size: 0.75em;
            color: var(--text-muted);
            margin-top: 5px;
            display: block;
        }

        .message-bubble.user .message-timestamp {
            text-align: right;
            color: rgba(255, 255, 255, 0.7);
        }

        .read-ticks {
            color: var(--accent-color-blue); /* Indigo */
            font-size: 0.8em;
            margin-left: 5px;
        }

        .thinking-box {
            background-color: rgba(var(--accent-color-1), 0.1);
            border-left: 3px solid var(--accent-color-1);
            padding: 10px 15px;
            border-radius: 8px;
            margin-top: 10px;
            font-size: 0.9em;
            color: var(--text-secondary);
            font-family: monospace;
            overflow-x: auto;
        }

        .thinking-box-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            font-weight: 600;
            color: var(--text-primary);
        }

        .thinking-box-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
        }

        .thinking-box.expanded .thinking-box-content {
            max-height: 200px; /* Arbitrary max height for expansion */
        }

        .typing-indicator {
            display: flex;
            align-items: center;
            margin-left: 42px; /* Align with AI messages */
            margin-bottom: 20px;
            opacity: 0;
            animation: message-fade-up 0.3s ease-out forwards;
        }

        .typing-indicator .avatar {
            width: 32px;
            height: 32px;
            font-size: 1em;
            margin-right: 10px;
            flex-shrink: 0;
        }

        .typing-dots {
            display: flex;
            gap: 5px;
            background-color: var(--card-panel-bg);
            padding: 15px;
            border-radius: 15px;
            border-bottom-left-radius: 0;
        }

        .typing-dots span {
            width: 8px;
            height: 8px;
            background-color: var(--accent-color-1);
            border-radius: 50%;
            animation: bounce 1.4s infinite ease-in-out both;
        }

        .typing-dots span:nth-child(1) { animation-delay: -0.32s; }
        .typing-dots span:nth-child(2) { animation-delay: -0.16s; background-color: var(--accent-color-3); }
        .typing-dots span:nth-child(3) { animation-delay: 0s; background-color: var(--accent-color-2); }

        @keyframes bounce {
            0%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
        }

        /* Input Area */
        .input-area {
            position: sticky;
            bottom: 0;
            width: 100%;
            padding: 15px 20px;
            background: var(--bg-primary);
            backdrop-filter: blur(10px);
            border-top: 1px solid var(--border-light);
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 10;
        }

        .input-container {
            display: flex;
            align-items: flex-end;
            width: 100%;
            max-width: 800px;
            background-color: var(--sidebar-bg);
            border: 1px solid var(--border-light);
            border-radius: 20px;
            padding: 8px;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .input-container:focus-within {
            border-color: var(--accent-color-1);
            box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.3);
        }

        .input-container .icon-btn {
            font-size: 1.1em;
            padding: 5px;
        }

        .input-container textarea {
            flex-grow: 1;
            background: none;
            border: none;
            outline: none;
            color: var(--text-primary);
            font-family: var(--font-inter);
            font-size: 1em;
            padding: 5px 10px;
            resize: none;
            min-height: 24px; /* Approx one line */
            max-height: 120px; /* Approx 5 lines */
            overflow-y: auto;
            line-height: 1.5;
        }

        .input-container textarea::placeholder {
            color: var(--text-muted);
        }

        .send-button {
            background: linear-gradient(135deg, var(--accent-color-1), var(--accent-color-2));
            color: white;
            border: none;
            border-radius: 50%;
            width: 36px;
            height: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1em;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 10px rgba(124, 58, 237, 0.3);
        }

        .send-button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(124, 58, 237, 0.5);
        }

        .send-button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: scale(1);
            box-shadow: none;
        }

        .disclaimer {
            font-size: 0.7em;
            color: var(--text-muted);
            margin-top: 10px;
            text-align: center;
        }

        /* Markdown Styling */
        .message-content pre {
            background-color: rgba(0, 0, 0, 0.4);
            border-radius: 8px;
            padding: 10px;
            overflow-x: auto;
            margin: 10px 0;
            position: relative;
        }

        .message-content code {
            font-family: monospace;
            font-size: 0.9em;
            color: #e2e2f5;
        }

        .message-content pre code {
            display: block;
            padding: 0;
        }

        .message-content p {
            margin-bottom: 10px;
        }

        .message-content p:last-child {
            margin-bottom: 0;
        }

        .message-content strong {
            font-weight: 700;
            color: var(--text-primary);
        }

        .message-content em {
            font-style: italic;
        }

        .message-content h1, .message-content h2, .message-content h3 {
            font-family: var(--font-space-grotesk);
            margin-top: 20px;
            margin-bottom: 10px;
            color: var(--accent-color-1);
        }

        .message-content h1 { font-size: 1.8em; }
        .message-content h2 { font-size: 1.5em; }
        .message-content h3 { font-size: 1.2em; }

        .message-content ul {
            list-style-type: disc;
            margin-left: 20px;
            margin-bottom: 10px;
        }

        .message-content ol {
            list-style-type: decimal;
            margin-left: 20px;
            margin-bottom: 10px;
        }

        .message-content li {
            margin-bottom: 5px;
        }

        .message-content blockquote {
            border-left: 4px solid var(--accent-color-1);
            padding-left: 15px;
            margin: 10px 0;
            color: var(--text-secondary);
            font-style: italic;
        }

        .message-content hr {
            border: none;
            border-top: 1px solid var(--border-light);
            margin: 20px 0;
        }

        .message-content table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }

        .message-content th, .message-content td {
            border: 1px solid var(--border-light);
            padding: 8px;
            text-align: left;
        }

        .message-content th {
            background-color: rgba(var(--accent-color-1), 0.1);
            font-weight: 600;
        }

        /* Code block specific */
        .code-header {
            position: absolute;
            top: 5px;
            right: 5px;
            font-size: 0.8em;
            color: var(--text-muted);
            display: flex;
            gap: 5px;
            align-items: center;
        }

        .code-header .copy-code-btn {
            background-color: rgba(255,255,255,0.1);
            border: none;
            color: white;
            padding: 3px 8px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.7em;
        }

        /* Settings Modal */
        .settings-modal-backdrop {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.7);
            backdrop-filter: blur(5px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0s linear 0.3s;
        }

        .settings-modal-backdrop.open {
            opacity: 1;
            visibility: visible;
            transition: opacity 0.3s ease;
        }

        .settings-modal {
            background-color: var(--card-panel-bg);
            border-radius: 15px;
            padding: 30px;
            width: 90%;
            max-width: 600px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transform: scale(0.9);
            opacity: 0;
            transition: transform 0.3s ease, opacity 0.3s ease;
            position: relative;
            color: var(--text-primary);
        }

        .settings-modal-backdrop.open .settings-modal {
            transform: scale(1);
            opacity: 1;
        }

        .settings-modal-close {
            position: absolute;
            top: 15px;
            right: 15px;
            font-size: 1.5em;
            color: var(--text-secondary);
            cursor: pointer;
        }

        .settings-modal h2 {
            font-family: var(--font-space-grotesk);
            color: var(--accent-color-1);
            margin-bottom: 20px;
        }

        .settings-section {
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--border-light);
        }

        .settings-section:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }

        .settings-section h3 {
            color: var(--text-primary);
            font-size: 1.1em;
            margin-bottom: 10px;
        }

        .settings-section label {
            display: block;
            margin-bottom: 5px;
            color: var(--text-secondary);
        }

        .settings-section input[type="text"],
        .settings-section textarea,
        .settings-section select {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid var(--border-light);
            background-color: var(--sidebar-bg);
            color: var(--text-primary);
            margin-bottom: 10px;
        }

        .settings-section textarea {
            min-height: 80px;
            resize: vertical;
        }

        .settings-section .btn-group button {
            margin-right: 10px;
            background-color: var(--sidebar-bg);
            color: var(--text-secondary);
            border: 1px solid var(--border-light);
        }

        .settings-section .btn-group button.active {
            background-color: var(--accent-color-1);
            color: white;
            border-color: var(--accent-color-1);
        }

        .color-picker-grid {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }

        .color-box {
            width: 30px;
            height: 30px;
            border-radius: 5px;
            cursor: pointer;
            border: 2px solid transparent;
            transition: border-color 0.2s ease;
        }

        .color-box.active {
            border-color: var(--text-primary);
        }

        /* Voice Chat Modal */
        .voice-chat-modal-backdrop {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.9);
            backdrop-filter: blur(10px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 1001;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0s linear 0.3s;
            color: white;
        }

        .voice-chat-modal-backdrop.open {
            opacity: 1;
            visibility: visible;
            transition: opacity 0.3s ease;
        }

        .voice-chat-modal h2 {
            font-family: var(--font-space-grotesk);
            color: var(--accent-color-1);
            margin-bottom: 30px;
        }

        .voice-mic-button {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--accent-color-1), var(--accent-color-2));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4em;
            color: white;
            cursor: pointer;
            position: relative;
            box-shadow: 0 0 0 0 rgba(var(--accent-color-1), 0.7);
            animation: pulse 2s infinite;
        }

        .voice-mic-button.recording {
            animation: pulse-red 1.5s infinite;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(var(--accent-color-1), 0.7); }
            70% { box-shadow: 0 0 0 20px rgba(var(--accent-color-1), 0); }
            100% { box-shadow: 0 0 0 0 rgba(var(--accent-color-1), 0); }
        }

        @keyframes pulse-red {
            0% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.7); }
            70% { box-shadow: 0 0 0 20px rgba(255, 0, 0, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); }
        }

        .voice-waveform {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 5px solid rgba(255,255,255,0.3);
            opacity: 0;
            animation: waveform 1.5s infinite ease-out;
        }

        .voice-mic-button.recording .voice-waveform {
            opacity: 1;
        }

        .voice-waveform:nth-child(2) { animation-delay: 0.2s; }
        .voice-waveform:nth-child(3) { animation-delay: 0.4s; }

        @keyframes waveform {
            0% { transform: scale(0.7); opacity: 0; }
            50% { transform: scale(1); opacity: 1; }
            100% { transform: scale(1.3); opacity: 0; }
        }

        .voice-status-text {
            margin-top: 20px;
            font-size: 1.2em;
            color: var(--text-secondary);
        }

        .voice-chat-exit-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            background: none;
            border: none;
            color: white;
            font-size: 1.5em;
            cursor: pointer;
        }

        /* Mobile Responsiveness */
        @media (max-width: 900px) {
            .right-panel {
                display: none;
            }
            .main-content {
                width: 100%;
            }
        }

        @media (max-width: 768px) {
            .sidebar {
                transform: translateX(-100%);
                position: absolute;
                height: 100%;
                top: 0;
                left: 0;
                z-index: 1000;
                box-shadow: 5px 0 15px rgba(0,0,0,0.3);
            }

            .sidebar.open {
                transform: translateX(0%);
            }

            .hamburger-menu {
                display: block;
            }

            .chat-main-header {
                padding: 10px 15px;
            }

            .chat-area {
                padding: 15px;
            }

            .message-content-wrapper {
                max-width: 82%; /* Mobile */
            }

            .input-area {
                padding: 10px 15px;
            }

            .message-actions {
                visibility: visible;
                opacity: 1;
            }
        }

        @media (max-width: 480px) {
            .sidebar-header .logo-mark {
                font-size: 1.2em;
            }

            .btn-primary {
                padding: 8px 12px;
                font-size: 0.9em;
            }

            .pill {
                padding: 6px 10px;
                font-size: 0.8em;
            }

            .input-container {
                padding: 5px;
            }

            .input-container textarea {
                padding: 5px 8px;
            }

            .send-button {
                width: 32px;
                height: 32px;
                font-size: 0.9em;
            }

            .settings-modal {
                padding: 20px;
            }

            .voice-mic-button {
                width: 120px;
                height: 120px;
                font-size: 3em;
            }
        }
    </style>
</head>
<body class="dark-mode">
    <div class="container">
        <!-- Sidebar -->
        <div class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <i class="fas fa-brain fa-2x" style="color: var(--accent-color-1);"></i>
                <span class="logo-mark">Nexo AI</span>
            </div>
            <button class="btn btn-primary sidebar-new-chat" id="new-chat-btn">+ New Chat</button>
            <input type="text" class="sidebar-search" id="sidebar-search" placeholder="Search chats...">

            <div class="recent-chats" id="recent-chats">
                <!-- Pinned Chats -->
                <div class="chat-history-section" id="pinned-chats-section" style="display: none;">
                    <h4>📌 Pinned</h4>
                    <div id="pinned-chat-list"></div>
                </div>
                <!-- Date Grouped Chats -->
                <div id="date-grouped-chat-list"></div>
            </div>

            <div class="sidebar-footer">
                <div class="user-profile">
                    <div class="user-avatar">NM</div>
                    <span class="user-name">Nexo Mind Team</span>
                </div>
                <button class="icon-btn settings-btn" id="settings-btn"><i class="fas fa-cog"></i> Settings</button>
            </div>
        </div>

        <!-- Main Content Area -->
        <div class="main-content">
            <div class="starfield" id="starfield"></div>
            <div class="glow-orb"></div>

            <!-- Chat Header -->
            <div class="chat-main-header">
                <div class="left-section">
                    <button class="icon-btn hamburger-menu" id="hamburger-menu"><i class="fas fa-bars"></i></button>
                    <select class="model-selector" id="model-selector">
                        <option value="meta-llama/llama-4-scout-17b-16e-instruct">Nexo 4.1 (Vision)</option>
                        <option value="llama-3.3-70b-versatile">Nexo 1.5 (Fast)</option>
                    </select>
                    <span class="incognito-badge" id="incognito-badge" style="display: none;"><i class="fas fa-lock"></i> Incognito</span>
                </div>
                <div class="center-section">
                    <div class="pill" id="thinking-toggle" data-mode="standard">🧠 Thinking: Standard</div>
                    <div class="pill" id="research-toggle" data-mode="off">🔬 Research: Off</div>
                </div>
                <div class="right-section">
                    <button class="icon-btn" id="incognito-toggle" title="Toggle Incognito Mode"><i class="fas fa-eye"></i></button>
                    <button class="icon-btn" id="theme-toggle" title="Toggle Light/Dark Mode"><i class="fas fa-moon"></i></button>
                    <button class="icon-btn" id="tasks-btn" title="Background Tasks"><i class="fas fa-bell"></i></button>
                    <button class="icon-btn" id="share-btn" title="Share Chat"><i class="fas fa-share-alt"></i></button>
                </div>
            </div>

            <!-- Chat Area -->
            <div class="chat-area" id="messages-area">
                <!-- Welcome Message -->
                <div class="message-bubble ai initial-welcome">
                    <div class="avatar">🤖</div>
                    <div class="message-content-wrapper">
                        <div class="message-content">
                            <p>Hello! I'm Nexo AI, your personal AI companion. How can I assist you today?</p>
                            <span class="message-timestamp">Just now</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Input Area -->
            <div class="input-area">
                <div class="input-container">
                    <button class="icon-btn" id="attach-btn" title="Attach file"><i class="fas fa-paperclip"></i></button>
                    <textarea id="chat-input" placeholder="Type your message..." rows="1"></textarea>
                    <button class="icon-btn" id="clear-input-btn" title="Clear text" style="display: none;"><i class="fas fa-times"></i></button>
                    <button class="icon-btn" id="mic-btn" title="Voice input"><i class="fas fa-microphone"></i></button>
                    <button class="send-button" id="send-button" disabled><i class="fas fa-arrow-up"></i></button>
                </div>
                <div class="disclaimer">
                    Nexo AI can make mistakes. Consider checking important information.
                </div>
            </div>
        </div>

        <!-- Right Panel -->
        <div class="right-panel" id="right-panel">
            <h3>AI Models</h3>
            <div class="card">
                <p>Nexo 4.1: Best for most tasks, vision-capable</p>
                <p>Nexo 1.5: Faster, lightweight, text-only</p>
            </div>
            <h3>Tools</h3>
            <div class="card">
                <p>Web Search, Image Analyzer, Voice Chat, Research Mode, Code Blocks</p>
            </div>
            <h3>Daily Usage</h3>
            <div class="card">
                <div class="progress-bar">
                    <div class="progress" style="width: 70%;"></div>
                </div>
                <p>70% used</p>
            </div>
        </div>
    </div>

    <!-- Settings Modal -->
    <div class="settings-modal-backdrop" id="settings-modal-backdrop">
        <div class="settings-modal" id="settings-modal">
            <i class="fas fa-times settings-modal-close" id="settings-modal-close"></i>
            <h2>Settings</h2>

            <div class="settings-section">
                <h3>Profile</h3>
                <label for="profile-role">Your Role:</label>
                <input type="text" id="profile-role" placeholder="e.g., I'm a teacher">
            </div>

            <div class="settings-section">
                <h3>Custom System Prompt</h3>
                <textarea id="custom-system-prompt" placeholder="Add your custom instructions here..."></textarea>
                <button class="btn btn-primary" id="save-custom-prompt">+ Add System Prompt</button>
                <button class="btn" id="clear-custom-prompt">Clear custom prompt</button>
            </div>

            <div class="settings-section">
                <h3>Appearance</h3>
                <label>Accent Color:</label>
                <div class="color-picker-grid">
                    <div class="color-box active" data-colors="#7c3aed,#ec4899,#8b5cf6" style="background: linear-gradient(135deg, #7c3aed, #ec4899, #8b5cf6);"></div>
                    <div class="color-box" data-colors="#3b82f6,#22d3ee,#60a5fa" style="background: linear-gradient(135deg, #3b82f6, #22d3ee, #60a5fa);"></div>
                    <div class="color-box" data-colors="#f97316,#ef4444,#f59e0b" style="background: linear-gradient(135deg, #f97316, #ef4444, #f59e0b);"></div>
                    <div class="color-box" data-colors="#10b981,#14b8a6,#34d399" style="background: linear-gradient(135deg, #10b981, #14b8a6, #34d399);"></div>
                </div>
            </div>

            <div class="settings-section">
                <h3>Font Size</h3>
                <div class="btn-group">
                    <button class="btn active" data-size="small">Small</button>
                    <button class="btn" data-size="medium">Medium</button>
                    <button class="btn" data-size="large">Large</button>
                </div>
            </div>

            <div class="settings-section">
                <h3>About</h3>
                <p>Nexo AI — Created by Nexo Mind Team</p>
                <p>Version: 1.0.0</p>
            </div>
        </div>
    </div>

    <!-- Voice Chat Modal -->
    <div class="voice-chat-modal-backdrop" id="voice-chat-modal-backdrop">
        <button class="voice-chat-exit-btn" id="voice-chat-exit-btn"><i class="fas fa-times"></i></button>
        <h2>Voice Chat Mode</h2>
        <div class="voice-mic-button" id="voice-mic-button">
            <i class="fas fa-microphone"></i>
            <div class="voice-waveform"></div>
            <div class="voice-waveform"></div>
            <div class="voice-waveform"></div>
        </div>
        <p class="voice-status-text" id="voice-status-text">Tap to speak</p>
        <p id="voice-transcript" style="margin-top: 20px; font-style: italic;"></p>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.3.3/purify.min.js"></script>
    <script>
        const messagesArea = document.getElementById("messages-area");
        const chatInput = document.getElementById("chat-input");
        const sendButton = document.getElementById("send-button");
        const newChatBtn = document.getElementById("new-chat-btn");
        const sidebar = document.getElementById("sidebar");
        const hamburgerMenu = document.getElementById("hamburger-menu");
        const themeToggle = document.getElementById("theme-toggle");
        const incognitoToggle = document.getElementById("incognito-toggle");
        const incognitoBadge = document.getElementById("incognito-badge");
        const modelSelector = document.getElementById("model-selector");
        const thinkingToggle = document.getElementById("thinking-toggle");
        const researchToggle = document.getElementById("research-toggle");
        const settingsBtn = document.getElementById("settings-btn");
        const settingsModalBackdrop = document.getElementById("settings-modal-backdrop");
        const settingsModalClose = document.getElementById("settings-modal-close");
        const profileRoleInput = document.getElementById("profile-role");
        const customSystemPromptTextarea = document.getElementById("custom-system-prompt");
        const saveCustomPromptBtn = document.getElementById("save-custom-prompt");
        const clearCustomPromptBtn = document.getElementById("clear-custom-prompt");
        const colorPickerGrid = document.querySelector(".color-picker-grid");
        const fontSizeButtons = document.querySelectorAll(".settings-section .btn-group button");
        const clearInputBtn = document.getElementById("clear-input-btn");
        const micBtn = document.getElementById("mic-btn");
        const voiceChatModalBackdrop = document.getElementById("voice-chat-modal-backdrop");
        const voiceChatExitBtn = document.getElementById("voice-chat-exit-btn");
        const voiceMicButton = document.getElementById("voice-mic-button");
        const voiceStatusText = document.getElementById("voice-status-text");
        const voiceTranscript = document.getElementById("voice-transcript");
        const attachBtn = document.getElementById("attach-btn");
        const recentChatsDiv = document.getElementById("recent-chats");
        const pinnedChatList = document.getElementById("pinned-chat-list");
        const dateGroupedChatList = document.getElementById("date-grouped-chat-list");
        const pinnedChatsSection = document.getElementById("pinned-chats-section");
        const sidebarSearch = document.getElementById("sidebar-search");
        const shareBtn = document.getElementById("share-btn");

        let currentChat = [];
        let currentChatId = null;
        let chatHistory = JSON.parse(localStorage.getItem("chatHistory")) || {};
        let incognitoMode = false;
        let isStreaming = false;
        let abortController = null;
        let recognition = null; // For Web Speech API
        let speechSynthesisUtterance = null; // For Speech Synthesis API
        let isVoiceChatMode = false;
        let attachedImage = null;
        let backgroundTasks = [];

        // --- Utility Functions ---
        function generateUniqueId() {
            return Date.now().toString(36) + Math.random().toString(36).substr(2);
        }

        function saveSettings() {
            localStorage.setItem("nexoAISettings", JSON.stringify({
                profileRole: profileRoleInput.value,
                customSystemPrompt: customSystemPromptTextarea.value,
                accentColor: document.body.dataset.accentColor,
                fontSize: document.body.dataset.fontSize,
                theme: document.body.classList.contains("light-mode") ? "light" : "dark"
            }));
        }

        function loadSettings() {
            const settings = JSON.parse(localStorage.getItem("nexoAISettings")) || {};
            profileRoleInput.value = settings.profileRole || "";
            customSystemPromptTextarea.value = settings.customSystemPrompt || "";
            if (settings.accentColor) {
                applyAccentColor(settings.accentColor);
            }
            if (settings.fontSize) {
                applyFontSize(settings.fontSize);
            }
            if (settings.theme === "light") {
                document.body.classList.add("light-mode");
                themeToggle.innerHTML = `<i class="fas fa-sun"></i>`;
            } else {
                document.body.classList.remove("light-mode");
                themeToggle.innerHTML = `<i class="fas fa-moon"></i>`;
            }
            // Update font size buttons
            fontSizeButtons.forEach(btn => {
                if (btn.dataset.size === settings.fontSize) {
                    btn.classList.add("active");
                } else {
                    btn.classList.remove("active");
                }
            });
            // Update color picker active state
            document.querySelectorAll(".color-box").forEach(box => {
                if (box.dataset.colors === settings.accentColor) {
                    box.classList.add("active");
                } else {
                    box.classList.remove("active");
                }
            });
        }

        function applyAccentColor(colors) {
            const [c1, c2, c3] = colors.split(",");
            document.documentElement.style.setProperty("--accent-color-1", c1);
            document.documentElement.style.setProperty("--accent-color-2", c2);
            document.documentElement.style.setProperty("--accent-color-3", c3);
            document.body.dataset.accentColor = colors;
        }

        function applyFontSize(size) {
            let fontSize;
            switch (size) {
                case "small": fontSize = "13px"; break;
                case "medium": fontSize = "15px"; break;
                case "large": fontSize = "17px"; break;
                default: fontSize = "15px";
            }
            document.documentElement.style.setProperty("--chat-text-size", fontSize);
            document.body.dataset.fontSize = size;
        }

        function saveChatHistory() {
            localStorage.setItem("chatHistory", JSON.stringify(chatHistory));
        }

        function renderChatHistory() {
            pinnedChatList.innerHTML = "";
            dateGroupedChatList.innerHTML = "";
            let hasPinnedChats = false;

            const sortedChatIds = Object.keys(chatHistory).sort((a, b) => {
                return chatHistory[b].timestamp - chatHistory[a].timestamp;
            });

            const today = new Date();
            const yesterday = new Date(today);
            yesterday.setDate(today.getDate() - 1);

            const sevenDaysAgo = new Date(today);
            sevenDaysAgo.setDate(today.getDate() - 7);

            const chatGroups = {
                "Pinned": [],
                "Today": [],
                "Yesterday": [],
                "Previous 7 Days": [],
                "Older": []
            };

            sortedChatIds.forEach(id => {
                const chat = chatHistory[id];
                const chatDate = new Date(chat.timestamp);

                if (chat.pinned) {
                    chatGroups["Pinned"].push({ id, chat });
                    hasPinnedChats = true;
                } else if (chatDate.toDateString() === today.toDateString()) {
                    chatGroups["Today"].push({ id, chat });
                } else if (chatDate.toDateString() === yesterday.toDateString()) {
                    chatGroups["Yesterday"].push({ id, chat });
                } else if (chatDate > sevenDaysAgo) {
                    chatGroups["Previous 7 Days"].push({ id, chat });
                } else {
                    chatGroups["Older"].push({ id, chat });
                }
            });

            if (hasPinnedChats) {
                pinnedChatsSection.style.display = "block";
                chatGroups["Pinned"].forEach(({ id, chat }) => {
                    pinnedChatList.appendChild(createChatItem(id, chat, true));
                });
            } else {
                pinnedChatsSection.style.display = "none";
            }

            for (const groupName of ["Today", "Yesterday", "Previous 7 Days", "Older"]) {
                if (chatGroups[groupName].length > 0) {
                    const groupHeader = document.createElement("h4");
                    groupHeader.textContent = groupName;
                    dateGroupedChatList.appendChild(groupHeader);
                    chatGroups[groupName].forEach(({ id, chat }) => {
                        dateGroupedChatList.appendChild(createChatItem(id, chat));
                    });
                }
            }
        }

        function createChatItem(id, chat, isPinned = false) {
            const chatItem = document.createElement("div");
            chatItem.classList.add("chat-item");
            if (id === currentChatId) {
                chatItem.classList.add("active");
            }
            chatItem.dataset.chatId = id;
            chatItem.innerHTML = `
                <i class="chat-item-icon fas fa-comment-alt"></i>
                <span class="chat-item-title">${chat.title}</span>
                <div class="chat-item-menu">
                    <button data-action="rename"><i class="fas fa-edit"></i> Rename</button>
                    <button data-action="delete"><i class="fas fa-trash"></i> Delete</button>
                    <button data-action="pin"><i class="fas fa-thumbtack"></i> ${isPinned ? "Unpin" : "Pin"}</button>
                </div>
            `;
            chatItem.addEventListener("click", (e) => {
                if (!e.target.closest(".chat-item-menu")) {
                    loadChat(id);
                }
            });
            chatItem.querySelector("[data-action='rename']").addEventListener("click", () => renameChat(id));
            chatItem.querySelector("[data-action='delete']").addEventListener("click", () => deleteChat(id));
            chatItem.querySelector("[data-action='pin']").addEventListener("click", () => togglePinChat(id));
            return chatItem;
        }

        function loadChat(id) {
            currentChatId = id;
            currentChat = chatHistory[id].messages;
            messagesArea.innerHTML = "";
            currentChat.forEach(msg => displayMessage(msg.role, msg.content, msg.timestamp, false));
            messagesArea.scrollTop = messagesArea.scrollHeight;
            renderChatHistory(); // Update active state
        }

        function renameChat(id) {
            const chat = chatHistory[id];
            const newTitle = prompt("Enter new title for chat:", chat.title);
            if (newTitle && newTitle.trim() !== "") {
                chat.title = newTitle.trim();
                saveChatHistory();
                renderChatHistory();
            }
        }

        function deleteChat(id) {
            if (confirm("Are you sure you want to delete this chat?")) {
                delete chatHistory[id];
                saveChatHistory();
                renderChatHistory();
                if (currentChatId === id) {
                    startNewChat();
                }
            }
        }

        function togglePinChat(id) {
            chatHistory[id].pinned = !chatHistory[id].pinned;
            saveChatHistory();
            renderChatHistory();
        }

        function startNewChat() {
            currentChat = [];
            currentChatId = null;
            messagesArea.innerHTML = `
                <div class="message-bubble ai initial-welcome">
                    <div class="avatar">🤖</div>
                    <div class="message-content-wrapper">
                        <div class="message-content">
                            <p>Hello! I'm Nexo AI, your personal AI companion. How can I assist you today?</p>
                            <span class="message-timestamp">Just now</span>
                        </div>
                    </div>
                </div>
            `;
            messagesArea.scrollTop = messagesArea.scrollHeight;
            renderChatHistory();
            attachedImage = null;
            // Clear image preview if any
        }

        function autoResizeTextarea() {
            chatInput.style.height = 'auto';
            chatInput.style.height = chatInput.scrollHeight + 'px';
        }

        chatInput.addEventListener("input", () => {
            autoResizeTextarea();
            sendButton.disabled = chatInput.value.trim() === "";
            clearInputBtn.style.display = chatInput.value.trim() === "" ? "none" : "inline-block";
        });

        clearInputBtn.addEventListener("click", () => {
            chatInput.value = "";
            autoResizeTextarea();
            sendButton.disabled = true;
            clearInputBtn.style.display = "none";
        });

        chatInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                if (!sendButton.disabled && !isStreaming) {
                    sendMessage();
                }
            }
        });

        sendButton.addEventListener("click", () => {
            if (isStreaming) {
                abortController.abort();
                sendButton.innerHTML = `<i class="fas fa-arrow-up"></i>`;
                sendButton.classList.remove("stop-button");
                isStreaming = false;
            } else {
                sendMessage();
            }
        });

        newChatBtn.addEventListener("click", startNewChat);

        hamburgerMenu.addEventListener("click", () => {
            sidebar.classList.toggle("open");
        });

        // --- Settings Modal Logic ---
        settingsBtn.addEventListener("click", () => {
            settingsModalBackdrop.classList.add("open");
            loadSettings(); // Load settings when modal opens
        });

        settingsModalClose.addEventListener("click", () => {
            settingsModalBackdrop.classList.remove("open");
            saveSettings(); // Save settings when modal closes
        });

        settingsModalBackdrop.addEventListener("click", (e) => {
            if (e.target === settingsModalBackdrop) {
                settingsModalBackdrop.classList.remove("open");
                saveSettings();
            }
        });

        saveCustomPromptBtn.addEventListener("click", saveSettings);
        clearCustomPromptBtn.addEventListener("click", () => {
            customSystemPromptTextarea.value = "";
            saveSettings();
        });

        profileRoleInput.addEventListener("change", saveSettings);

        colorPickerGrid.addEventListener("click", (e) => {
            const colorBox = e.target.closest(".color-box");
            if (colorBox) {
                document.querySelectorAll(".color-box").forEach(box => box.classList.remove("active"));
                colorBox.classList.add("active");
                applyAccentColor(colorBox.dataset.colors);
                saveSettings();
            }
        });

        fontSizeButtons.forEach(button => {
            button.addEventListener("click", () => {
                fontSizeButtons.forEach(btn => btn.classList.remove("active"));
                button.classList.add("active");
                applyFontSize(button.dataset.size);
                saveSettings();
            });
        });

        // --- Theme Toggle ---
        themeToggle.addEventListener("click", () => {
            document.body.classList.toggle("light-mode");
            if (document.body.classList.contains("light-mode")) {
                themeToggle.innerHTML = `<i class="fas fa-sun"></i>`;
            } else {
                themeToggle.innerHTML = `<i class="fas fa-moon"></i>`;
            }
            saveSettings();
        });

        // --- Incognito Mode Toggle ---
        incognitoToggle.addEventListener("click", () => {
            incognitoMode = !incognitoMode;
            if (incognitoMode) {
                incognitoBadge.style.display = "inline-flex";
                incognitoToggle.querySelector("i").classList.replace("fa-eye", "fa-eye-slash");
            } else {
                incognitoBadge.style.display = "none";
                incognitoToggle.querySelector("i").classList.replace("fa-eye-slash", "fa-eye");
            }
            startNewChat(); // Start a fresh session for incognito
        });

        // --- Model Selector ---
        modelSelector.addEventListener("change", () => {
            localStorage.setItem("selectedModel", modelSelector.value);
        });
        modelSelector.value = localStorage.getItem("selectedModel") || "meta-llama/llama-4-scout-17b-16e-instruct";

        // --- Thinking/Research Toggles ---
        thinkingToggle.addEventListener("click", () => {
            const currentMode = thinkingToggle.dataset.mode;
            thinkingToggle.dataset.mode = currentMode === "standard" ? "extended" : "standard";
            thinkingToggle.innerHTML = thinkingToggle.dataset.mode === "standard" ? "🧠 Thinking: Standard" : "🧠 Thinking: Extended";
            thinkingToggle.classList.toggle("active", thinkingToggle.dataset.mode === "extended");
        });

        researchToggle.addEventListener("click", () => {
            const currentMode = researchToggle.dataset.mode;
            researchToggle.dataset.mode = currentMode === "off" ? "on" : "off";
            researchToggle.innerHTML = researchToggle.dataset.mode === "off" ? "🔬 Research: Off" : "🔬 Research: On";
            researchToggle.classList.toggle("active", researchToggle.dataset.mode === "on");
        });

        // --- Message Display and Markdown Rendering ---
        function displayMessage(role, content, timestamp = new Date().toISOString(), animate = true, messageId = generateUniqueId()) {
            const messageBubble = document.createElement("div");
            messageBubble.classList.add("message-bubble", role);
            messageBubble.dataset.messageId = messageId;

            let avatar = role === "user" ? `<div class="avatar">You</div>` : `<div class="avatar">🤖</div>`;
            let formattedContent = DOMPurify.sanitize(marked.parse(content));

            messageBubble.innerHTML = `
                ${role === "ai" ? avatar : ''}
                <div class="message-content-wrapper">
                    <div class="message-content">
                        ${formattedContent}
                    </div>
                    <div class="message-actions">
                        ${role === "ai" ? `
                            <button title="Thumbs Up"><i class="fas fa-thumbs-up"></i></button>
                            <button title="Thumbs Down"><i class="fas fa-thumbs-down"></i></button>
                            <button title="Read Aloud" class="read-aloud-btn"><i class="fas fa-volume-up"></i></button>
                            <button title="Share/Export" class="share-export-btn"><i class="fas fa-share-alt"></i></button>
                        ` : `
                            <button title="Edit Message" class="edit-message-btn"><i class="fas fa-pencil-alt"></i></button>
                        `}
                        <button title="Copy" class="copy-message-btn"><i class="fas fa-copy"></i></button>
                        <button title="Regenerate/Retry" class="regenerate-btn"><i class="fas fa-redo"></i></button>
                    </div>
                    <span class="message-timestamp">${formatTimestamp(timestamp)}</span>
                </div>
                ${role === "user" ? avatar : ''}
            `;

            messagesArea.appendChild(messageBubble);
            if (animate) {
                messagesArea.scrollTop = messagesArea.scrollHeight;
            }

            // Add event listeners for message actions
            if (role === "ai") {
                messageBubble.querySelector(".read-aloud-btn").addEventListener("click", (e) => toggleReadAloud(e.currentTarget, content));
                messageBubble.querySelector(".share-export-btn").addEventListener("click", (e) => showShareExportMenu(e.currentTarget, content));
            } else if (role === "user") {
                messageBubble.querySelector(".edit-message-btn").addEventListener("click", (e) => editUserMessage(e.currentTarget, messageId, content));
            }
            messageBubble.querySelector(".copy-message-btn").addEventListener("click", (e) => copyToClipboard(content, e.currentTarget));
            messageBubble.querySelector(".regenerate-btn").addEventListener("click", () => regenerateResponse(messageId));

            // Syntax highlighting for code blocks
            messageBubble.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightElement(block);
                const lang = block.className.split(' ').find(cls => cls.startsWith('language-'))?.replace('language-', '') || 'text';
                const codeHeader = document.createElement('div');
                codeHeader.classList.add('code-header');
                codeHeader.innerHTML = `<span>${lang}</span><button class="copy-code-btn">Copy</button>`;
                block.parentNode.insertBefore(codeHeader, block);
                codeHeader.querySelector('.copy-code-btn').addEventListener('click', () => copyToClipboard(block.textContent, codeHeader.querySelector('.copy-code-btn')));
            });

            return messageBubble;
        }

        function formatTimestamp(isoString) {
            const date = new Date(isoString);
            return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        }

        // --- Copy to Clipboard ---
        function copyToClipboard(text, button) {
            navigator.clipboard.writeText(text).then(() => {
                const originalText = button.innerHTML;
                button.innerHTML = `<i class="fas fa-check"></i> Copied!`;
                setTimeout(() => {
                    button.innerHTML = originalText;
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        }

        // --- Read Aloud ---
        function toggleReadAloud(button, text) {
            if ('speechSynthesis' in window) {
                if (speechSynthesisUtterance && speechSynthesis.speaking) {
                    speechSynthesis.cancel();
                    button.innerHTML = `<i class="fas fa-volume-up"></i>`;
                } else {
                    speechSynthesisUtterance = new SpeechSynthesisUtterance(text);
                    speechSynthesisUtterance.onstart = () => {
                        button.innerHTML = `<i class="fas fa-volume-mute"></i>`;
                    };
                    speechSynthesisUtterance.onend = () => {
                        button.innerHTML = `<i class="fas fa-volume-up"></i>`;
                    };
                    speechSynthesis.speak(speechSynthesisUtterance);
                }
            } else {
                alert("Speech synthesis not supported in this browser.");
            }
        }

        // --- Share/Export Menu ---
        function showShareExportMenu(button, content) {
            // For Phase 1, we'll just mock the share link and client-side downloads
            const shareMenu = document.createElement('div');
            shareMenu.classList.add('message-actions-menu'); // You'd need to style this
            shareMenu.innerHTML = `
                <button>Copy as Markdown</button>
                <button>Download as .txt</button>
                <button>Download as PDF</button>
                <button>Share Link (Mock)</button>
            `;
            // Position the menu near the button
            button.parentNode.appendChild(shareMenu);

            shareMenu.querySelector('button:nth-child(1)').addEventListener('click', () => {
                copyToClipboard(content, button);
                shareMenu.remove();
            });
            shareMenu.querySelector('button:nth-child(2)').addEventListener('click', () => {
                downloadTextAsFile(content, 'nexo-ai-chat.txt');
                shareMenu.remove();
            });
            shareMenu.querySelector('button:nth-child(3)').addEventListener('click', () => {
                printPdf(content); // Use browser print to PDF
                shareMenu.remove();
            });
            shareMenu.querySelector('button:nth-child(4)').addEventListener('click', () => {
                const mockShareId = generateUniqueId();
                const mockShareLink = `${window.location.origin}/share/${mockShareId}`;
                copyToClipboard(mockShareLink, button);
                alert(`Mock Share Link (copied): ${mockShareLink}`);
                shareMenu.remove();
            });

            // Remove menu when clicking outside
            document.addEventListener('click', (e) => {
                if (!shareMenu.contains(e.target) && e.target !== button) {
                    shareMenu.remove();
                }
            }, { once: true });
        }

        function downloadTextAsFile(text, filename) {
            const blob = new Blob([text], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        function printPdf(content) {
            const printWindow = window.open('', '_blank');
            printWindow.document.write(`
                <html>
                <head>
                    <title>Nexo AI Chat</title>
                    <style>
                        body { font-family: sans-serif; margin: 20px; }
                        pre { background-color: #f0f0f0; padding: 10px; border-radius: 5px; overflow-x: auto; }
                        blockquote { border-left: 4px solid #ccc; padding-left: 10px; color: #666; }
                    </style>
                </head>
                <body>
                    <h1>Nexo AI Chat Export</h1>
                    <div>${marked.parse(content)}</div>
                </body>
                </html>
            `);
            printWindow.document.close();
            printWindow.print();
        }

        // --- Edit User Message ---
        function editUserMessage(button, messageId, originalContent) {
            const messageContentDiv = button.closest('.message-content-wrapper').querySelector('.message-content');
            messageContentDiv.innerHTML = `
                <textarea class="edit-textarea">${originalContent}</textarea>
                <div class="edit-actions">
                    <button class="btn btn-primary save-edit-btn">Save</button>
                    <button class="btn cancel-edit-btn">Cancel</button>
                </div>
            `;
            const textarea = messageContentDiv.querySelector('.edit-textarea');
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';

            messageContentDiv.querySelector('.save-edit-btn').addEventListener('click', () => {
                const newContent = textarea.value;
                // Find the message in currentChat and update it
                const messageIndex = currentChat.findIndex(msg => msg.messageId === messageId);
                if (messageIndex !== -1) {
                    currentChat[messageIndex].content = newContent;
                    // Trigger regeneration for this message
                    regenerateResponse(messageId, newContent);
                }
                // Re-render the chat to reflect changes
                renderCurrentChat();
            });

            messageContentDiv.querySelector('.cancel-edit-btn').addEventListener('click', () => {
                messageContentDiv.innerHTML = DOMPurify.sanitize(marked.parse(originalContent));
            });
        }

        function renderCurrentChat() {
            messagesArea.innerHTML = '';
            currentChat.forEach(msg => displayMessage(msg.role, msg.content, msg.timestamp, false, msg.messageId));
            messagesArea.scrollTop = messagesArea.scrollHeight;
        }

        // --- Regenerate Response ---
        function regenerateResponse(messageId, userMessageContent = null) {
            const messageIndex = currentChat.findIndex(msg => msg.messageId === messageId);
            if (messageIndex === -1) return;

            // Remove the AI response that corresponds to this user message, and any subsequent messages
            currentChat.splice(messageIndex + 1);

            const userMessage = currentChat[messageIndex];
            if (userMessageContent) {
                userMessage.content = userMessageContent;
            }

            renderCurrentChat();
            sendMessage(userMessage.content); // Resend the user message
        }

        // --- Main Send Message Logic ---
        async function sendMessage(messageText = chatInput.value) {
            if (messageText.trim() === "" || isStreaming) return;

            const userMessageId = generateUniqueId();
            displayMessage("user", messageText, undefined, true, userMessageId);
            currentChat.push({ role: "user", content: messageText, timestamp: new Date().toISOString(), messageId: userMessageId });

            chatInput.value = "";
            autoResizeTextarea();
            sendButton.disabled = true;
            clearInputBtn.style.display = "none";

            // Auto-name chat if it's a new one
            if (!currentChatId && !incognitoMode) {
                currentChatId = generateUniqueId();
                const chatTitle = messageText.substring(0, 40) + (messageText.length > 40 ? "..." : "");
                chatHistory[currentChatId] = { title: chatTitle, messages: [], timestamp: Date.now(), pinned: false };
                saveChatHistory();
                renderChatHistory();
            }

            // Add message to current chat history (if not incognito)
            if (!incognitoMode) {
                chatHistory[currentChatId].messages.push({ role: "user", content: messageText, timestamp: new Date().toISOString(), messageId: userMessageId });
                saveChatHistory();
            }

            // Show typing indicator
            const typingIndicator = document.createElement("div");
            typingIndicator.classList.add("typing-indicator");
            typingIndicator.innerHTML = `
                <div class="avatar">🤖</div>
                <div class="typing-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            `;
            messagesArea.appendChild(typingIndicator);
            messagesArea.scrollTop = messagesArea.scrollHeight;

            sendButton.innerHTML = `<i class="fas fa-stop"></i>`;
            sendButton.classList.add("stop-button");
            isStreaming = true;
            abortController = new AbortController();
            const signal = abortController.signal;

            let aiResponseContent = "";
            const aiMessageId = generateUniqueId();
            let aiMessageBubble = null;
            let thinkingBox = null;
            let thinkingContentDiv = null;
            let isThinking = false;
            let isSearching = false;
            let isResearching = false;
            let researchProgress = "";

            try {
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        messages: currentChat.map(msg => ({ role: msg.role, content: msg.content })),
                        model: modelSelector.value,
                        thinking: thinkingToggle.dataset.mode,
                        research: researchToggle.dataset.mode === "on",
                        user_profile: profileRoleInput.value,
                        custom_system_prompt: customSystemPromptTextarea.value,
                        image_data: attachedImage // Send attached image data
                    }),
                    signal,
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const reader = response.body.getReader();
                const decoder = new TextDecoder("utf-8");

                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;

                    const chunk = decoder.decode(value);
                    const lines = chunk.split("\n");

                    for (const line of lines) {
                        if (line.startsWith("data: ")) {
                            const data = line.substring(6);
                            if (data === "[DONE]") {
                                break;
                            }
                            try {
                                const json_data = JSON.parse(data);
                                if (json_data.text) {
                                    aiResponseContent += json_data.text;
                                    if (!aiMessageBubble) {
                                        typingIndicator.remove();
                                        aiMessageBubble = displayMessage("ai", aiResponseContent, undefined, true, aiMessageId);
                                    } else {
                                        aiMessageBubble.querySelector(".message-content").innerHTML = DOMPurify.sanitize(marked.parse(aiResponseContent));
                                        messagesArea.scrollTop = messagesArea.scrollHeight;
                                    }
                                    // If thinking box is open and streaming, auto-expand it
                                    if (thinkingBox && isThinking && !thinkingBox.classList.contains('expanded')) {
                                        thinkingBox.classList.add('expanded');
                                        thinkingContentDiv.style.maxHeight = thinkingContentDiv.scrollHeight + 'px';
                                    }
                                } else if (json_data.searching !== undefined) {
                                    isSearching = json_data.searching;
                                    // Display search indicator in UI
                                    if (isSearching) {
                                        // You'd typically add a temporary message or update a status bar
                                        console.log("Searching the web...");
                                    } else {
                                        console.log("Search complete.");
                                    }
                                } else if (json_data.researching !== undefined) {
                                    isResearching = true;
                                    researchProgress = json_data.researching;
                                    if (researchProgress === "done") {
                                        isResearching = false;
                                        // Remove research indicator
                                    } else {
                                        // Update research indicator in UI
                                        console.log(`Researching: ${researchProgress}`);
                                    }
                                } else if (json_data.verified !== undefined) {
                                    // Display verification badge
                                    if (aiMessageBubble) {
                                        const badge = document.createElement('span');
                                        badge.classList.add('verification-badge');
                                        badge.innerHTML = json_data.verified ? '✓ Verified with sources' : '⚠️ Not verified — consider fact-checking';
                                        aiMessageBubble.querySelector('.message-content-wrapper').appendChild(badge);
                                    }
                                }
                            } catch (e) {
                                console.error("Error parsing JSON from SSE:", e, "Data:", data);
                            }
                        }
                    }
                }
            } catch (error) {
                if (error.name === 'AbortError') {
                    aiResponseContent += " [Stopped]";
                } else {
                    console.error("Error fetching chat response:", error);
                    aiResponseContent += `\n\nError: ${error.message}`;
                }
            } finally {
                typingIndicator.remove();
                sendButton.innerHTML = `<i class="fas fa-arrow-up"></i>`;
                sendButton.classList.remove("stop-button");
                sendButton.disabled = chatInput.value.trim() === "";
                isStreaming = false;
                attachedImage = null; // Clear attached image after sending

                if (aiResponseContent.includes("<thinking>") && aiResponseContent.includes("</thinking>")) {
                    const thinkingBlock = aiResponseContent.match(/<thinking>([\s\S]*?)<\/thinking>/);
                    if (thinkingBlock) {
                        const thinkingText = thinkingBlock[1].trim();
                        aiResponseContent = aiResponseContent.replace(thinkingBlock[0], "").trim();

                        // Re-render the AI message without the thinking block
                        if (aiMessageBubble) {
                            aiMessageBubble.querySelector(".message-content").innerHTML = DOMPurify.sanitize(marked.parse(aiResponseContent));
                        }

                        thinkingBox = document.createElement('div');
                        thinkingBox.classList.add('thinking-box');
                        thinkingBox.innerHTML = `
                            <div class="thinking-box-header">
                                <span>🧠 Thinking...</span>
                                <i class="fas fa-chevron-down"></i>
                            </div>
                            <div class="thinking-box-content">
                                <pre><code>${thinkingText}</code></pre>
                            </div>
                        `;
                        aiMessageBubble.querySelector('.message-content-wrapper').insertBefore(thinkingBox, aiMessageBubble.querySelector('.message-actions'));
                        thinkingContentDiv = thinkingBox.querySelector('.thinking-box-content');

                        thinkingBox.querySelector('.thinking-box-header').addEventListener('click', () => {
                            thinkingBox.classList.toggle('expanded');
                            if (thinkingBox.classList.contains('expanded')) {
                                thinkingContentDiv.style.maxHeight = thinkingContentDiv.scrollHeight + 'px';
                            } else {
                                thinkingContentDiv.style.maxHeight = '0';
                            }
                        });
                        isThinking = true;
                        // Auto-collapse after 1 second if not actively streaming
                        setTimeout(() => {
                            if (thinkingBox && thinkingBox.classList.contains('expanded') && !isStreaming) {
                                thinkingBox.classList.remove('expanded');
                                thinkingContentDiv.style.maxHeight = '0';
                            }
                        }, 1000);
                    }
                }

                // Add AI response to current chat history (if not incognito)
                if (!incognitoMode && aiResponseContent.trim() !== "") {
                    chatHistory[currentChatId].messages.push({ role: "ai", content: aiResponseContent, timestamp: new Date().toISOString(), messageId: aiMessageId });
                    saveChatHistory();
                }
                messagesArea.scrollTop = messagesArea.scrollHeight;
            }
        }

        // --- Starfield Background ---
        function createStar() {
            const star = document.createElement("div");
            star.classList.add("star");
            star.style.width = `${Math.random() * 3 + 1}px`;
            star.style.height = star.style.width;
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.animationDuration = `${Math.random() * 3 + 2}s`;
            star.style.animationDelay = `${Math.random() * 2}s`;
            document.getElementById("starfield").appendChild(star);
        }

        for (let i = 0; i < 100; i++) {
            createStar();
        }

        // --- Voice Input (Web Speech API) ---
        micBtn.addEventListener("click", () => {
            if (isVoiceChatMode) {
                // Exit voice chat mode
                voiceChatModalBackdrop.classList.remove("open");
                isVoiceChatMode = false;
                if (speechSynthesis.speaking) {
                    speechSynthesis.cancel();
                }
                if (recognition) {
                    recognition.stop();
                }
            } else {
                // Toggle between voice-to-text and voice chat mode
                if (micBtn.dataset.mode === "voice-to-text") {
                    startVoiceChatMode();
                } else {
                    startVoiceToText();
                }
            }
        });

        micBtn.addEventListener("contextmenu", (e) => {
            e.preventDefault();
            // Toggle mode on right click/long press
            micBtn.dataset.mode = micBtn.dataset.mode === "voice-to-text" ? "voice-chat" : "voice-to-text";
            alert(`Switched to ${micBtn.dataset.mode === "voice-to-text" ? "Voice-to-Text" : "Voice Chat"} mode.`);
        });

        function startVoiceToText() {
            if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
                alert("Speech recognition not supported in this browser.");
                return;
            }

            recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.interimResults = true;
            recognition.lang = 'en-US'; // Or dynamically set based on user's language

            let finalTranscript = '';

            recognition.onstart = () => {
                micBtn.classList.add("recording");
                console.log("Voice-to-text started...");
            };

            recognition.onresult = (event) => {
                let interimTranscript = '';
                for (let i = event.resultIndex; i < event.results.length; ++i) {
                    if (event.results[i].isFinal) {
                        finalTranscript += event.results[i][0].transcript;
                    } else {
                        interimTranscript += event.results[i][0].transcript;
                    }
                }
                chatInput.value = finalTranscript + interimTranscript;
                autoResizeTextarea();
                sendButton.disabled = chatInput.value.trim() === "";
            };

            recognition.onend = () => {
                micBtn.classList.remove("recording");
                console.log("Voice-to-text ended.");
                if (finalTranscript.trim() !== "") {
                    chatInput.value = finalTranscript.trim();
                    autoResizeTextarea();
                    sendButton.disabled = false;
                }
            };

            recognition.onerror = (event) => {
                console.error('Speech recognition error', event.error);
                micBtn.classList.remove("recording");
            };

            recognition.start();
        }

        function startVoiceChatMode() {
            if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window) || !('speechSynthesis' in window)) {
                alert("Voice chat mode not fully supported in this browser.");
                return;
            }

            isVoiceChatMode = true;
            voiceChatModalBackdrop.classList.add("open");
            voiceStatusText.textContent = "Tap to speak";
            voiceTranscript.textContent = "";

            recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.interimResults = false; // Only final results
            recognition.continuous = false; // Stop after a single utterance
            recognition.lang = 'en-US';

            recognition.onstart = () => {
                voiceMicButton.classList.add("recording");
                voiceStatusText.textContent = "Listening...";
                voiceTranscript.textContent = "";
            };

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                voiceTranscript.textContent = transcript;
                voiceStatusText.textContent = "Processing...";
                sendMessage(transcript); // Send message automatically
            };

            recognition.onend = () => {
                voiceMicButton.classList.remove("recording");
                voiceStatusText.textContent = "Tap to speak";
            };

            recognition.onerror = (event) => {
                console.error('Speech recognition error', event.error);
                voiceStatusText.textContent = "Error. Tap to retry.";
                voiceMicButton.classList.remove("recording");
            };

            voiceMicButton.onclick = () => {
                if (speechSynthesis.speaking) {
                    speechSynthesis.cancel();
                }
                recognition.start();
            };

            voiceChatExitBtn.onclick = () => {
                voiceChatModalBackdrop.classList.remove("open");
                isVoiceChatMode = false;
                if (speechSynthesis.speaking) {
                    speechSynthesis.cancel();
                }
                if (recognition) {
                    recognition.stop();
                }
            };
        }

        // --- Image Upload ---
        attachBtn.addEventListener("click", () => {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/jpeg, image/png, image/webp';
            input.onchange = (e) => {
                const file = e.target.files[0];
                if (file) {
                    if (file.size > 5 * 1024 * 1024) { // 5MB limit
                        alert("Image size exceeds 5MB limit.");
                        return;
                    }
                    const reader = new FileReader();
                    reader.onload = (event) => {
                        attachedImage = event.target.result.split(',')[1]; // Base64 content
                        alert("Image attached! It will be sent with your next message.");
                        // Optionally, display a thumbnail preview
                    };
                    reader.readAsDataURL(file);
                }
            };
            input.click();
        });

        // --- Slash Commands / Prompt Templates ---
        chatInput.addEventListener("input", () => {
            if (chatInput.value.startsWith("/")) {
                // Show slash command suggestions (simplified for now)
                console.log("Showing slash command suggestions...");
                // In a real app, you'd show a dropdown with commands like /summarize, /translate
            }
        });

        // --- Background Tasks (Simplified) ---
        // This would involve polling the /tasks endpoint and updating a UI element
        // For Phase 1, we'll just log to console for now.
        async function fetchBackgroundTasks() {
            try {
                const response = await fetch('/tasks');
                const tasks = await response.json();
                // Update UI with tasks
                console.log("Background Tasks:", tasks);
            } catch (error) {
                console.error("Error fetching tasks:", error);
            }
        }
        // setInterval(fetchBackgroundTasks, 5000); // Poll every 5 seconds

        // --- Share Chat (Mock) ---
        shareBtn.addEventListener("click", () => {
            // This will open a modal for sharing options
            alert("Share functionality is under development. You can copy the current chat content.");
            // For a real implementation, you'd generate a shareable link via the backend
        });

        // --- Sidebar Search ---
        sidebarSearch.addEventListener("input", () => {
            const query = sidebarSearch.value.toLowerCase();
            document.querySelectorAll("#recent-chats .chat-item").forEach(item => {
                const title = item.querySelector(".chat-item-title").textContent.toLowerCase();
                // For full search, you'd also need to search message content
                if (title.includes(query)) {
                    item.style.display = "flex";
                } else {
                    item.style.display = "none";
                }
            });
        });

        // --- Initialize ---
        loadSettings();
        renderChatHistory();
        if (currentChatId) {
            loadChat(currentChatId);
        } else {
            startNewChat();
        }

        // Load highlight.js for syntax highlighting
        const hljsScript = document.createElement('script');
        hljsScript.src = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js";
        document.head.appendChild(hljsScript);

        // Load marked.js for markdown parsing
        const markedScript = document.createElement('script');
        markedScript.src = "https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js";
        markedScript.onload = () => {
            marked.setOptions({
                gfm: true,
                breaks: true,
                highlight: function(code, lang) {
                    const language = hljs.getLanguage(lang) ? lang : 'plaintext';
                    return hljs.highlight(code, { language }).value;
                }
            });
        };
        document.head.appendChild(markedScript);


    </script>
</body>
</html>
