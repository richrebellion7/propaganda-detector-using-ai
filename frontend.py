import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = os.getenv("BACKEND_URL")

if not API_URL:
    API_URL = st.secrets["BACKEND_URL"]

st.set_page_config(
    page_title="AI Propaganda Detector",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI Propaganda Detector")

st.markdown("""
Analyze text for:
- Clickbait language
- Emotional manipulation
- Sensational phrasing
""")

example = st.selectbox(
    "Try an example",
    [
        "",

        "BREAKING: The mainstream media is hiding the hidden truth about this crisis. Share this immediately before it's deleted and wake people up!",

        "Scientists from multiple universities published a peer-reviewed climate report discussing rising temperatures and long-term environmental impacts.",

        "SHOCKING revelation exposes secret agenda behind government policies. They don't want you to know how dangerous this situation really is!",

        "Local authorities announced new healthcare initiatives aimed at improving rural hospital access and reducing emergency response times.",

        "ACT NOW before it's too late! This unbelievable report reveals how controlled narratives manipulate public opinion every single day.",

        "Researchers presented new findings on artificial intelligence regulation during an international technology and ethics conference this week."
    ]
)

text = st.text_area(
    "Paste text below",
    value=example,
    height=200
)

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        with st.spinner("Analyzing text..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"text": text},
                    timeout=60
                )

                if response.status_code != 200:
                    st.error("Backend returned an error.")
                    st.stop()
                data = response.json()

                if "error" in data:
                    st.error(data["error"])

                else:

                    score = data["manipulation_score"]
                    severity = data["severity"]

                    st.subheader("📊 Analysis Result")
    
                    if score >= 70:
                        st.error(f"Manipulation Score: {score}%")

                    elif score >= 40:
                        st.warning(f"Manipulation Score: {score}%")

                    else:
                        st.success(f"Manipulation Score: {score}%")

                    if severity == "HIGH":
                        st.error(f"⚠️ Severity Level: {severity}")

                    elif severity == "MEDIUM":
                        st.warning(f"⚠️ Severity Level: {severity}")

                    else:
                        st.success(f"⚠️ Severity Level: {severity}")

                    st.subheader("🚩 Flags")

                    if data["flags"]:
                        for flag in data["flags"]:
                            st.write(f"- {flag}")
                    else:
                        st.write("No major manipulation indicators detected.")

                    st.subheader("🧠 Sentiment")

                    st.json(data["sentiment"])

            except Exception as e:

                st.error(f"Request failed: {e}")

st.markdown("---")
st.caption("Built using FastAPI, Streamlit, and HuggingFace Transformers")