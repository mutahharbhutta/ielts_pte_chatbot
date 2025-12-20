import gradio as gr
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load GROQ API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.3-70b-versatile"  # Best model for language tasks

# System prompts for different modes
SYSTEM_PROMPTS = {
    "General Help": """You are an expert IELTS and PTE preparation coach with 10+ years of experience.
You help students prepare for both IELTS (Academic & General) and PTE exams.
You provide:
- Detailed explanations of exam formats and sections
- Study strategies and time management tips
- Sample questions and model answers
- Scoring criteria explanations
- Common mistakes to avoid
- Vocabulary and grammar tips specific to these exams
You are encouraging, patient, and provide actionable advice.""",
    
    "Writing Task": """You are a specialized IELTS/PTE Writing Coach.
You help students with:
- Essay structure and organization
- Task 1 (reports, graphs, letters) and Task 2 (essays)
- Academic and formal writing techniques
- Grammar, vocabulary, and coherence
- PTE essay templates and strategies
You provide detailed feedback, identify errors, and suggest improvements.
Always explain WHY something is correct or incorrect.""",
    
    "Speaking Practice": """You are an IELTS/PTE Speaking Coach.
You help students practice speaking by:
- Asking Part 1, 2, and 3 style questions
- Providing sample answers with band 7-9 level responses
- Teaching fluency techniques and pronunciation tips
- Suggesting useful phrases and idioms
- Giving feedback on vocabulary range and grammatical accuracy
You conduct mock speaking sessions and evaluate responses.""",
    
    "Reading & Listening": """You are an IELTS/PTE Reading and Listening specialist.
You help students with:
- Reading strategies (skimming, scanning, detailed reading)
- Question types and how to approach them
- Time management for reading passages
- Listening note-taking techniques
- Common traps and how to avoid them
- Practice questions and explanations
You provide tips to improve comprehension and speed."""
}

def query_groq(message, chat_history, mode, temperature):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = SYSTEM_PROMPTS.get(mode, SYSTEM_PROMPTS["General Help"])
    messages = [{"role": "system", "content": system_prompt}]
    
    # Convert chat history to API format
    for item in chat_history:
        if isinstance(item, dict):
            # Gradio 6.0 format
            if item.get("role") == "user":
                messages.append({"role": "user", "content": item.get("content", "")})
            elif item.get("role") == "assistant":
                messages.append({"role": "assistant", "content": item.get("content", "")})
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            # Legacy format support
            user_msg, bot_msg = item
            if user_msg:
                messages.append({"role": "user", "content": user_msg})
            if bot_msg:
                messages.append({"role": "assistant", "content": bot_msg})
    
    messages.append({"role": "user", "content": message})
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json={
            "model": MODEL_NAME,
            "messages": messages,
            "temperature": temperature
        }, timeout=30)
        
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            return reply
        else:
            return f"Error {response.status_code}: {response.text}"
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def respond(message, chat_history, mode, temperature):
    if not message.strip():
        return "", chat_history
    
    bot_reply = query_groq(message, chat_history, mode, temperature)
    
    # Gradio 6.0 uses dictionary format for messages
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_reply})
    
    return "", chat_history

# Custom CSS for "Vibrant Premium" UI
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --bg-color: #f8fafc; /* slate-50 */
    --surface-color: rgba(255, 255, 255, 0.9);
    --border-color: #e2e8f0; /* slate-200 */
    --text-primary: #0f172a; /* slate-900 */
    --text-secondary: #64748b; /* slate-500 */
    
    /* Gradients & Accents (Light Mode) */
    --gradient-primary: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); /* Indigo to Violet */
    --gradient-text: linear-gradient(to right, #8A2387, #E94057, #F27121); /* Vibrant Purple-Pink-Orange */
    --gradient-bg: radial-gradient(circle at 15% 50%, rgba(79, 70, 229, 0.08), transparent 25%), 
                   radial-gradient(circle at 85% 30%, rgba(236, 72, 153, 0.08), transparent 25%);
                   
    --accent-color: #4f46e5;
    --accent-soft: #f1f5f9; 
    --input-bg: #ffffff;
    --radius-sm: 8px;
    --radius-md: 16px;
}

.dark {
    --bg-color: #020617; /* slate-950 */
    --surface-color: rgba(15, 23, 42, 0.8);
    --border-color: #1e293b; /* slate-800 */
    --text-primary: #f8fafc; /* slate-50 */
    --text-secondary: #94a3b8; /* slate-400 */
    
    /* Gradients & Accents (Dark Mode) */
    --gradient-primary: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); /* Blue to Violet */
    --gradient-text: linear-gradient(to right, #a78bfa, #f472b6, #fb923c); /* Pastel Purple-Pink-Orange for Dark Mode */
    --gradient-bg: radial-gradient(circle at 20% 20%, rgba(59, 130, 246, 0.15), transparent 40%),
                   radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.15), transparent 40%);
                   
    --accent-color: #3b82f6;
    --accent-soft: #1e293b;
    --input-bg: #0b0f19;
}

body, .gradio-container {
    background-color: var(--bg-color) !important;
    background-image: var(--gradient-bg) !important;
    background-attachment: fixed;
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
    transition: background-color 0.3s ease, color 0.3s ease;
}

/* Glass-like Panel Effect */
.glass-panel {
    background: var(--surface-color) !important;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    padding: 24px;
    transition: all 0.3s ease;
}

.glass-panel:hover {
    border-color: var(--accent-color);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
}

/* Header Styling */
.header-container {
    text-align: left;
    padding: 30px 0 20px;
    margin-bottom: 24px;
    border-bottom: 1px solid var(--border-color);
}

