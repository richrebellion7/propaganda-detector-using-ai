import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = os.getenv("BACKEND_URL")
if not API_URL:
    try:
        API_URL = st.secrets["BACKEND_URL"]
    except Exception:
        API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="AI Propaganda Detector", page_icon="🧠", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

:root {
    --bg-base:       #070d1a;
    --bg-surface:    #0d1629;
    --bg-card:       #111c35;
    --bg-glass:      rgba(17, 28, 53, 0.75);
    --border:        rgba(99, 120, 200, 0.18);
    --border-glow:   rgba(99, 120, 200, 0.45);
    --accent:        #6272e4;
    --accent-soft:   rgba(98, 114, 228, 0.15);
    --accent-glow:   rgba(98, 114, 228, 0.35);
    --text-primary:  #e8ecf8;
    --text-secondary:#8b97c6;
    --text-muted:    #4a5478;
    --red-vivid:     #f23d5e;
    --red-soft:      rgba(242, 61, 94, 0.12);
    --red-glow:      rgba(242, 61, 94, 0.3);
    --amber-vivid:   #f5a623;
    --amber-soft:    rgba(245, 166, 35, 0.12);
    --amber-glow:    rgba(245, 166, 35, 0.3);
    --green-vivid:   #2dd698;
    --green-soft:    rgba(45, 214, 152, 0.12);
    --green-glow:    rgba(45, 214, 152, 0.3);
    --radius:        16px;
    --radius-sm:     10px;
    --radius-pill:   999px;
}

/* ── GLOBAL RESET ── */
html, body, [class*="css"], .stApp {
    background-color: var(--bg-base) !important;
    font-family: 'DM Sans', sans-serif !important;
    color: var(--text-primary) !important;
}

