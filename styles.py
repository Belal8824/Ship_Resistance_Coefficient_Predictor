"""
styles.py

Shared visual identity for the application: color tokens, typography,
component CSS, and the recurring hull-section divider motif. Importing
`inject_global_styles()` once per page keeps every page visually consistent.
"""

import streamlit as st


# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------

COLOR_PRIMARY_NAVY = "#0B2545"      # primary navy - headers, sidebar, key text
COLOR_SECONDARY_NAVY = "#13315C"    # secondary navy - subheaders, borders
COLOR_STEEL_BLUE = "#3E6B96"        # accent - links, hover, active states
COLOR_PAGE_BG = "#F4F6F9"           # light page background
COLOR_CARD_BG = "#FFFFFF"           # clean white content cards
COLOR_BORDER = "#D9E0E8"            # hairline borders on cards/tables
COLOR_TEXT_PRIMARY = "#0B2545"
COLOR_TEXT_SECONDARY = "#4A5A6A"
COLOR_ACCENT_AMBER = "#C8941F"      # single warm accent - result emphasis only

FONT_DISPLAY = "'IBM Plex Serif', Georgia, serif"
FONT_BODY = "'IBM Plex Sans', 'Segoe UI', sans-serif"
FONT_MONO = "'IBM Plex Mono', 'Courier New', monospace"


