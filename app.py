"""
app.py

Application entry point. Defines the page navigation structure using
Streamlit's modern st.navigation API and renders the Home page content.
"""

import streamlit as st

from config import (
    APP_TITLE,
    APP_SUBTITLE,
    PROJECT_DESCRIPTION,
    DESIGN_PHILOSOPHY,
    MODEL_INFO,
    DATASET_SOURCE,
)
from styles import inject_global_styles, hull_section_divider, sidebar_brand, render_footer


def render_home() -> None:
    st.markdown('<div class="eyebrow">Naval Architecture &middot; Machine Learning</div>', unsafe_allow_html=True)
    st.title(APP_TITLE)
    st.markdown(f"##### {APP_SUBTITLE}")

    st.write("")
    st.write(PROJECT_DESCRIPTION)

    st.markdown(hull_section_divider(), unsafe_allow_html=True)

    # -- Design Philosophy -------------------------------------------------
    st.markdown("## Design Philosophy")
    philosophy_html = "".join(f"<li>{item}</li>" for item in DESIGN_PHILOSOPHY)
    st.markdown(
        f"""
        <div class="app-card">
            <ul>{philosophy_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -- Model Information ---------------------------------------------------
    st.markdown("## Model Information")
    info_items = list(MODEL_INFO.items())
    cols_per_row = 4
    for row_start in range(0, len(info_items), cols_per_row):
        row_items = info_items[row_start: row_start + cols_per_row]
        cols = st.columns(len(row_items))
        for col, (label, value) in zip(cols, row_items):
            with col:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">{label}</div>
                        <div class="metric-value">{value}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        st.write("")

    # -- Dataset Source -------------------------------------------------------
    st.markdown("## Dataset Source")
    st.markdown(
        f"""
        <div class="source-card">
            <div class="source-title">{DATASET_SOURCE['title']}</div>
            <div class="source-meta">
                {DATASET_SOURCE['author']}<br/>
                {DATASET_SOURCE['report']}<br/>
                {DATASET_SOURCE['date']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_footer()


def main() -> None:
    st.set_page_config(
        page_title="Ship Resistance Prediction | Series 60",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_global_styles()
    sidebar_brand()

    home_page = st.Page(render_home, title="Home", url_path="home", default=True)
    input_guide_page = st.Page("pages/1_input_guide.py", title="Input Guide", url_path="input-guide")
    constraints_page = st.Page("pages/2_constraints.py", title="Constraints", url_path="constraints")
    estimation_page = st.Page("pages/3_resistance_estimation.py", title="Resistance Estimation", url_path="estimation")

    navigation = st.navigation(
        [home_page, input_guide_page, constraints_page, estimation_page]
    )
    navigation.run()


if __name__ == "__main__":
    main()
