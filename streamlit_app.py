
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Better Than You", layout="wide")

# Visual rework styling: modern, elegant, emotionally engaging
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
}
.stButton.manual button {
    background: linear-gradient(145deg, #393c50, #4a4e68);
    color: #cdd6f4;
}
.stButton.manual button:hover {
    background: #6370a0;
    color: white;
}
.stButton.automate button {
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

# Mini demo content
st_autorefresh(interval=100, key="refresh")

st.title("Better Than You")
st.markdown("### Why do it yourself when a robot can do it for you?")

st.markdown("<div class='count-box'>🍽️ Let's go to work: Worked manually: 3 | Done by robot: 6 | <span class='total-count'>Total: 9</span></div>", unsafe_allow_html=True)

st.markdown("✅ Do it manually", unsafe_allow_html=True)
st.markdown("🤖 Let's automate this", unsafe_allow_html=True)

# Final CTA
st.markdown("## Everything you do, a robot can do better.")
st.markdown("#### So… what's the point of your existence?")
st.markdown("""
<div style='margin-top: 30px;'>
    <a href='https://aish.com/humans-vs-ai-will-we-remain-relevant/' target='_blank' class='cta-button'>🌌 Discover what makes you human</a>
</div>
""", unsafe_allow_html=True)