def inject_global_styles() -> None:
    """Inject shared fonts, page background, and component CSS once per page."""
    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">

        <style>
        html, body, [class*="css"] {{
            font-family: {FONT_BODY};
            color: {COLOR_TEXT_PRIMARY};
        }}

        .stApp {{
            background-color: {COLOR_PAGE_BG};
        }}

        section[data-testid="stSidebar"] {{
            background-color: {COLOR_PRIMARY_NAVY};
        }}
        section[data-testid="stSidebar"] * {{
            color: #E7ECF3 !important;
        }}
        section[data-testid="stSidebar"] .nav-brand {{
            font-family: {FONT_DISPLAY};
            font-size: 1.05rem;
            font-weight: 600;
            color: #FFFFFF !important;
            line-height: 1.35;
            padding: 0.25rem 0 0.9rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.18);
            margin-bottom: 0.75rem;
        }}
        section[data-testid="stSidebar"] .nav-brand small {{
            display: block;
            font-family: {FONT_BODY};
            font-weight: 400;
            font-size: 0.72rem;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: #9FB3CC !important;
            margin-top: 0.3rem;
        }}

        h1, h2, h3 {{
            font-family: {FONT_DISPLAY};
            color: {COLOR_PRIMARY_NAVY};
            letter-spacing: -0.01em;
        }}

        h1 {{
            font-weight: 700;
            font-size: 2.0rem;
            line-height: 1.25;
        }}

        h2 {{
            font-weight: 600;
            font-size: 1.35rem;
            border-bottom: 2px solid {COLOR_BORDER};
            padding-bottom: 0.5rem;
            margin-top: 1.75rem;
        }}

        .eyebrow {{
            font-family: {FONT_BODY};
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: {COLOR_STEEL_BLUE};
            margin-bottom: 0.35rem;
        }}

        .app-card {{
            background-color: {COLOR_CARD_BG};
            border: 1px solid {COLOR_BORDER};
            border-radius: 6px;
            padding: 1.4rem 1.6rem;
            margin-bottom: 1.1rem;
        }}

        .app-card h3 {{
            margin-top: 0;
            font-size: 1.05rem;
            border-bottom: none;
        }}

        .app-card ul {{
            margin-bottom: 0;
            padding-left: 1.1rem;
        }}

        .app-card li {{
            margin-bottom: 0.45rem;
            color: {COLOR_TEXT_SECONDARY};
            line-height: 1.55;
        }}

        .metric-card {{
            background-color: {COLOR_CARD_BG};
            border: 1px solid {COLOR_BORDER};
            border-left: 3px solid {COLOR_SECONDARY_NAVY};
            border-radius: 6px;
            padding: 0.9rem 1.1rem;
            height: 100%;
        }}
        .metric-card .metric-label {{
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: {COLOR_TEXT_SECONDARY};
            margin-bottom: 0.3rem;
        }}
        .metric-card .metric-value {{
            font-family: {FONT_MONO};
            font-size: 1.25rem;
            font-weight: 600;
            color: {COLOR_PRIMARY_NAVY};
        }}

        .source-card {{
            background-color: {COLOR_CARD_BG};
            border: 1px solid {COLOR_BORDER};
            border-radius: 6px;
            padding: 1.3rem 1.6rem;
            font-family: {FONT_DISPLAY};
        }}
        .source-card .source-title {{
            font-weight: 600;
            font-size: 1.0rem;
            color: {COLOR_PRIMARY_NAVY};
            line-height: 1.5;
            margin-bottom: 0.6rem;
        }}
        .source-card .source-meta {{
            font-family: {FONT_BODY};
            font-size: 0.85rem;
            color: {COLOR_TEXT_SECONDARY};
            line-height: 1.6;
        }}

        .notice-band {{
            background-color: #EFF3F7;
            border-left: 3px solid {COLOR_STEEL_BLUE};
            border-radius: 4px;
            padding: 0.85rem 1.1rem;
            font-size: 0.9rem;
            color: {COLOR_SECONDARY_NAVY};
        }}

        .result-card {{
            background-color: {COLOR_CARD_BG};
            border: 1px solid {COLOR_BORDER};
            border-top: 4px solid {COLOR_ACCENT_AMBER};
            border-radius: 6px;
            padding: 1.8rem 2rem;
            text-align: center;
        }}
        .result-card .result-label {{
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: {COLOR_TEXT_SECONDARY};
            margin-bottom: 0.5rem;
        }}
        .result-card .result-value {{
            font-family: {FONT_MONO};
            font-size: 2.6rem;
            font-weight: 600;
            color: {COLOR_PRIMARY_NAVY};
            line-height: 1.2;
        }}
        .result-card .result-unit {{
            font-size: 0.85rem;
            color: {COLOR_TEXT_SECONDARY};
            margin-top: 0.4rem;
        }}

        .footer-block {{
            margin-top: 2.5rem;
            padding-top: 1.2rem;
            border-top: 1px solid {COLOR_BORDER};
            text-align: center;
            color: {COLOR_TEXT_SECONDARY};
            font-size: 0.82rem;
            line-height: 1.6;
        }}
        .footer-block strong {{
            color: {COLOR_SECONDARY_NAVY};
        }}

        .stButton > button {{
            background-color: {COLOR_PRIMARY_NAVY};
            color: #FFFFFF;
            border: none;
            border-radius: 5px;
            padding: 0.6rem 1.6rem;
            font-weight: 600;
            font-size: 0.95rem;
            letter-spacing: 0.01em;
            transition: background-color 0.15s ease-in-out;
        }}
        .stButton > button:hover {{
            background-color: {COLOR_STEEL_BLUE};
            color: #FFFFFF;
        }}

        div[data-testid="stDataFrame"] {{
            border: 1px solid {COLOR_BORDER};
            border-radius: 6px;
        }}

        .hull-divider {{
            margin: 1.4rem 0 1.6rem 0;
            opacity: 0.85;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def hull_section_divider() -> str:
    """
    Returns the recurring signature motif: a stylized ship body-plan
    section line, used as a quiet divider between major sections instead
    of a generic <hr>. Echoes the half-breadth/sectional curves naval
    architects draw on a body plan.
    """
    return f"""
    <div class="hull-divider">
        <svg width="100%" height="28" viewBox="0 0 600 28" preserveAspectRatio="none"
             xmlns="http://www.w3.org/2000/svg">
            <line x1="0" y1="14" x2="600" y2="14" stroke="{COLOR_BORDER}" stroke-width="1"/>
            <path d="M 260 26 C 270 6, 290 4, 300 4 C 310 4, 330 6, 340 26"
                  fill="none" stroke="{COLOR_SECONDARY_NAVY}" stroke-width="1.6"/>
        </svg>
    </div>
    """


def sidebar_brand(active_page_count: int | None = None) -> None:
    """Renders the consistent sidebar brand block above the page navigation."""
    st.sidebar.markdown(
        """
        <div class="nav-brand">
            Ship Resistance Predictor
            <small>Series 60 &middot; Preliminary Design</small>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    """Renders the consistent footer block, shared across all pages."""
    from config import FOOTER_NAME, FOOTER_ROLE, FOOTER_TAGLINE

    st.markdown(
        f"""
        <div class="footer-block">
            Developed by <strong>{FOOTER_NAME}</strong><br/>
            {FOOTER_ROLE}<br/>
            {FOOTER_TAGLINE}
        </div>
        """,
        unsafe_allow_html=True,
    )
