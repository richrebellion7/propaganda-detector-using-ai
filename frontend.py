import streamlit as st
import requests

st.set_page_config(
    page_title="Propaganda Detector",
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

text = st.text_area(
    "Paste text below",
    height=200
)

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        try:

            response = requests.post(
                "https://propaganda-detector-using-ai-1.onrender.com/analyze",
                json={"text": text},
                timeout=60
            )

            st.write("Status Code:", response.status_code)

            data = response.json()

            if "error" in data:
                st.error(data["error"])

            else:

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

        except Exception as e:
            st.error(f"Request failed: {e}")