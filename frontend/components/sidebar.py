import streamlit as st
from components.footer import render_footer

def render_sidebar():

    with st.sidebar:

        st.markdown("""
        <div style="padding: 0.5rem 0 1rem;">
            <div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;
                        color:#e8ecf8;margin-bottom:0.25rem;">🧠 PropagandaAI</div>
            <div style="font-size:0.75rem;color:#4a5478;letter-spacing:0.08em;
                        text-transform:uppercase;">Detection System</div>
        </div>
        <hr style="border-color:rgba(99,120,200,0.18);margin:0 0 1.25rem 0;">
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="font-size:0.82rem;color:#8b97c6;line-height:1.75;margin-bottom:1.5rem;">
            An AI-powered system that analyzes text for propaganda patterns,
            emotional manipulation, and disinformation signals in real time.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="font-family:'Syne',sans-serif;font-size:0.7rem;font-weight:700;
                    letter-spacing:0.12em;text-transform:uppercase;color:#4a5478;
                    margin-bottom:0.75rem;">Tech Stack</div>
        """, unsafe_allow_html=True)

        for tech, desc in [
            ("🤖 Transformers", "HuggingFace sentiment"),
            ("⚡ FastAPI", "Backend inference API"),
            ("🎈 Streamlit", "Interactive frontend"),
            ("🐍 Python 3.11", "Core runtime"),
        ]:

            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;padding:0.55rem 0.75rem;
                        background:rgba(17,28,53,0.8);border:1px solid rgba(99,120,200,0.12);
                        border-radius:10px;margin-bottom:0.5rem;">
                <span style="font-size:0.88rem;">{tech.split()[0]}</span>
                <div>
                    <div style="font-size:0.82rem;color:#c8d0ee;font-weight:500;">
                        {" ".join(tech.split()[1:])}</div>
                    <div style="font-size:0.72rem;color:#4a5478;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        render_footer()
