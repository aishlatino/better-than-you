
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
    padding: 0.5em 1em;
    border-radius: 8px;
    font-size: 1em;
    transition: 0.3s ease;
    margin: 0.25em 0.25em 0.25em 0;
    width: auto;
    display: inline-block;
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
    {"name": "Work", "emoji": "💼", "icon": "🧠", "transition": "No more meetings or emails — now I can write that book.", "labels": ("done", "automated", "total")},
    {"name": "Write a book", "emoji": "📖", "icon": "✍️", "transition": "With writing done, I finally have time to read and reflect.", "labels": ("written manually", "written by robot", "total")},
    {"name": "Read a book", "emoji": "📚", "icon": "👓", "transition": "Books read, brain fed — now I want to connect with someone.", "labels": ("read myself", "read by robot", "total")},
    {"name": "Talk to a friend", "emoji": "🗣️", "icon": "🫂", "transition": "Now that I’ve connected, I just want to be present with my family.", "labels": ("talked in person", "talked by robot", "total")},
    {"name": "Spend time with your kids", "emoji": "👨‍👧‍👦", "icon": "🧸", "transition": "Even this… replaced.", "labels": ("spent in person", "done by robot", "total")}
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
    st.session_state.transition_text = {}

# Title
st.title("Better Than You")
st.markdown("### Why do it yourself when a robot can do it for you?")

# Current task flow
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    name = task["name"]

    if name not in st.session_state.manual_counts:
        st.session_state.manual_counts[name] = 0
    if name not in st.session_state.robot_counts:
        st.session_state.robot_counts[name] = 0

    manual = st.session_state.manual_counts.get(name, 0)
    auto = st.session_state.robot_counts.get(name, 0)
    total = manual + auto
    manual_label, auto_label, total_label = task["labels"]

    robot_display = ""
    if name in st.session_state.robots:
        if name not in st.session_state.robot_anim:
            st.session_state.robot_anim[name] = 0
        frame = st.session_state.robot_anim[name]
        icons = [task["emoji"]] * 10
        icons[frame % 10] = "✅"
        robot_display = f"<br>{' '.join(icons)}"
        st.session_state.robot_anim[name] = (frame + 1) % 10
        st.session_state.robot_counts[name] += 1

    st.markdown(
        f"<div class='count-box'>{task['emoji']} <strong>{name}</strong>: "
        f"{manual_label.capitalize()}: {manual} &nbsp;&nbsp; | &nbsp;&nbsp; "
        f"{auto_label.capitalize()}: {auto} &nbsp;&nbsp; | &nbsp;&nbsp; "
        f"<span class='total-count'>{total_label.capitalize()}: {total}</span>{robot_display}</div>",
        unsafe_allow_html=True
    )

    st.markdown(f"**Now we are going to...**")
    st.markdown(f"## {task['emoji']} {name}")

    if name in st.session_state.transition_text:
        st.success(st.session_state.transition_text[name])

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✅ Do it manually"):
            st.session_state.manual_counts[name] += 1
    with col2:
        if st.button("🤖 Let's automate this"):
            st.session_state.robots.append(name)
            st.session_state.robot_anim[name] = 0
            st.session_state.transition_text[name] = f"✨ {task['transition']}"
            st.session_state.level += 1

# Show all completed counters
for task in activities:
    name = task["name"]
    if name != activities[st.session_state.level]["name"] if st.session_state.level < len(activities) else True:
        if name in st.session_state.manual_counts or name in st.session_state.robot_counts:
            manual = st.session_state.manual_counts.get(name, 0)
            auto = st.session_state.robot_counts.get(name, 0)
            total = manual + auto
            manual_label, auto_label, total_label = task["labels"]

            robot_display = ""
            if name in st.session_state.robots:
                frame = st.session_state.robot_anim.get(name, 0)
                icons = [task["emoji"]] * 10
                icons[frame % 10] = "✅"
                robot_display = f"<br>{' '.join(icons)}"
                st.session_state.robot_anim[name] = (frame + 1) % 10
                st.session_state.robot_counts[name] += 1

            st.markdown(
                f"<div class='count-box'>{task['emoji']} <strong>{name}</strong>: "
                f"{manual_label.capitalize()}: {manual} &nbsp;&nbsp; | &nbsp;&nbsp; "
                f"{auto_label.capitalize()}: {auto} &nbsp;&nbsp; | &nbsp;&nbsp; "
                f"<span class='total-count'>{total_label.capitalize()}: {total}</span>{robot_display}</div>",
                unsafe_allow_html=True
            )

# Final message
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
