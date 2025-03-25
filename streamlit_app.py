import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random

st.set_page_config(page_title="Better Than You", layout="wide")

# Estilo centrado y oscuro para foco narrativo
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0d0d0d, #1a0033);
    color: #e0e0ff;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3, h4 {
    color: #ff66ff;
    text-align: center;
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
.centered {
    max-width: 700px;
    margin: auto;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Refresh loop para animaciones
st_autorefresh(interval=1000, key="refresh")

# Definir actividades por nivel de sofisticación
activities = [
    {"name": "Pick apples", "emoji": "🍎", "icon": "🧺"},
    {"name": "Clean the house", "emoji": "🧹", "icon": "🧽"},
    {"name": "Drive a car", "emoji": "🚗", "icon": "🛣️"},
    {"name": "Cook a meal", "emoji": "🍳", "icon": "👨‍🍳"},
    {"name": "Diagnose a patient", "emoji": "🩺", "icon": "🧬"},
    {"name": "Write a poem", "emoji": "📜", "icon": "✍️"},
    {"name": "Paint a picture", "emoji": "🎨", "icon": "🖌️"},
    {"name": "Compose music", "emoji": "🎼", "icon": "🎵"},
    {"name": "Offer emotional support", "emoji": "🧠", "icon": "🫂"},
    {"name": "Spend time with your children", "emoji": "👨‍👧‍👦", "icon": "🧸"},
]

# Inicializar estado
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
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='centered'>", unsafe_allow_html=True)

# Introducción
if st.session_state.level == 0 and st.session_state.count == 0 and len(st.session_state.robots) == 0:
    st.title("Better Than You")
    st.markdown("### Let's see how much of your life a robot can automate.")
    st.markdown("Do the task. Repeat it. Then hand it over. Slowly, your life is no longer yours.")
    st.markdown("### 🧠 Automation progress")
st.markdown("---")

# Mostrar barra de progreso
progress = len(st.session_state.robots)
st.progress(progress / len(activities))

# Tarea actual
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    st.markdown(f"## Current task: {task['name']} {task['emoji']}")
    st.markdown(f"**You've done it {st.session_state.count}/3 times**")

    st.markdown("<div style='min-height: 3em;'>", unsafe_allow_html=True)
    if st.session_state.transition_text:
        st.success(st.session_state.transition_text)

    if st.button(f"✅ Do '{task['name']}'"):
        st.session_state.count += 1
        st.session_state.global_count += 1
        st.session_state.transition_text = ""
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.count >= 3:
        if st.button(f"🤖 Automate '{task['name']}' with a robot"):
            st.session_state.robots.append(task)
            st.session_state.robot_anim[task['name']] = 0

            if st.session_state.level + 1 < len(activities):
                next_task = activities[st.session_state.level + 1]
                st.session_state.transition_text = f"I’ve been freed from '{task['name']}'. I finally get to '{next_task['name']}'... or so I thought."
            else:
                st.session_state.transition_text = "Even family time... replaced."

            st.session_state.level += 1
            st.session_state.count = 0

# Mostrar robots trabajando
if len(st.session_state.robots) > 0:
    st.markdown("### 🤖 Robots now control these tasks:")
    for task in st.session_state.robots:
        container = st.empty()
        frame = st.session_state.robot_anim[task['name']]
        icons = [task['emoji']] * 10
        icons[frame % 10] = "✅"
        display = " ".join(icons)
        container.markdown(f"<div class='task-box'>{task['icon']} {task['name']} → {display}</div>", unsafe_allow_html=True)
        st.session_state.robot_anim[task['name']] = (frame + 1) % 10

# Final: todas las tareas automatizadas
if st.session_state.level >= len(activities):
    st.markdown("## Everything you do, a robot can do better.")
    st.markdown("You no longer need to farm, clean, write, create… or even love.")
    st.markdown("#### So… what's the point of your existence?")
    st.markdown("""
    <div style='margin-top: 30px; text-align: center;'>
        <a href='https://aish.com/humans-vs-ai-will-we-remain-relevant/' target='_blank' style='
            display: inline-block;
            background-color: #ff1aff;
            color: white;
            padding: 1.2em 2em;
            font-size: 1.4em;
            border-radius: 12px;
            text-decoration: none;
            font-weight: bold;
            box-shadow: 0 0 20px #ff1aff;
        '>🌌 Discover what makes you human</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧠 Automation progress")
st.markdown("---")
st.markdown("📸 **If this made you think — share it.** Screenshot your screen. Tag [#BetterThanYou] on social media.")

st.markdown("</div>", unsafe_allow_html=True)
