import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://localhost:8000/find_emoji"

# Page config
st.set_page_config(page_title="Emoji Finder", page_icon="🔍")
st.title("🔍 Emoji Finder")
st.markdown("Type your text and get relevant emojis instantly!")

# Custom CSS for larger input and emoji display
st.markdown("""
    <style>
    .big-input input {
        font-size: 20px !important;
        height: 3em !important;
    }
    .big-emoji {
        font-size: 32px;
        line-height: 2em;
    }
    </style>
""", unsafe_allow_html=True)

# Input with custom class
query = st.text_input("Enter text:", key="input", label_visibility="collapsed", placeholder="Type something...", help="", args=None)

# Trigger emoji search live
if query.strip():
    with st.spinner("Finding emojis..."):
        try:
            response = requests.get(API_URL, params={"query": query})
            if response.status_code == 200:
                data = response.json()
                st.markdown(f'<div class="big-emoji">🔎 Results - {data["emojis"]}</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️ API error. Please check the backend.")
        except Exception as e:
            st.error(f"❌ Connection error: {e}")
