
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Better Than You", layout="wide")

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
    border-radius: 8px;
    font-size: 1em;
    transition: 0.3s ease;
    margin-bottom: 0.5em;
    width: 300px;
    display: block;
}
.stButton.manual button {
    background-color: #3344aa;
    color: white;
    border: 1px solid #3344aa;
}
.stButton.manual button:hover {
    background-color: #5566ff;
    color: black;
}
.stButton.automate button {
    background-color: #aa3388;
    color: white;
    border: 1px solid #aa3388;
}
.stButton.automate button:hover {
    background-color: #ff66cc;
    color: black;
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
    {"name": "Work", "emoji": "💼", "icon": "🧠", "transition": "No more meetings or emails — now I can write that book.", "labels": ("Done manually", "Automated", "Total"), "cta": "Let's work"},
    {"name": "Write a book", "emoji": "📖", "icon": "✍️", "transition": "With writing done, I finally have time to read and reflect.", "labels": ("Written manually", "Written by robot", "Total"), "cta": "Let's write"},
    {"name": "Read a book", "emoji": "📚", "icon": "👓", "transition": "Books read, brain fed — now I want to connect with someone.", "labels": ("Read by myself", "Read by robot", "Total"), "cta": "Let's read"},
    {"name": "Talk to a friend", "emoji": "🗣️", "icon": "🫂", "transition": "Now that I’ve connected, I just want to be present with my family.", "labels": ("Talked in person", "Talked by robot", "Total"), "cta": "Let's talk"},
    {"name": "Spend time with your kids", "emoji": "👨‍👧‍👦", "icon": "🧸", "transition": "Even this… replaced.", "labels": ("Spent in person", "Done by robot", "Total"), "cta": "Let's be with them"}
]

# State init
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
if "pending_transition" not in st.session_state:
    st.session_state.pending_transition = ""
if "manual_feedback" not in st.session_state:
    st.session_state.manual_feedback = {}

# Title
st.title("Better Than You")
st.markdown("### Why do it yourself when a robot can do it for you?")

# Counters
for task in activities:
    name = task["name"]
    st.session_state.manual_counts.setdefault(name, 0)
    st.session_state.robot_counts.setdefault(name, 0)

    manual = st.session_state.manual_counts[name]
    auto = st.session_state.robot_counts[name]
    total = manual + auto
    labels = task["labels"]

    robot_display = ""
    if name in st.session_state.robots:
        st.session_state.robot_anim.setdefault(name, 0)
        frame = st.session_state.robot_anim[name]
        icons = [task["emoji"]] * 10
        icons[frame % 10] = "✅"
        robot_display = f"<br>{' '.join(icons)}"
        st.session_state.robot_anim[name] = (frame + 1) % 10
        st.session_state.robot_counts[name] += 1

    if manual > 0 or auto > 0 or name in st.session_state.robots:
        st.markdown(
            f"<div class='count-box'>{task['emoji']} <strong>{name}</strong>: "
            f"{labels[0]}: {manual} &nbsp;&nbsp; | &nbsp;&nbsp; "
            f"{labels[1]}: {auto} &nbsp;&nbsp; | &nbsp;&nbsp; "
            f"<span class='total-count'>{labels[2]}: {total}</span>{robot_display}</div>",
            unsafe_allow_html=True
        )

# Transition message
if st.session_state.pending_transition:
    st.success(st.session_state.pending_transition)

# Task logic
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    name = task["name"]

    st.markdown(f"## {task['emoji']} {task['cta']}")

    manual_clicked = st.button("✅ Do it manually", key=f"manual_{name}")
    auto_clicked = st.button("🤖 Let's automate this", key=f"auto_{name}")

    red_shades = ["#ffcccc", "#ff9999", "#ff6666", "#ff3333", "#ff0000"]
    feedback_msgs = [
        f"Nice! You just completed: {name}.",
        f"Great job doing '{name}' again.",
        f"You seem to like doing '{name}' by hand...",
        f"Still going manually? Robots could help.",
        f"Maybe it’s time to automate '{name}'?"
    ]

    if manual_clicked:
        st.session_state.manual_counts[name] += 1
        st.session_state.pending_transition = ""
        count = st.session_state.manual_counts[name]
        shade = red_shades[min(count - 1, len(red_shades)-1)]
        msg = feedback_msgs[min(count - 1, len(feedback_msgs)-1)]
        st.markdown(f"<div style='background-color:{shade}; padding: 1em; border-radius:8px;'>{msg}</div>", unsafe_allow_html=True)

    if auto_clicked:
        if name not in st.session_state.robots:
            st.session_state.robots.append(name)
        st.session_state.robot_anim[name] = 0
        transition = f"✨ {task['transition']}"
        st.session_state.transition_text[name] = transition
        st.session_state.pending_transition = transition
        st.session_state.level += 1

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
