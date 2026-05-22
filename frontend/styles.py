def load_css():

    return """
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

/* ── ALERTS ── */
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
"""