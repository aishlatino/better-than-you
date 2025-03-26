
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
    text-align: left;
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
    margin: 0.25em 0;
    width: 100%;
    text-align: left;
}
.stButton>button:hover {
    background-color: #80f0ff;
    color: #0d0d0d;
}
.manual-button button {
    background-color: #3333aa;
    border-color: #3333aa;
}
.manual-button button:hover {
    background-color: #6666ff;
}
.automate-button button {
    background-color: #aa3388;
    border-color: #aa3388;
}
.automate-button button:hover {
    background-color: #ff66cc;
}
.task-box {
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid #444;
    padding: 1em;
    margin: 1em 0;
    border-radius: 10px;
}
.count-box {
    background-color: rgba(255,255,255,0.05);
    border: 1px solid #555;
    padding: 0.75em;
    margin: 0.5em 0;
    border-radius: 8px;
    font-size: 0.95em;
}
.total-count {
    color: #ff66ff;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st_autorefresh(interval=100, key="refresh")

activities = [
    {"name": "Work", "emoji": "💼", "icon": "🧠", "transition": "No more meetings or emails — now I can write that book."},
    {"name": "Write a book", "emoji": "📖", "icon": "✍️", "transition": "With writing done, I finally have time to read and reflect."},
    {"name": "Read a book", "emoji": "📚", "icon": "👓", "transition": "Books read, brain fed — now I want to connect with someone."},
    {"name": "Talk to a friend", "emoji": "🗣️", "icon": "🫂", "transition": "Now that I’ve connected, I just want to be present with my family."},
    {"name": "Spend time with your kids", "emoji": "👨‍👧‍👦", "icon": "🧸", "transition": "Even this… replaced."}
]

# Init state
if "level" not in st.session_state:
    st.session_state.level = 0
if "robots" not in st.session_state:
    st.session_state.robots = []
if "robot_anim" not in st.session_state:
    st.session_state.robot_anim = {}
if "robot_counts" not in st.session_state:
    st.session_state.robot_counts = {}
if "manual_counts" not in st.session_state:
    st.session_state.manual_counts = {}
if "transition_text" not in st.session_state:
    st.session_state.transition_text = ""

# Title
st.title("Better Than You")
st.markdown("### Why do it yourself when a robot can do it for you?")

# Current task
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    task_name = task['name']

    if task_name not in st.session_state.robot_counts:
        st.session_state.robot_counts[task_name] = 0
    if task_name not in st.session_state.manual_counts:
        st.session_state.manual_counts[task_name] = 0

    st.markdown(f"**Now we are going to...**")
    st.markdown(f"## {task['emoji']} {task_name}")

    if st.session_state.transition_text:
        st.success(st.session_state.transition_text)

    # Buttons stacked
    if st.button("✅ Do it manually"):
        st.session_state.manual_counts[task_name] += 1

    if st.button("🤖 Let's automate this"):
        st.session_state.robots.append(task)
        st.session_state.robot_anim[task_name] = 0
        st.session_state.transition_text = f"✨ {task['transition']}"
        st.session_state.level += 1

# Show counters for each task
for t in activities:
    name = t["name"]
    if name in st.session_state.manual_counts or name in st.session_state.robot_counts:
        manual = st.session_state.manual_counts.get(name, 0)
        auto = st.session_state.robot_counts.get(name, 0)
        total = manual + auto
        st.markdown(f"<div class='count-box'>{t['emoji']} <strong>{name}</strong>: Written manually: {manual} &nbsp;&nbsp; | &nbsp;&nbsp; By robot: {auto} &nbsp;&nbsp; | &nbsp;&nbsp; <span class='total-count'>Total: {total}</span></div>", unsafe_allow_html=True)

# Robots working
if len(st.session_state.robots) > 0:
    st.markdown("### 🤖 Automated tasks in progress:")
    for task in st.session_state.robots:
        container = st.empty()
        name = task["name"]
        frame = st.session_state.robot_anim[name]
        icons = [task['emoji']] * 10
        icons[frame % 10] = "✅"
        display = " ".join(icons)

        st.session_state.robot_counts[name] += 1

        container.markdown(
            f"<div class='task-box'>{task['icon']} {name} → {display}<br><small>The robot has done this {st.session_state.robot_counts[name]} times</small></div>",
            unsafe_allow_html=True
        )
        st.session_state.robot_anim[name] = (frame + 1) % 10

# Ending
if st.session_state.level >= len(activities):
    st.markdown("## Everything you do, a robot can do better.")
    st.markdown("You no longer need to work, learn, talk, feel… or even love.")
    st.markdown("#### So… what's the point of your existence?")
    st.markdown("""
    <div style='margin-top: 30px;'>
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
