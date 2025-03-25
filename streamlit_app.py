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

# Set up session state
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

st.title("Better Than You")
st.subheader("Let's get to work.")

# Current task loop
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    st.markdown(f"### Current task: {task['name']} {task['emoji']}")
    st.markdown(f"You've done it **{st.session_state.count}/5** times")
    st.markdown(f"**Total human actions completed:** {st.session_state.global_count}")

    if st.button(f"Do '{task['name']}'"):
        st.session_state.count += 1
        st.session_state.global_count += 1

    if st.session_state.count >= 5:
        if st.button(f"🤖 Buy robot to automate '{task['name']}'"):
            st.session_state.robots.append(task)
            st.session_state.robot_anim[task['name']] = 0
            st.session_state.level += 1
            st.session_state.count = 0
            st.success(f"A robot is now doing: {task['name']}")

# Show robot animations only after first robot
if len(st.session_state.robots) > 0:
    st.markdown("## 🤖 Robots working for you:")
    for task in st.session_state.robots:
        container = st.empty()
        frame = st.session_state.robot_anim[task['name']]
        icons = [task['emoji']] * 5
        icons[frame % 5] = "✅"
        display = " ".join(icons)
        container.markdown(f"{task['icon']} {task['name']} → {display}")
        st.session_state.robot_anim[task['name']] = (frame + 1) % 5

# Final screen with CTA
if st.session_state.level >= len(activities):
    st.header("Everything you do, a robot can do better.")
    st.markdown("#### So… what's the point of your existence?")
    st.markdown("### 🤖 Your life is now fully automated:")

    for task in st.session_state.robots:
        st.write(f"{task['icon']} {task['name']}")

    st.markdown("---")
    st.markdown("### 👉 [Discover it here](https://www.aish.com)", unsafe_allow_html=True)
