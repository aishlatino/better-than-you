import streamlit as st
st.set_page_config(page_title="Better Than You", layout="centered")
from streamlit_autorefresh import st_autorefresh
import random

# Auto-refresh loop (every 1.2 sec)
st_autorefresh(interval=1200, key="refresh")

activities = [
    {"name": "Pick apples", "emoji": "🍎", "icon": "🧺"},
    {"name": "Sweep the floor", "emoji": "💨", "icon": "🧹"},
    {"name": "Drive a car", "emoji": "🛣️", "icon": "🚗"},
    {"name": "Write a poem", "emoji": "📜", "icon": "✍️"},
    {"name": "Paint a picture", "emoji": "🎨", "icon": "🖌️"},
    {"name": "Diagnose a patient", "emoji": "🧬", "icon": "🩺"},
    {"name": "Teach a class", "emoji": "📚", "icon": "👩‍🏫"},
    {"name": "Compose music", "emoji": "🎵", "icon": "🎼"},
    {"name": "Write code", "emoji": "⌨️", "icon": "💻"},
    {"name": "Counsel a friend", "emoji": "🫂", "icon": "🧠"},
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
st.subheader("Start working. Do the task. Repeat it. Again and again — until a robot replaces you.")

# MAIN TASK LOOP
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]

    # Show transition text if available
    if st.session_state.transition_text:
        st.success(st.session_state.transition_text)
        st.session_state.transition_text = ""

    st.markdown(f"### Current task: {task['name']} {task['emoji']}")
    st.markdown(f"**Total human actions completed:** {st.session_state.global_count}")

    if st.button(f"Do '{task['name']}'"):
        st.session_state.count += 1
        st.session_state.global_count += 1

    if st.session_state.count >= 5:
        if st.button(f"🤖 Buy robot to automate '{task['name']}'"):
            st.session_state.robots.append(task)
            st.session_state.robot_anim[task['name']] = 0

            # Build transition message
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
        container.markdown(f"{task['icon']} {task['name']} → {display}")
        st.session_state.robot_anim[task['name']] = (frame + 1) % 10

# FINAL MESSAGE & CTA
if st.session_state.level >= len(activities):
    st.header("Everything you do, a robot can do better.")
    
    summary = ", ".join([f"{t['name'].lower()}" for t in st.session_state.robots])
    st.markdown(f"Robots now do it all — {summary}. Your life is now fully automated.")
    
    st.markdown("#### So… what's the point of your existence?")
    
    # Big CTA button using markdown with styling
    cta_url = "https://aish.com/humans-vs-ai-will-we-remain-relevant/"
    st.markdown(f"""
        <div style='margin-top: 20px; text-align: center;'>
            <a href='{cta_url}' target='_blank' style='
                display: inline-block;
                background-color: #ff4b4b;
                color: white;
                padding: 1em 2em;
                font-size: 1.2em;
                border-radius: 10px;
                text-decoration: none;
                font-weight: bold;
            '>🌟 Discover it here</a>
        </div>
    """, unsafe_allow_html=True)
