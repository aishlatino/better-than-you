import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random

st.set_page_config(page_title="Better Than You", layout="wide")

# Inject corrected CSS
custom_css = """
<style>
html, body {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #0e0e0e, #1f003f);
    color: #f0f0f0;
    font-family: 'Inter', sans-serif;
    overflow-y: auto !important;
}

section {
    max-width: 800px;
    margin: auto;
    margin-top: 3em;
    padding: 2em;
    background: rgba(255, 255, 255, 0.04);
    border-radius: 20px;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.4s ease;
}

h1 {
    font-size: 3em;
    font-weight: 700;
    color: #e668ff;
    text-align: center;
    margin-bottom: 0.3em;
}

h3 {
    color: #8be9fd;
    font-weight: 400;
    text-align: center;
    margin-bottom: 2em;
}

.stButton>button {
    background-color: #8be9fd;
    color: #0e0e0e;
    border: none;
    border-radius: 12px;
    padding: 0.75em 1.5em;
    font-size: 1.1em;
    font-weight: bold;
    transition: 0.3s ease-in-out;
    box-shadow: 0 0 12px #8be9fd;
}

.stButton>button:hover {
    background-color: #50c8ec;
    box-shadow: 0 0 25px #50c8ec;
    transform: scale(1.02);
}

.task-box {
    padding: 0.8em 1em;
    margin: 1em 0;
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    border: 1px solid #333;
}

.cta-button {
    display: inline-block;
    margin: 2em auto;
    background: #ff4bd8;
    color: white;
    padding: 1.2em 2em;
    font-size: 1.3em;
    font-weight: bold;
    border-radius: 12px;
    text-decoration: none;
    box-shadow: 0 0 20px #ff4bd8;
    transition: all 0.3s ease;
}

.cta-button:hover {
    background: #ff1aff;
    box-shadow: 0 0 30px #ff1aff;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
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

st.markdown("<section>", unsafe_allow_html=True)
st.markdown("<h1>Better Than You</h1>", unsafe_allow_html=True)
st.markdown("<h3>Start working. Do the task. Repeat it.</h3>", unsafe_allow_html=True)

if st.session_state.level < len(activities):
    task = activities[st.session_state.level]

    if st.session_state.transition_text:
        st.markdown(f"<div class='task-box'><b>{st.session_state.transition_text}</b></div>", unsafe_allow_html=True)

    st.markdown(f"### Current task: {task['name']} {task['emoji']}")
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

if st.session_state.level >= len(activities):
    st.header("Everything you do, a robot can do better.")
    summary = ", ".join([f"{t['name'].lower()}" for t in st.session_state.robots])
    st.markdown(f"Robots now do it all — {summary}. Your life is now fully automated.")
    st.markdown("#### So… what's the point of your existence?")
    st.markdown("""
        <div style='text-align:center'>
            <a href='https://aish.com/humans-vs-ai-will-we-remain-relevant/' target='_blank' class='cta-button'>🌌 Discover it here</a>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</section>", unsafe_allow_html=True)
