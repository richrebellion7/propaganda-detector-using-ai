import streamlit as st
import requests

API_URL = "https://propaganda-detector-using-ai-1.onrender.com/analyze"

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
        "BREAKING shocking truth they don't want you to know!",
        "Scientists publish new climate report.",
        "The mainstream media is hiding this unbelievable secret."
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

                data = response.json()

                if "error" in data:
                    st.error(data["error"])

                else:

                    score = data["manipulation_score"]

                    st.subheader("📊 Analysis Result")

                    if score >= 70:
                        st.error(f"Manipulation Score: {score}%")

                    elif score >= 40:
                        st.warning(f"Manipulation Score: {score}%")

                    else:
                        st.success(f"Manipulation Score: {score}%")

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