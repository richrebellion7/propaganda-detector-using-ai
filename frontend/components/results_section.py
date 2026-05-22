import streamlit as st
import requests

def render_results_section(analyze_button, text, API_URL):
    st.markdown("""
    <div style="
        font-family:'Syne',sans-serif;
        font-size:0.68rem;
        font-weight:700;
        letter-spacing:0.14em;
        text-transform:uppercase;
        color:#4a5478;
        margin-bottom:0.6rem;
    ">
        Analysis Results
    </div>
    """, unsafe_allow_html=True)

    if not analyze_button:
        empty_state_html = """
        <div style="height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(13,22,41,0.6);border:1px dashed rgba(99,120,200,0.2);border-radius:16px;text-align:center;gap:0.75rem;">
            <div style="font-size:2.5rem;opacity:0.25;">🔍</div>
            <div style="font-size:0.9rem;color:#4a5478;font-weight:500;">Results will appear here</div>
            <div style="font-size:0.78rem;color:#2e3a5c;max-width:220px;line-height:1.6;">
                Enter some text and hit Analyze to get a full propaganda breakdown.
            </div>
        </div>
        """
        st.markdown(empty_state_html, unsafe_allow_html=True)
        return

    if text.strip() == "":
        st.markdown("""
        <div style="
            padding:1rem 1.2rem;
            background:rgba(245,166,35,0.1);
            border:1px solid rgba(245,166,35,0.25);
            border-radius:12px;
            color:#f5a623;
            font-size:0.88rem;
        ">
            ⚠️ Please enter some text before analyzing.
        </div>
        """, unsafe_allow_html=True)
        return

    with st.spinner("Analyzing propaganda patterns…"):
        try:
            response = requests.post(
                API_URL,
                json={"text": text},
                timeout=60
            )

            if response.status_code != 200:
                st.markdown(f"""
                <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);border:1px solid rgba(242,61,94,0.3);border-radius:12px;color:#f23d5e;font-size:0.88rem;">
                    ❌ Backend error — HTTP {response.status_code}
                </div>""", unsafe_allow_html=True)
                return

            data = response.json()

            if "error" in data:
                st.markdown(f"""
                <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);border:1px solid rgba(242,61,94,0.3);border-radius:12px;color:#f23d5e;font-size:0.88rem;">
                    ❌ {data["error"]}
                </div>""", unsafe_allow_html=True)
                return

            score = data["manipulation_score"]
            severity = data["severity"]
            flags = data.get("flags", [])
            sent = data["sentiment"]
            s_label = sent["label"]
            s_score = round(sent["score"] * 100, 1)

            if severity == "HIGH":
                sev_color = "#f23d5e"
                sev_soft = "rgba(242,61,94,0.10)"
                sev_glow = "rgba(242,61,94,0.30)"
                sev_icon = "🔴"
                bar_grad = "linear-gradient(90deg,#f23d5e,#c0163a)"
            elif severity == "MEDIUM":
                sev_color = "#f5a623"
                sev_soft = "rgba(245,166,35,0.10)"
                sev_glow = "rgba(245,166,35,0.30)"
                sev_icon = "🟡"
                bar_grad = "linear-gradient(90deg,#f5a623,#c07d10)"
            else:
                sev_color = "#2dd698"
                sev_soft = "rgba(45,214,152,0.10)"
                sev_glow = "rgba(45,214,152,0.30)"
                sev_icon = "🟢"
                bar_grad = "linear-gradient(90deg,#2dd698,#19a472)"

            if s_label == "NEGATIVE":
                sent_color = "#f23d5e"
            elif s_label == "POSITIVE":
                sent_color = "#2dd698"
            else:
                sent_color = "#6272e4"

            st.markdown(f"""
            <div style="background:{sev_soft};border:1px solid {sev_color}40;border-radius:16px;padding:1.4rem 1.5rem;margin-bottom:1rem;box-shadow:0 0 32px {sev_glow};">
                <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem;">
                    <div>
                        <div style="font-size:0.68rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:{sev_color};margin-bottom:0.3rem;">Manipulation Score</div>
                        <div style="font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;color:{sev_color};line-height:1;">
                            {score}<span style="font-size:1.4rem;opacity:0.7;">%</span>
                        </div>
                    </div>
                    <div style="text-align:right;">
                        <div style="background:{sev_color}22;border:1px solid {sev_color}55;border-radius:999px;padding:0.4rem 1rem;display:inline-block;margin-bottom:0.5rem;">
                            <span style="font-family:'Syne',sans-serif;font-size:0.78rem;font-weight:700;color:{sev_color};">{sev_icon} {severity} SEVERITY</span>
                        </div>
                    </div>
                </div>
                <div style="height:6px;background:rgba(255,255,255,0.07);border-radius:999px;overflow:hidden;">
                    <div style="width:{score}%;height:100%;background:{bar_grad};border-radius:999px;transition:width 0.8s cubic-bezier(.4,0,.2,1);"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="background:rgba(13,22,41,0.8);border:1px solid rgba(99,120,200,0.18);border-radius:16px;padding:1.1rem 1.4rem;margin-bottom:1rem;display:flex;align-items:center;justify-content:space-between;">
                <div>
                    <div style="font-size:0.68rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#4a5478;margin-bottom:0.4rem;">Sentiment Analysis</div>
                    <div style="font-family:'Syne',sans-serif;font-size:1.35rem;font-weight:700;color:{sent_color};">{s_label}</div>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:0.72rem;color:#4a5478;margin-bottom:0.25rem;">Confidence</div>
                    <div style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;color:{sent_color};">{s_score}%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="font-size:0.68rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#4a5478;margin:0.75rem 0 0.65rem;">
                Detected Signals
            </div>
            """, unsafe_allow_html=True)

            if flags:
                pills_html = '<div style="display:flex;flex-wrap:wrap;gap:0.5rem;">'
                for flag in flags:
                    # 💡 FIX: Keep the HTML on a single, continuous line to prevent text breaking
                    pills_html += f'<div style="background:rgba(242,61,94,0.10);border:1px solid rgba(242,61,94,0.30);border-radius:999px;padding:0.35rem 0.9rem;"><span style="font-size:0.78rem;font-weight:500;color:#f23d5e;">⚑ {flag}</span></div>'
                pills_html += "</div>"
                st.markdown(pills_html, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="display:flex;align-items:center;gap:0.75rem;padding:0.85rem 1.1rem;background:rgba(45,214,152,0.08);border:1px solid rgba(45,214,152,0.25);border-radius:12px;">
                    <span style="font-size:1.2rem;">✅</span>
                    <span style="font-size:0.85rem;color:#2dd698;font-weight:500;">No manipulation signals detected.</span>
                </div>
                """, unsafe_allow_html=True)

        except requests.exceptions.ConnectionError:
            st.markdown("""
            <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);border:1px solid rgba(242,61,94,0.3);border-radius:12px;color:#f23d5e;font-size:0.88rem;">
                ❌ Cannot reach the backend. Is the FastAPI server running?
            </div>""", unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
            <div style="padding:1rem 1.2rem;background:rgba(242,61,94,0.1);border:1px solid rgba(242,61,94,0.3);border-radius:12px;color:#f23d5e;font-size:0.88rem;">
                ❌ Request failed: {e}
            </div>""", unsafe_allow_html=True)