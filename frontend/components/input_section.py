import streamlit as st

def render_input_section():

    st.markdown("""
    <div style="
        margin-bottom:1rem;
        font-family:'Syne',sans-serif;
        font-size:0.7rem;
        font-weight:700;
        letter-spacing:0.12em;
        text-transform:uppercase;
        color:#4a5478;
    ">
        Input Text
    </div>
    """, unsafe_allow_html=True)

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
        height=340,
        placeholder="Paste an article, tweet, headline, or narrative here..."
    )

    uploaded_image = st.file_uploader(
        "Upload screenshot or image",
        type=["png", "jpg", "jpeg"]
    )

    analyze_button = st.button(
        "🚀 Analyze Text",
        use_container_width=True
    )

    detect_card_html = """
    <div style="
        margin-top:1.5rem;
        background:rgba(17,28,53,0.75);
        border:1px solid rgba(99,120,200,0.12);
        border-radius:16px;
        padding:1rem 1.2rem;
    ">
        <div style="
            font-family:'Syne',sans-serif;
            font-size:0.72rem;
            font-weight:700;
            letter-spacing:0.12em;
            text-transform:uppercase;
            color:#4a5478;
            margin-bottom:0.75rem;
        ">
            What We Detect
        </div>

        <div style="
            display:flex;
            flex-wrap:wrap;
            gap:0.5rem;
        ">

            <span style="background:rgba(242,61,94,0.12); color:#f23d5e; padding:0.4rem 0.7rem; border-radius:999px; font-size:0.76rem; border:1px solid rgba(242,61,94,0.2);">
                Emotional Manipulation
            </span>

            <span style="background:rgba(245,166,35,0.12); color:#f5a623; padding:0.4rem 0.7rem; border-radius:999px; font-size:0.76rem; border:1px solid rgba(245,166,35,0.2);">
                Clickbait Language
            </span>

            <span style="background:rgba(98,114,228,0.12); color:#6272e4; padding:0.4rem 0.7rem; border-radius:999px; font-size:0.76rem; border:1px solid rgba(98,114,228,0.2);">
                Conspiracy Framing
            </span>

            <span style="background:rgba(45,214,152,0.12); color:#2dd698; padding:0.4rem 0.7rem; border-radius:999px; font-size:0.76rem; border:1px solid rgba(45,214,152,0.2);">
                Urgency Tactics
            </span>

        </div>
    </div>
    """

    st.markdown(detect_card_html, unsafe_allow_html=True)

    return text, analyze_button, uploaded_image