import streamlit as st

def render_expander_section():
    with st.expander("🧠  How does the detector work?"):
        bento_html = """
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;padding-top:0.5rem;">
            <div style="padding:1rem;background:rgba(17,28,53,0.8);border:1px solid rgba(99,120,200,0.15);border-radius:12px;"><div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;color:#6272e4;margin-bottom:0.5rem;">🤖 Transformer Model</div><div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">A fine-tuned HuggingFace model scores sentiment and detects loaded language patterns associated with propaganda.</div></div>
            <div style="padding:1rem;background:rgba(17,28,53,0.8);border:1px solid rgba(99,120,200,0.15);border-radius:12px;"><div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;color:#6272e4;margin-bottom:0.5rem;">📊 Manipulation Score</div><div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">A composite 0–100 score derived from flag density, sentiment polarity, urgency markers, and rhetorical amplifiers.</div></div>
            <div style="padding:1rem;background:rgba(17,28,53,0.8);border:1px solid rgba(99,120,200,0.15);border-radius:12px;"><div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;color:#6272e4;margin-bottom:0.5rem;">⚑ Signal Detection</div><div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">Rule-based and learned classifiers identify clickbait language, conspiracy framing, false urgency, and fear-mongering patterns.</div></div>
            <div style="padding:1rem;background:rgba(17,28,53,0.8);border:1px solid rgba(99,120,200,0.15);border-radius:12px;"><div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;color:#6272e4;margin-bottom:0.5rem;">⚡ FastAPI Backend</div><div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">All inference runs server-side via a FastAPI endpoint, keeping the frontend snappy and model weights off the client.</div></div>
        </div>
        """
        st.markdown(bento_html, unsafe_allow_html=True)