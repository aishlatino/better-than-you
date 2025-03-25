import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random

# AUTOREFRESH every 1000ms = 1 second
st_autorefresh(interval=1000, key="refresh")

# Tasks and associated "things" to act on
activities = [
    {"name": "Pick apples", "emoji": "🍎", "icon": "🧺"},
    {"name": "Sweep the floor", "emoji": "💨", "icon": "🧹"},
    {"name": "Drive a car", "emoji": "🛣️", "icon": "🚗"},
    {"name": "Write a poem", "emoji": "📜", "icon": "✍️"},
    {"name": "Paint a picture", "emoji": "🖼️", "icon": "🎨"},
    {"name": "Diagnose a patient", "emoji": "🧬", "icon": "🩺"},
    {"name": "Teach a class", "emoji": "📚", "icon": "👩‍🏫"},
    {"name": "Compose music", "emoji": "🎵", "icon": "🎼"},
    {"name": "Write code", "emoji": "⌨️", "icon": "💻"},
    {"name": "Counsel a friend", "emoji": "🫂", "icon": "🧠"},
]

# Setup session state
if "level" not in st.session_state:
    st.session_state.level = 0
if "count" not in st.session_state:
    st.session_state.count = 0
if "robots" not in st.session_state:
    st.session_state.robots = []
if "global_count" not in st.session_state:
    st.session_state.global_count = 0
if "robot_anim_state" not in st.session_state:
    st.session_state.robot_anim_state = {}  # Holds state of each robot animation

# Title & Intro
st.title("Better Than You")
st.subheader("Let's get to work.")

# Show current task if not finished
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    st.markdown(f"### Current task: {task['name']} {task['emoji']}")
    st.markdown(f"You've done it **{st.session_state.count}/5** times")
    st.markdown(f"**Total human actions done:** {st.session_state.global_count}")

    if st.button(f"Do '{task['name']}'"):
        st.session_state.count += 1
        st.session_state.global_count += 1

    # After 5 actions, allow robot creation
    if st.session_state.count >= 5:
        if st.button(f"🤖 Buy robot to automate '{task['name']}'"):
            st.session_state.robots.append(task)
            st.session_state.robot_anim_state[task['name']] = random.randint(0, 3)
            st.session_state.level += 1
            st.session_state.count = 0

# Show robots only after at least one is acquired
if len(st.session_state.robots) > 0:
    st.markdown("## 🤖 Robots working for you:")
    for i, robot in enumerate(st.session_state.robots):
        spot = st.empty()
        state = st.session_state.robot_anim_state.get(robot['name'], 0)
        max_len = 10
        line = [" "]*max_len
        if state < max_len:
            line[state] = robot['emoji']
            st.session_state.robot_anim_state[robot['name']] += 1
        else:
            st.session_state.robot_anim_state[robot['name']] = 0
        progress = " ".join(line)
        spot.markdown(f"{robot['icon']} {robot['name']} → {progress}")

# Ending screen
if st.session_state.level >= len(activities):
    st.header("Everything you do, a robot can do better.")
    st.subheader("So… what's the meaning of your existence?")
    st.markdown("### 🤖 All your robots are working:")
    for robot in st.session_state.robots:
        st.write(f"{robot['icon']} {robot['name']}")
    if st.button("🌟 Find Meaning at Aish.com"):
        st.markdown("[Click here to explore](https://www.aish.com)", unsafe_allow_html=True)
