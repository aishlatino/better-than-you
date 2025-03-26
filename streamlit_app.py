
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
    margin-bottom: 0.75em;
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

# Rav Noach Weinberg's 5 levels of pleasure reflected as tasks
activities = [
    {
        "name": "Eat delicious food", "emoji": "🍲", "icon": "🍽️",
        "transition": "No more cooking or eating stress — now I can write and create.",
        "labels": ("Enjoyed manually", "Served by robot", "Total"),
        "cta": "Let's enjoy a good meal"
    },
    {
        "name": "Create something meaningful", "emoji": "📝", "icon": "🎨",
        "transition": "Creative energy? Delegated. Now I can sit back and take in wisdom.",
        "labels": ("Created manually", "Created by robot", "Total"),
        "cta": "Let's write a book"
    },
    {
        "name": "Learn something deep", "emoji": "📘", "icon": "🧠",
        "transition": "No need to read — I have time to connect with someone I care about.",
        "labels": ("Read myself", "Read by robot", "Total"),
        "cta": "Let's read a book"
    },
    {
        "name": "Talk with a friend", "emoji": "🗣️", "icon": "🫂",
        "transition": "Even connection can be simulated. At least I have my family... right?",
        "labels": ("Spoken in person", "Simulated by robot", "Total"),
        "cta": "Let's talk with a friend"
    },
    {
        "name": "Spend time with your kids", "emoji": "👨‍👧‍👦", "icon": "🧸",
        "transition": "Even this… replaced. What’s left that truly needs *you*?",
        "labels": ("Spent in person", "Done by robot", "Total"),
        "cta": "Let's spend time with my kids"
    }
]

# State init
for k in ["level", "robots", "robot_anim", "robot_counts", "manual_counts", "transition_text", "manual_clicked"]:
    if k not in st.session_state:
        st.session_state[k] = {} if "counts" in k or "anim" in k or "text" in k or "clicked" in k else 0 if k == "level" else []

if "pending_transition" not in st.session_state:
    st.session_state.pending_transition = ""
if "pending_manual_feedback" not in st.session_state:
    st.session_state.pending_manual_feedback = ""
if "pending_manual_color" not in st.session_state:
    st.session_state.pending_manual_color = "#ffcccc"

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

# Main flow
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    name = task["name"]

    st.markdown(f"## {task['emoji']} {task['cta']}")

    # Message (manual or automation)
    if st.session_state.pending_manual_feedback:
        st.markdown(
            f"<div style='background-color:{st.session_state.pending_manual_color}; padding: 1.2em; border-radius:8px; margin-bottom:1em;'>{st.session_state.pending_manual_feedback}</div>",
            unsafe_allow_html=True
        )
    elif st.session_state.pending_transition:
        st.success(st.session_state.pending_transition)

    # Buttons
    already_clicked = st.session_state.manual_clicked.get(name, False)
    manual_label = "✅ Do it manually again..." if already_clicked else "✅ Do it manually"
    manual_clicked = st.button(manual_label, key=f"manual_{name}")
    auto_clicked = st.button("🤖 Let's automate this", key=f"auto_{name}")

    # Red messages
    red_shades = ["#ffcccc", "#ff9999", "#ff6666", "#ff3333", "#cc0000"]
    friendly_msgs = [
        f"👏 Amazing! You just enjoyed your first {name.lower()}.",
        f"💪 Well done — another {name.lower()} completed.",
        f"You're getting good at this... still doing it by hand?",
        f"Hmm, still no robot? It's getting repetitive...",
        f"🤖 This could really be automated now, just saying..."
    ]

    if manual_clicked:
        st.session_state.manual_counts[name] += 1
        st.session_state.manual_clicked[name] = True
        count = st.session_state.manual_counts[name]
        msg = friendly_msgs[min(count-1, len(friendly_msgs)-1)]
        color = red_shades[min(count-1, len(red_shades)-1)]
        st.session_state.pending_manual_feedback = msg
        st.session_state.pending_manual_color = color
        st.session_state.pending_transition = ""

    if auto_clicked:
        if name not in st.session_state.robots:
            st.session_state.robots.append(name)
        st.session_state.robot_anim[name] = 0
        st.session_state.transition_text[name] = f"✨ {task['transition']}"
        st.session_state.pending_transition = f"✨ {task['transition']}"
        st.session_state.pending_manual_feedback = ""
        st.session_state.manual_clicked[name] = False
        st.session_state.level += 1

# Final message
if st.session_state.level >= len(activities):
    st.markdown("## Everything you do, a robot can do better.")
    st.markdown("You no longer need to eat, create, learn, connect… or even spend time with your loved ones.")
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
