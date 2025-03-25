import streamlit as st
st.set_page_config(page_title="Better Than You", layout="wide")
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components
import random

# Estilo Blade Runner (HTML + CSS insertado)
custom_css = """
<style>
body {
    background: linear-gradient(135deg, #0d0d0d, #1a0033);
    color: #e0e0ff;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3, h4 {
    color: #ff66ff;
}
.stButton>button {
    background-color: #1a1a1a;
    color: #80f0ff;
    border: 1px solid #80f0ff;
    padding: 0.6em 1.2em;
    border-radius: 8px;
    font-size: 1.1em;
    transition: 0.3s ease;
}
.stButton>button:hover {
    background-color: #80f0ff;
    color: #0d0d0d;
}
.task-box {
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid #444;
    padding: 0.75em;
    margin: 0.5em 0;
    border-radius: 10px;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("<div style='max-width: 700px; margin: auto; text-align: center;'>", unsafe_allow_html=True)

# Auto-refresh loop (every 0.5 sec)
st_autorefresh(interval=500, key="refresh")

activities = [
    {"name": "Pick apples", "emoji": "🍎", "icon": "🧺"},
    {"name": "Clean the house", "emoji": "🧹", "icon": "🧽"},
    {"name": "Drive a car", "emoji": "🚗", "icon": "🛣️"},
    {"name": "Cook a meal", "emoji": "🍳", "icon": "👨‍🍳"},
    {"name": "Diagnose a patient", "emoji": "🩺", "icon": "🧬"},
    {"name": "Write a poem", "emoji": "📜", "icon": "✍️"},
    {"name": "Paint a picture", "emoji": "🎨", "icon": "🖌️"},
    {"name": "Compose music", "emoji": "🎼", "icon": "🎵"},
    {"name": "Write code", "emoji": "💻", "icon": "⌨️"},
    {"name": "Offer emotional support", "emoji": "🧠", "icon": "🫂"},
]

if "level" not in st.session_state:
    st.session_state.level = 0
if "count" not in st.session_state:
    st.session_state.count = 0
if "robots" not in st.session_state:
    st.session_state.robots = []
if "global_count" not in st.session_state:
    st.session_state.global_count = 0
if "robot_anim" not in st.session_state:
    st.session_state.robot_anim = {}
if "transition_text" not in st.session_state:
    st.session_state.transition_text = ""

st.title("Better Than You")
st.markdown("### Start working. Do the task. Repeat it.")

# MAIN TASK LOOP
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]

    if st.session_state.transition_text:
        st.markdown(f"<div class='task-box'><strong>{st.session_state.transition_text}</strong></div>", unsafe_allow_html=True)

    st.markdown(f"### Current task: <span style='color:#80f0ff'>{task['name']} {task['emoji']}</span>", unsafe_allow_html=True)
    st.markdown(f"**Total human actions completed:** {st.session_state.global_count}")

    if st.button(f"Do '{task['name']}'"):
        st.session_state.count += 1
        st.session_state.global_count += 1
        st.session_state.transition_text = ""

    if st.session_state.count >= 5:
        if st.button(f"🤖 Buy robot to automate '{task['name']}'"):
            st.session_state.robots.append(task)
            st.session_state.robot_anim[task['name']] = 0

            if st.session_state.level + 1 < len(activities):
                next_task = activities[st.session_state.level + 1]
                st.session_state.transition_text = f"I no longer have to spend time on '{task['name']}'. Now I can '{next_task['name']}'."

            st.session_state.level += 1
            st.session_state.count = 0

# ROBOTS IN ACTION
if len(st.session_state.robots) > 0:
    st.markdown("## 🤖 Robots working for you:")
    for task in st.session_state.robots:
        container = st.empty()
        frame = st.session_state.robot_anim[task['name']]
        icons = [task['emoji']] * 10
        icons[frame % 10] = "✅"
        display = " ".join(icons)
        container.markdown(f"<div class='task-box'>{task['icon']} {task['name']} → {display}</div>", unsafe_allow_html=True)
        st.session_state.robot_anim[task['name']] = (frame + 1) % 10

# FINAL MESSAGE & CTA
if st.session_state.level >= len(activities):
    st.header("Everything you do, a robot can do better.")
    
    summary = ", ".join([f"{t['name'].lower()}" for t in st.session_state.robots])
    st.markdown(f"Robots now do it all — {summary}. Your life is now fully automated.")
    
    st.markdown("#### So… what's the point of your existence?")
    
    cta_url = "https://aish.com/humans-vs-ai-will-we-remain-relevant/"
    st.markdown(f"""
        <div style='margin-top: 30px; text-align: center;'>
            <a href='{cta_url}' target='_blank' style='
                display: inline-block;
                background-color: #ff1aff;
                color: white;
                padding: 1.2em 2em;
                font-size: 1.4em;
                border-radius: 12px;
                text-decoration: none;
                font-weight: bold;
                box-shadow: 0 0 20px #ff1aff;
            '>🌌 Discover it here</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