/* Subtle grid background */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(98,114,228,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(98,114,228,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    z-index: 0;
}

/* ── MAIN CONTENT AREA ── */
.main .block-container {
    background: transparent !important;
    padding: 2rem 2.5rem 3rem !important;
    max-width: 1280px !important;
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: var(--bg-surface) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * {
    color: var(--text-secondary) !important;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: var(--text-primary) !important;
    font-family: 'Syne', sans-serif !important;
}
section[data-testid="stSidebar"] .stCaption {
    color: var(--text-muted) !important;
    font-size: 0.75rem !important;
}

/* ── HEADINGS ── */
h1, h2, h3, h4 {
    font-family: 'Syne', sans-serif !important;
    color: var(--text-primary) !important;
}

/* ── SUBHEADER ── */
[data-testid="stMarkdownContainer"] h3 {
    font-size: 0.7rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: var(--text-muted) !important;
    margin-bottom: 0.75rem !important;
}

/* ── SELECT / DROPDOWN ── */
[data-baseweb="select"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
}
[data-baseweb="select"] * {
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="list"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: 0 16px 48px rgba(0,0,0,0.6) !important;
}
[role="option"] {
    background: var(--bg-card) !important;
    color: var(--text-secondary) !important;
}
[role="option"]:hover {
    background: var(--accent-soft) !important;
    color: var(--text-primary) !important;
}

/* ── TEXT AREA ── */
textarea {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-primary) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    line-height: 1.65 !important;
    resize: none !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
textarea:focus {
    border-color: var(--border-glow) !important;
    box-shadow: 0 0 0 3px var(--accent-glow) !important;
    outline: none !important;
}
textarea::placeholder {
    color: var(--text-muted) !important;
}

/* ── LABEL ── */
label, .stSelectbox label, .stTextArea label {
    color: var(--text-secondary) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.03em !important;
    margin-bottom: 4px !important;
}

/* ── BUTTON ── */
.stButton > button {
    width: 100% !important;
    padding: 0.8rem 1.5rem !important;
    background: linear-gradient(135deg, #5463d4 0%, #8247e5 100%) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: #fff !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(84,99,212,0.4) !important;
    position: relative !important;
    overflow: hidden !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(84,99,212,0.6) !important;
    background: linear-gradient(135deg, #6272e4 0%, #9456f0 100%) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── SPINNER ── */
.stSpinner > div {
    border-top-color: var(--accent) !important;
}

/* ── EXPANDER ── */
[data-testid="stExpander"] {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    margin-top: 1.5rem !important;
}
[data-testid="stExpander"] summary {
    color: var(--text-secondary) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
}
[data-testid="stExpander"] p {
    color: var(--text-secondary) !important;
    font-size: 0.88rem !important;
    line-height: 1.7 !important;
}

/* ── ALERTS (warning/error/success) ── */
.stAlert {
    border-radius: var(--radius-sm) !important;
    border: none !important;
    background: var(--bg-card) !important;
}

/* ── TOOLTIP ── */
[data-baseweb="tooltip"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
}

/* ── DIVIDER ── */
hr {
    border-color: var(--border) !important;
    margin: 1.25rem 0 !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--border-glow); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
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

    st.markdown("""
    <div style="margin-top:2rem;font-size:0.72rem;color:#4a5478;line-height:1.6;">
        Built by <span style="color:#6272e4;font-weight:600;">Mohammed Tazeem Wajahat</span>
    </div>
    """, unsafe_allow_html=True)

# ── HEADER ─────────────────────────────────────────────────────────────────────
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

# ── COLUMNS ────────────────────────────────────────────────────────────────────
col1, spacer, col2 = st.columns([1, 0.06, 1])

with col1:
    st.markdown("""
    <div style="font-family:'Syne',sans-serif;font-size:0.68rem;font-weight:700;
                letter-spacing:0.14em;text-transform:uppercase;color:#4a5478;
                margin-bottom:0.6rem;">Input Text</div>
    """, unsafe_allow_html=True)

    example = st.selectbox(
        "Try an example",
        options=[
            "",
            "BREAKING: The mainstream media is hiding the hidden truth about this secret agenda!",
            "Scientists from multiple universities published a peer-reviewed study confirming the results.",
            "SHOCKING revelation exposes secret agenda behind government water fluoridation program.",
            "This ONE WEIRD TRICK the elites don't want you to know about will change your life FOREVER!",
        ],
        format_func=lambda x: "— Select an example —" if x == "" else (x[:72] + "…" if len(x) > 72 else x),
    )

    text = st.text_area(
        "Paste text to analyze",
        value=example,
        height=300,
        placeholder="Paste any article, headline, social-media post, or speech excerpt…",
    )

    analyze_button = st.button("🚀  Analyze Text", use_container_width=True)

    st.markdown("""
    <div style="margin-top:1rem;padding:0.85rem 1rem;
                background:rgba(98,114,228,0.07);
                border:1px solid rgba(98,114,228,0.15);
                border-radius:10px;">
        <div style="font-size:0.75rem;color:#6272e4;font-weight:600;
                    margin-bottom:0.3rem;">ℹ️ What we detect</div>
        <div style="font-size:0.78rem;color:#8b97c6;line-height:1.65;">
            Clickbait language · Fear-mongering · False urgency ·
            Loaded vocabulary · Conspiracy framing · Emotional amplifiers
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="font-family:'Syne',sans-serif;font-size:0.68rem;font-weight:700;
                letter-spacing:0.14em;text-transform:uppercase;color:#4a5478;
                margin-bottom:0.6rem;">Analysis Results</div>
    """, unsafe_allow_html=True)

    if not analyze_button:
        st.markdown("""
        <div style="height:420px;display:flex;flex-direction:column;align-items:center;
                    justify-content:center;background:rgba(13,22,41,0.6);
                    border:1px dashed rgba(99,120,200,0.2);border-radius:16px;
                    text-align:center;gap:0.75rem;">
            <div style="font-size:2.5rem;opacity:0.25;">🔍</div>
            <div style="font-size:0.9rem;color:#4a5478;font-weight:500;">
                Results will appear here
            </div>
            <div style="font-size:0.78rem;color:#2e3a5c;max-width:220px;line-height:1.6;">
                Enter some text and hit Analyze to get a full propaganda breakdown.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if text.strip() == "":
            st.markdown("""
            <div style="padding:1rem 1.2rem;background:rgba(245,166,35,0.1);
                        border:1px solid rgba(245,166,35,0.25);border-radius:12px;
                        color:#f5a623;font-size:0.88rem;">
                ⚠️  Please enter some text before analyzing.
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Analyzing propaganda patterns…"):
                try:
                    response = requests.post(API_URL, json={"text": text}, timeout=60)
                    if response.status_code != 200:
                        st.markdown(f"""
                        <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);
                                    border:1px solid rgba(242,61,94,0.3);border-radius:12px;
                                    color:#f23d5e;font-size:0.88rem;">
                            ❌  Backend error — HTTP {response.status_code}
                        </div>""", unsafe_allow_html=True)
                        st.stop()

                    data = response.json()

                    if "error" in data:
                        st.markdown(f"""
                        <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);
                                    border:1px solid rgba(242,61,94,0.3);border-radius:12px;
                                    color:#f23d5e;font-size:0.88rem;">
                            ❌  {data['error']}
                        </div>""", unsafe_allow_html=True)
                    else:
                        score    = data["manipulation_score"]        # 0–100
                        severity = data["severity"]                  # HIGH / MEDIUM / LOW
                        flags    = data.get("flags", [])
                        sent     = data["sentiment"]
                        s_label  = sent["label"]                     # POSITIVE / NEGATIVE / NEUTRAL
                        s_score  = round(sent["score"] * 100, 1)

                        # Severity palette
                        if severity == "HIGH":
                            sev_color  = "#f23d5e"
                            sev_soft   = "rgba(242,61,94,0.10)"
                            sev_glow   = "rgba(242,61,94,0.30)"
                            sev_icon   = "🔴"
                            bar_grad   = "linear-gradient(90deg,#f23d5e,#c0163a)"
                        elif severity == "MEDIUM":
                            sev_color  = "#f5a623"
                            sev_soft   = "rgba(245,166,35,0.10)"
                            sev_glow   = "rgba(245,166,35,0.30)"
                            sev_icon   = "🟡"
                            bar_grad   = "linear-gradient(90deg,#f5a623,#c07d10)"
                        else:
                            sev_color  = "#2dd698"
                            sev_soft   = "rgba(45,214,152,0.10)"
                            sev_glow   = "rgba(45,214,152,0.30)"
                            sev_icon   = "🟢"
                            bar_grad   = "linear-gradient(90deg,#2dd698,#19a472)"

                        # Sentiment palette
                        if s_label == "NEGATIVE":
                            sent_color = "#f23d5e"; sent_soft = "rgba(242,61,94,0.10)"
                        elif s_label == "POSITIVE":
                            sent_color = "#2dd698"; sent_soft = "rgba(45,214,152,0.10)"
                        else:
                            sent_color = "#6272e4"; sent_soft = "rgba(98,114,228,0.10)"

                        # ── SCORE CARD ─────────────────────────────────────────
                        st.markdown(f"""
                        <div style="background:{sev_soft};border:1px solid {sev_color}40;
                                    border-radius:16px;padding:1.4rem 1.5rem;margin-bottom:1rem;
                                    box-shadow:0 0 32px {sev_glow};">
                            <div style="display:flex;align-items:center;
                                        justify-content:space-between;margin-bottom:1rem;">
                                <div>
                                    <div style="font-size:0.68rem;font-weight:700;
                                                letter-spacing:0.12em;text-transform:uppercase;
                                                color:{sev_color};margin-bottom:0.3rem;">
                                        Manipulation Score
                                    </div>
                                    <div style="font-family:'Syne',sans-serif;font-size:3rem;
                                                font-weight:800;color:{sev_color};line-height:1;">
                                        {score}<span style="font-size:1.4rem;opacity:0.7;">%</span>
                                    </div>
                                </div>
                                <div style="text-align:right;">
                                    <div style="background:{sev_color}22;border:1px solid {sev_color}55;
                                                border-radius:999px;padding:0.4rem 1rem;
                                                display:inline-block;margin-bottom:0.5rem;">
                                        <span style="font-family:'Syne',sans-serif;font-size:0.78rem;
                                                     font-weight:700;color:{sev_color};">
                                            {sev_icon} {severity} SEVERITY
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div style="height:6px;background:rgba(255,255,255,0.07);
                                        border-radius:999px;overflow:hidden;">
                                <div style="width:{score}%;height:100%;
                                            background:{bar_grad};border-radius:999px;
                                            transition:width 0.8s cubic-bezier(.4,0,.2,1);">
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        # ── SENTIMENT CARD ─────────────────────────────────────
                        st.markdown(f"""
                        <div style="background:rgba(13,22,41,0.8);
                                    border:1px solid rgba(99,120,200,0.18);
                                    border-radius:16px;padding:1.1rem 1.4rem;
                                    margin-bottom:1rem;display:flex;
                                    align-items:center;justify-content:space-between;">
                            <div>
                                <div style="font-size:0.68rem;font-weight:700;
                                            letter-spacing:0.12em;text-transform:uppercase;
                                            color:#4a5478;margin-bottom:0.4rem;">
                                    Sentiment Analysis
                                </div>
                                <div style="font-family:'Syne',sans-serif;font-size:1.35rem;
                                            font-weight:700;color:{sent_color};">
                                    {s_label}
                                </div>
                            </div>
                            <div style="text-align:right;">
                                <div style="font-size:0.72rem;color:#4a5478;
                                            margin-bottom:0.25rem;">Confidence</div>
                                <div style="font-family:'Syne',sans-serif;font-size:1.5rem;
                                            font-weight:800;color:{sent_color};">
                                    {s_score}%
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        # ── DETECTED FLAGS ─────────────────────────────────────
                        st.markdown("""
                        <div style="font-size:0.68rem;font-weight:700;
                                    letter-spacing:0.12em;text-transform:uppercase;
                                    color:#4a5478;margin:0.75rem 0 0.65rem;">
                            Detected Signals
                        </div>
                        """, unsafe_allow_html=True)

                        if flags:
                            # Pill badges — 2-column grid
                            pills_html = '<div style="display:flex;flex-wrap:wrap;gap:0.5rem;">'
                            for flag in flags:
                                pills_html += f"""
                                <div style="background:rgba(242,61,94,0.10);
                                            border:1px solid rgba(242,61,94,0.30);
                                            border-radius:999px;padding:0.35rem 0.9rem;">
                                    <span style="font-size:0.78rem;font-weight:500;
                                                 color:#f23d5e;">⚑ {flag}</span>
                                </div>"""
                            pills_html += "</div>"
                            st.markdown(pills_html, unsafe_allow_html=True)
                        else:
                            st.markdown("""
                            <div style="display:flex;align-items:center;gap:0.75rem;
                                        padding:0.85rem 1.1rem;
                                        background:rgba(45,214,152,0.08);
                                        border:1px solid rgba(45,214,152,0.25);
                                        border-radius:12px;">
                                <span style="font-size:1.2rem;">✅</span>
                                <span style="font-size:0.85rem;color:#2dd698;font-weight:500;">
                                    No manipulation signals detected.
                                </span>
                            </div>
                            """, unsafe_allow_html=True)

                except requests.exceptions.ConnectionError:
                    st.markdown("""
                    <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);
                                border:1px solid rgba(242,61,94,0.3);border-radius:12px;
                                color:#f23d5e;font-size:0.88rem;">
                        ❌  Cannot reach the backend. Is the FastAPI server running?
                    </div>""", unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(f"""
                    <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);
                                border:1px solid rgba(242,61,94,0.3);border-radius:12px;
                                color:#f23d5e;font-size:0.88rem;">
                        ❌  Request failed: {e}
                    </div>""", unsafe_allow_html=True)

# ── EXPANDER ───────────────────────────────────────────────────────────────────
with st.expander("🧠  How does the detector work?"):
    st.markdown("""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;padding-top:0.5rem;">
        <div style="padding:1rem;background:rgba(17,28,53,0.8);
                    border:1px solid rgba(99,120,200,0.15);border-radius:12px;">
            <div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;
                        color:#6272e4;margin-bottom:0.5rem;">🤖 Transformer Model</div>
            <div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">
                A fine-tuned HuggingFace model scores sentiment and detects loaded
                language patterns associated with propaganda.
            </div>
        </div>
        <div style="padding:1rem;background:rgba(17,28,53,0.8);
                    border:1px solid rgba(99,120,200,0.15);border-radius:12px;">
            <div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;
                        color:#6272e4;margin-bottom:0.5rem;">📊 Manipulation Score</div>
            <div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">
                A composite 0–100 score derived from flag density, sentiment polarity,
                urgency markers, and rhetorical amplifiers.
            </div>
        </div>
        <div style="padding:1rem;background:rgba(17,28,53,0.8);
                    border:1px solid rgba(99,120,200,0.15);border-radius:12px;">
            <div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;
                        color:#6272e4;margin-bottom:0.5rem;">⚑ Signal Detection</div>
            <div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">
                Rule-based and learned classifiers identify clickbait language,
                conspiracy framing, false urgency, and fear-mongering patterns.
            </div>
        </div>
        <div style="padding:1rem;background:rgba(17,28,53,0.8);
                    border:1px solid rgba(99,120,200,0.15);border-radius:12px;">
            <div style="font-family:'Syne',sans-serif;font-size:0.82rem;font-weight:700;
                        color:#6272e4;margin-bottom:0.5rem;">⚡ FastAPI Backend</div>
            <div style="font-size:0.8rem;color:#8b97c6;line-height:1.7;">
                All inference runs server-side via a FastAPI endpoint, keeping the
                frontend snappy and model weights off the client.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)