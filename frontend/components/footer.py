import streamlit as st

def render_footer():
    st.markdown("""
        <div style="margin-top:2rem;font-size:0.72rem;color:#4a5478;line-height:1.6;">
            Built by <span style="color:#6272e4;font-weight:600;">Mohammed Tazeem Wajahat</span>
        </div>
        """, unsafe_allow_html=True)