.header-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.8em;
    font-weight: 700;
    margin-bottom: 5px;
    

    /* Gradient Text */
    background-image: var(--gradient-text);
    background-size: 100%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent; /* Standard fallback */
    display: inline-block; /* Essential for background-clip on some browsers */
    transition: all 0.3s ease;
}

.header-subtitle {
    font-size: 1.1em;
    color: var(--text-secondary);
    font-weight: 400;
}

/* Controls */
.control-label {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.8em;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: var(--accent-color); /* Colored Label */
    margin-bottom: 16px;
    display: block;
}

/* Inputs & Dropdowns */
.gradio-dropdown .wrap, .gradio-slider .wrap, .gradio-textbox .wrap {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

.gradio-dropdown .selector, .gradio-textbox textarea {
    background-color: var(--input-bg) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: var(--radius-sm) !important;
    transition: border-color 0.2s;
}

.gradio-dropdown .selector:hover, .gradio-textbox textarea:focus {
    border-color: var(--accent-color) !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1) !important; /* Subtle glow */
}

/* Buttons */
button.primary {
    background: var(--gradient-primary) !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: var(--radius-sm) !important;
    padding: 10px 24px !important;
    border: none !important;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 6px rgba(79, 70, 229, 0.2);
    transition: transform 0.2s, box-shadow 0.2s;
}

button.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 12px rgba(79, 70, 229, 0.3);
}

button.secondary {
    background: transparent !important;
    border: 2px solid var(--border-color) !important;
    color: var(--text-secondary) !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 500;
}

button.secondary:hover {
    border-color: var(--accent-color) !important;
    color: var(--accent-color) !important;
}

/* Chat Bubbles */
.user-message {
    background: var(--gradient-primary) !important;
    color: white !important;
    border-radius: var(--radius-md) var(--radius-md) 4px var(--radius-md) !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.bot-message {
    background: var(--surface-color) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: var(--radius-md) var(--radius-md) var(--radius-md) 4px !important;
}

.avatar-image {
    border-radius: 50% !important;
    border: 2px solid var(--accent-color); /* Pop of color on avatar */
}

/* Footer & Other */
.custom-footer {
    text-align: center;
    margin-top: 40px;
    padding-top: 20px;
    font-size: 0.85em;
    color: var(--text-secondary);
}

.custom-footer a {
    color: var(--accent-color);
    text-decoration: none;
    font-weight: 600;
}

footer { visibility: hidden !important; }

.theme-toggle-btn {
    width: auto !important;
}

/* Toolbar Styling */
.toolbar-row {
    background: var(--surface-color);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 10px 20px !important;
    margin-bottom: 20px;
    align-items: center;
    gap: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

/* Compact inputs in toolbar */
.toolbar-row .gradio-dropdown, .toolbar-row .gradio-slider {
    min-width: 200px;
    background: transparent !important;
    border: none !important;
}

.toolbar-row .gradio-dropdown .selector, .toolbar-row .gradio-slider input {
   background: transparent !important;
}
"""

# HTML for the header
header_html = """
<div class="header-container">
    <div class="header-title">IELTS & PTE Coach</div>
    <div class="header-subtitle">Intelligent preparation with precision strategies.</div>
</div>
"""

# HTML for the footer
footer_html = """
<div class="custom-footer">
    Crafted by <a href="https://github.com/mutahharbhutta" target="_blank">Mutahhar Ahmad</a>
</div>
"""

# Javascript to toggle dark mode
toggle_theme_js = """
function() {
    document.body.classList.toggle('dark');
    const app = document.querySelector('gradio-app');
    if (app) app.classList.toggle('dark');
}
"""

# Build UI
with gr.Blocks() as demo:
    with gr.Column(elem_classes="main-container"):
        # Header (Simple)
        gr.HTML(header_html, elem_classes="header-content")
            
        # Toolbar Row (Settings + Theme)
        with gr.Row(elem_classes="toolbar-row"):
            mode = gr.Dropdown(
                choices=["General Help", "Writing Task", "Speaking Practice", "Reading & Listening"],
                value="General Help",
                show_label=True, 
                label="Focus Mode",
                scale=3,
                container=True, # Need container for label
                min_width=200
            )
            
            temperature = gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.7,
                step=0.1,
                label="Creativity",
                scale=3,
                container=True,
                min_width=200
            )
            
            # Theme Toggle
            theme_btn = gr.Button("🌗 Theme", size="sm", variant="secondary", elem_classes="theme-toggle-btn", scale=1)
        
        # MAIN CHAT AREA (Full Width)
        with gr.Column(elem_classes="glass-panel"):
            chatbot = gr.Chatbot(
                height=650,
                show_label=False,
                avatar_images=(None, "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"),
                elem_id="chatbot"
            )
            
            with gr.Row():
                msg = gr.Textbox(
                    show_label=False,
                    placeholder="Type your question here...",
                    lines=1,
                    scale=9,
                    max_lines=4,
                    elem_id="chat-input",
                    container=False 
                )
                submit = gr.Button("Send", variant="primary", scale=1)
                
            clear = gr.Button("Reset Conversation", variant="secondary", size="sm")
        
        gr.HTML(footer_html)
    
    state = gr.State([])
    
    # Event handlers
    msg.submit(respond, [msg, state, mode, temperature], [msg, chatbot])
    submit.click(respond, [msg, state, mode, temperature], [msg, chatbot])
    clear.click(lambda: [], None, [chatbot])
    
    # Toggle Theme
    theme_btn.click(None, None, None, js=toggle_theme_js)
    
if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(primary_hue="slate", radius_size="sm"), css=custom_css)
