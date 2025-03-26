
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Better Than You", layout="wide")

# Inject Orbitron font and custom animation
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
<style>
body {
    background-color: #0d0d0d;
    color: #e0e0ff;
    font-family: 'Orbitron', sans-serif;
}
h1, h2, h3 {
    text-align: left;
    color: #ff66ff;
    font-family: 'Orbitron', sans-serif;
}
@keyframes pulse-glow {
  0% { opacity: 0.1; text-shadow: none; }
  50% { opacity: 1; text-shadow: 0 0 10px #ff66ff, 0 0 20px #ff66ff; }
  100% { opacity: 0.1; text-shadow: none; }
}
.terminal-intro {
    font-size: 1.8em;
    margin-top: 1em;
    animation: pulse-glow 2.5s infinite;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

st_autorefresh(interval=100, key="refresh")

# Animated intro text
with st.container():
    st.markdown("<div class='terminal-intro'>Everything you do… a robot will soon do better.</div>", unsafe_allow_html=True)

# Continue with normal app (minimal placeholder for now)
st.title("Better Than You")
st.markdown("### Why do it yourself when a robot can do it for you?")

# Placeholder for demo
st.markdown("This version focuses on Black Mirror-inspired animated intro and typography.")

st.markdown("---")
st.markdown("📸 **If this made you think — share it.** Screenshot your screen. Tag [#BetterThanYou] on social media.")
