
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Better Than You", layout="wide")

# Inject styles
st.markdown("""
<style>
body {
    background-color: #0d0d0d;
    color: #e0e0ff;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    color: #ff66ff;
}
.stButton>button {
    background-color: #1a1a1a;
    color: #80f0ff;
    border: 1px solid #80f0ff;
    padding: 0.6em 1.2em;
    border-radius: 8px;
    font-size: 1em;
    transition: 0.3s ease;
    margin: 0.5em;
}
.stButton>button:hover {
    background-color: #80f0ff;
    color: #0d0d0d;
}
.task-box {
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid #444;
    padding: 1em;
    margin: 1em 0;
    border-radius: 10px;
}
.centered {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st_autorefresh(interval=1000, key="refresh")

# Activities
activities = [
    {"name": "Work", "emoji": "💼", "icon": "🧠"},
    {"name": "Write a book", "emoji": "📖", "icon": "✍️"},
    {"name": "Read a book", "emoji": "📚", "icon": "👓"},
    {"name": "Talk to a friend", "emoji": "🗣️", "icon": "🫂"},
    {"name": "Spend time with your kids", "emoji": "👨‍👧‍👦", "icon": "🧸"},
]

# Init session state
if "level" not in st.session_state:
    st.session_state.level = 0
if "robots" not in st.session_state:
    st.session_state.robots = []
if "robot_anim" not in st.session_state:
    st.session_state.robot_anim = {}
if "robot_counts" not in st.session_state:
    st.session_state.robot_counts = {}
if "total_actions" not in st.session_state:
    st.session_state.total_actions = 0

# Title
st.title("Better Than You")
st.markdown("### Why do it yourself when a robot can do it for you?")

# Big counter
st.markdown(f"<h2 class='centered'>🤖 Total automated actions: {st.session_state.total_actions}</h2>", unsafe_allow_html=True)

# Current task
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    st.markdown(f"## {task['emoji']} {task['name']}")
    st.markdown(f"<div class='centered'>What would you like to do?</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"✅ Do it manually"):
            st.session_state.total_actions += 1
    with col2:
        if st.button(f"🤖 Let's automate this"):
            st.session_state.robots.append(task)
            st.session_state.robot_anim[task['name']] = 0
            st.session_state.robot_counts[task['name']] = 0
            st.session_state.level += 1

# Robots working
if len(st.session_state.robots) > 0:
    st.markdown("### 🤖 Automated tasks in progress:")
    for task in st.session_state.robots:
        container = st.empty()
        frame = st.session_state.robot_anim[task['name']]
        icons = [task['emoji']] * 10
        icons[frame % 10] = "✅"
        display = " ".join(icons)

        st.session_state.robot_counts[task['name']] += 1
        st.session_state.total_actions += 1

        container.markdown(
            f"<div class='task-box'>{task['icon']} {task['name']} → {display}<br><small>The robot has done this {st.session_state.robot_counts[task['name']]} times</small></div>",
            unsafe_allow_html=True
        )
        st.session_state.robot_anim[task['name']] = (frame + 1) % 10

# Ending
if st.session_state.level >= len(activities):
    st.markdown("## Everything you do, a robot can do better.")
    st.markdown("You no longer need to work, learn, talk, feel… or even love.")
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

st.markdown("---")
st.markdown("📸 **If this made you think — share it.** Screenshot your screen. Tag [#BetterThanYou] on social media.")
