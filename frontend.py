import streamlit as st
import requests

st.set_page_config(
    page_title="Propaganda Detector",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI Propaganda Detector")

st.markdown(
    """
Analyze text for:
- Clickbait language
- Emotional manipulation
- Sensational phrasing
"""
)

text = st.text_area(
    "Paste text below",
    height=200
)

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={"text": text}
        )

        data = response.json()

        st.subheader("📊 Analysis Result")

        st.metric(
            "Manipulation Score",
            f"{data['manipulation_score']}%"
        )

        st.subheader("🚩 Flags")

        if data["flags"]:
            for flag in data["flags"]:
                st.write(f"- {flag}")
        else:
            st.write("No major manipulation indicators detected.")

        st.subheader("🧠 Sentiment")

        st.json(data["sentiment"])