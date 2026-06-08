import streamlit as st

def render_input_section():
    st.markdown("<div style='margin-bottom:0.6rem;font-weight:700;'>Input</div>", unsafe_allow_html=True)
    text = st.text_area("Enter text to analyze", height=260, placeholder="Paste text here or upload an image...")
    uploaded_image = st.file_uploader("Upload image (optional)", type=["png", "jpg", "jpeg"])
    analyze_button = st.button("Analyze")
    return text, analyze_button, uploaded_image