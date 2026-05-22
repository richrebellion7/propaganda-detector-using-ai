import streamlit as st
import requests
from dotenv import load_dotenv
import os
from components.expander_section import render_expander_section
from styles import load_css
from components.sidebar import render_sidebar
from components.header import render_header
from components.input_section import render_input_section
from components.results_section import render_results_section

load_dotenv()
API_URL = os.getenv("BACKEND_URL")
if not API_URL:
    try:
        API_URL = st.secrets["BACKEND_URL"]
    except Exception:
        API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="AI Propaganda Detector", page_icon="🧠", layout="wide")

st.markdown(load_css(), unsafe_allow_html=True)

render_sidebar()

render_header()

col1, spacer, col2 = st.columns([1, 0.06, 1])

with col1:
    text, analyze_button, uploaded_image = render_input_section()

with col2:
    
    render_results_section(
        analyze_button=analyze_button,
        text=text,
        API_URL=API_URL,
        uploaded_image=uploaded_image
    )

render_expander_section()