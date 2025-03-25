import streamlit as st
import time

# Tareas y robots
activities = [
    "Pick apples 🍎",
    "Sweep the floor 🧹",
    "Drive a car 🚗",
    "Write a poem ✍️",
    "Paint a picture 🎨",
    "Diagnose a patient 🩺",
    "Teach a class 👩‍🏫",
    "Compose music 🎼",
    "Write code 💻",
    "Counsel a friend 🧠❤️"
]

robot_emojis = ["🤖", "🦾", "👾", "🤖", "🧠", "🔧", "💻", "📡", "🦿", "🚀"]

if "level" not in st.session_state:
    st.session_state.level = 0
if "count" not in st.session_state:
    st.session_state.count = 0
if "robots" not in st.session_state:
    st.session_state.robots = []
if "animating" not in st.session_state:
    st.session_state.animating = False

st.set_page_config(page_title="Better Than You", layout="centered")
st.title("🤖 Better Than You")

if st.session_state.level < len(activities):
    current_task = activities[st.session_state.level]
    st.subheader(f"Current task: {current_task}")
    st.write(f"You have done it {st.session_state.count}/5 times")

    if st.button(f"Do '{current_task}'"):
        st.session_state.count += 1

    # Mostrar botón para comprar robot
    if st.session_state.count >= 5:
        if st.button("🤖 Buy Robot to do this task"):
            st.session_state.animating = True
            robot = {
                "emoji": robot_emojis[st.session_state.level % len(robot_emojis)],
                "task": current_task
            }
            st.session_state.robots.append(robot)

            # Ejecutar animación si es la primera tarea (recoger manzanas)
            if st.session_state.level == 0:
                st.subheader("🤖 Robot is picking apples...")
                animation_area = st.empty()
                apples = ["🍎"] * 5

                for i in range(5):
                    apples[i] = "✅"
                    animation_area.markdown(
                        f"{robot['emoji']} picking: {' '.join(apples)}"
                    )
                    time.sleep(0.5)

                st.success("Robot has taken over!")
            else:
                st.success(f"Robot now does: '{current_task}'")

            st.session_state.level += 1
            st.session_state.count = 0
            st.session_state.animating = False

    # Mostrar robots activos
    st.markdown("### 🤖 Robots working for you:")
    for robot in st.session_state.robots:
        st.write(f"{robot['emoji']} is doing: *{robot['task']}*")

else:
    st.header("Everything you do, a robot can do better.")
    st.subheader("So… what's the meaning of your existence?")
    
    st.markdown("### 🤖 All your robots:")
    for robot in st.session_state.robots:
        st.write(f"{robot['emoji']} is doing: *{robot['task']}*")

    if st.button("🌟 Find Meaning at Aish.com"):
        st.markdown("[Click here to explore](https://www.aish.com)", unsafe_allow_html=True)
