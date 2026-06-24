"""
pages/1_input_guide.py

Input Guide page: explains every model input parameter, its symbol,
and a concise engineering description, so users understand the inputs
without needing to leave the page.
"""

import pandas as pd
import streamlit as st

from config import FEATURES
from styles import inject_global_styles, hull_section_divider, sidebar_brand, render_footer

st.set_page_config(page_title="Input Guide | Froude's Circular Constant Prediction", layout="wide")
inject_global_styles()
sidebar_brand()

st.markdown('<div class="eyebrow">Reference</div>', unsafe_allow_html=True)
st.title("Input Guide")
st.write(
    "This page describes every parameter used by the prediction model, "
    "including its symbol, full name, and engineering meaning."
)

st.markdown(hull_section_divider(), unsafe_allow_html=True)

# -- Symbol / Full Name table --------------------------------------------------
st.markdown("## Parameter Reference Table")

table_rows = [{"Symbol": f.symbol, "Full Name": f.full_name} for f in FEATURES]
reference_df = pd.DataFrame(table_rows)
st.dataframe(reference_df, hide_index=True, width="stretch")

st.markdown(hull_section_divider(), unsafe_allow_html=True)

# -- Detailed explanations -----------------------------------------------------
st.markdown("## Parameter Descriptions")

for feature in FEATURES:
    st.markdown(
        f"""
        <div class="app-card">
            <h3>{feature.symbol} &mdash; {feature.full_name}</h3>
            <p style="color:#4A5A6A; line-height:1.6; margin-bottom:0;">{feature.help_text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -- LCB sign convention, called out separately as requested -----------------
st.markdown(
    """
    <div class="notice-band">
        <strong>LCB Sign Convention</strong><br/>
        Positive values indicate a position forward of midships.<br/>
        Negative values indicate a position aft of midships.
    </div>
    """,
    unsafe_allow_html=True,
)

render_footer()
