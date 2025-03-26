
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Better Than You", layout="wide")

# Combine Black Mirror-style visual design with v15 logic
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
body {
    background: linear-gradient(145deg, #0f1115, #1a1d22);
    color: #e3e3ff;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3 {
    font-family: 'Orbitron', sans-serif;
    color: #9d4edd;
    text-shadow: 0 0 6px #9d4edd55;
}
.stButton>button {
    border-radius: 10px;
    padding: 0.6em 1.4em;
    font-size: 1.05em;
    margin-bottom: 0.75em;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    width: 320px;
}
.stButton.manual button {
    border: 2px solid #6370a0;
    background: linear-gradient(145deg, #393c50, #4a4e68);
    color: #cdd6f4;
}
.stButton.manual button:hover {
    background: #6370a0;
    color: white;
}
.stButton.automate button {
    border: 2px solid #a855f7;
    background: linear-gradient(145deg, #5a2a82, #752a8d);
    color: #f4eaff;
}
.stButton.automate button:hover {
    background: #a855f7;
    color: black;
}
.count-box {
    background-color: rgba(255,255,255,0.03);
    border: 1px solid #444;
    padding: 1em;
    margin: 1em 0;
    border-radius: 10px;
    font-size: 0.95em;
    box-shadow: 0 0 10px #11111188;
}
.total-count {
    color: #a855f7;
    font-weight: bold;
}
.cta-button {
    color: #ffffff !important;
    display: inline-block;
    background-color: #4400ff;
    color: white;
    padding: 1.2em 2em;
    font-size: 1.4em;
    border-radius: 12px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0 0 20px #4400ff;
    transition: all 0.3s ease;
}
.cta-button:hover {
    background-color: #6c00ff;
    box-shadow: 0 0 30px #6c00ff;
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=100, key="refresh")

activities = [
    {
        "name": "Go to work", "emoji": "🏢", "icon": "💼",
        "transition": "Work? Delegated. I can now focus on meaningful creativity.",
        "labels": ("Worked manually", "Done by robot", "Total"),
        "cta": "Let's go to work"
    },
    {
        "name": "Write a book", "emoji": "📖", "icon": "✍️",
        "transition": "With writing off my plate, it's time to absorb wisdom.",
        "labels": ("Written manually", "Written by robot", "Total"),
        "cta": "Let's write a book"
    },
    {
        "name": "Read a book", "emoji": "📚", "icon": "📘",
        "transition": "Learning complete. Let’s connect with someone real.",
        "labels": ("Read manually", "Read by robot", "Total"),
        "cta": "Let's read a book"
    },
    {
        "name": "Talk with a friend", "emoji": "🗣️", "icon": "🫂",
        "transition": "Even connection can be simulated. At least I have my family... right?",
        "labels": ("Talked in person", "Simulated by robot", "Total"),
        "cta": "Let's talk with a friend"
    },
    {
        "name": "Spend time with your kids", "emoji": "👨‍👧‍👦", "icon": "🧸",
        "transition": "Even this… replaced. What’s left that truly needs *you*?",
        "labels": ("Spent in person", "Done by robot", "Total"),
        "cta": "Let's spend time with my kids"
    }
]

red_feedbacks = {
    "Go to work": [
        "🏢 Nice hustle! Another day at the office.",
        "💼 Still clocking in manually, huh?",
        "⏱️ Work-life balance? Robots don’t sleep.",
        "🧮 Time is money. Robots work for free.",
        "🤖 It's probably time to automate this."
    ],
    "Write a book": [
        "✍️ Beautiful! You wrote your first page.",
        "📖 Another chapter done!",
        "⌨️ Still writing by hand? You sure?",
        "🧠 Typing again? Robots write faster.",
        "🤖 Maybe it's time to automate this."
    ],
    "Read a book": [
        "📚 Great! A new book opened.",
        "📖 Deep thoughts, again?",
        "📄 Let an AI summarize it?",
        "🌀 You read that already, remember?",
        "🤖 Maybe it's time to automate this."
    ],
    "Talk with a friend": [
        "🗣️ Nice talk! That felt good.",
        "👂 Still doing it in person?",
        "😅 Same story again, huh?",
        "💬 A chatbot could listen too.",
        "🤖 Maybe it's time to automate this."
    ],
    "Spend time with your kids": [
        "🧸 A precious moment with your child — nothing else matters.",
        "🤗 Another memory made… but how many more can you afford to make?",
        "🧠 You're here now… but what if you could give them more by doing less?",
        "👀 You keep showing up, but could someone else do it better?",
        "🤖 Even parenting can be optimized now... maybe it’s time to automate?"
    ]
}

for k in ["level", "robots", "robot_anim", "robot_counts", "manual_counts", "transition_text", "manual_clicked"]:
    if k not in st.session_state:
        st.session_state[k] = {} if "counts" in k or "anim" in k or "text" in k or "clicked" in k else 0 if k == "level" else []

if "pending_transition" not in st.session_state:
    st.session_state.pending_transition = ""
if "pending_manual_feedback" not in st.session_state:
    st.session_state.pending_manual_feedback = ""
if "pending_manual_color" not in st.session_state:
    st.session_state.pending_manual_color = "#ffcccc"

st.title("Better Than You")
st.markdown("### Why do it yourself when a robot can do it for you?")

# Display counters (hide first task until interaction)
for i, task in enumerate(activities):
    name = task["name"]
    st.session_state.manual_counts.setdefault(name, 0)
    st.session_state.robot_counts.setdefault(name, 0)
    if i < st.session_state.level or (i == st.session_state.level and (i > 0 or st.session_state.manual_counts.get(name, 0) > 0)):
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
        st.markdown(
            f"<div class='count-box'>{task['emoji']} <strong>{task['cta']}</strong>: "
            f"{labels[0]}: {manual} &nbsp;&nbsp; | &nbsp;&nbsp; "
            f"{labels[1]}: {auto} &nbsp;&nbsp; | &nbsp;&nbsp; "
            f"<span class='total-count'>{labels[2]}: {total}</span>{robot_display}</div>",
            unsafe_allow_html=True
        )

# Show current task
if st.session_state.level < len(activities):
    task = activities[st.session_state.level]
    name = task["name"]
    st.markdown(f"## {task['emoji']} {task['cta']}")

    if st.session_state.pending_manual_feedback:
        st.markdown(
            f"<div style='background-color:{st.session_state.pending_manual_color}; padding: 1.2em; border-radius:8px; margin-bottom:1em;'>{st.session_state.pending_manual_feedback}</div>",
            unsafe_allow_html=True
        )
    elif st.session_state.pending_transition:
        st.success(st.session_state.pending_transition)

    already_clicked = st.session_state.manual_clicked.get(name, False)
    manual_label = "✅ Do it manually again..." if already_clicked else "✅ Do it manually"
    manual_clicked = st.button(manual_label, key=f"manual_{name}")
    auto_clicked = st.button("🤖 Let's automate this", key=f"auto_{name}")

    if manual_clicked:
        st.session_state.manual_counts[name] += 1
        st.session_state.manual_clicked[name] = True
        count = st.session_state.manual_counts[name]
        msg_list = red_feedbacks.get(name, ["Well done!"])
        msg = msg_list[min(count - 1, len(msg_list) - 1)] if count <= len(msg_list) else msg_list[-1]
        shade_val = max(0, 204 - int(count * 2))
        hex_val = f"{shade_val:02x}"
        color = f"#ff{hex_val}{hex_val}"
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

# Ending
if st.session_state.level >= len(activities):
    st.markdown("## Everything you do, a robot can do better.")
    st.markdown("You no longer need to work, write, read, connect… or even spend time with your loved ones.")
    st.markdown("#### So… what's the point of your existence?")
    st.markdown("""
    <div style='margin-top: 30px;'>
        <a href='https://aish.com/humans-vs-ai-will-we-remain-relevant/' target='_blank' class='cta-button'>🌌 Discover what makes you human</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("📸 **If this made you think — share it.** Screenshot your screen. Tag [#BetterThanYou] on social media.")
