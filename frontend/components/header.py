import streamlit as st

def render_header():

    st.markdown("""
    <div style="text-align:center;padding:2.5rem 1rem 2rem;">
        <div style="display:inline-block;background:rgba(98,114,228,0.12);
                    border:1px solid rgba(98,114,228,0.25);border-radius:999px;
                    padding:0.35rem 1rem;margin-bottom:1rem;">
            <span style="font-size:0.72rem;font-weight:600;letter-spacing:0.12em;
                         text-transform:uppercase;color:#6272e4;">AI-Powered Analysis</span>
        </div>
        <h1 style="font-family:'Syne',sans-serif;font-size:2.6rem;font-weight:800;
                   background:linear-gradient(135deg,#e8ecf8 30%,#6272e4 100%);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                   background-clip:text;margin:0 0 0.75rem 0;line-height:1.15;">
            Propaganda Detector
        </h1>
        <p style="font-size:1rem;color:#8b97c6;max-width:520px;margin:0 auto;
                  font-weight:300;line-height:1.65;">
            Uncover emotional manipulation, disinformation patterns, and
            rhetorical tactics buried inside any text — instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)