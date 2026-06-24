"""
pages/2_constraints.py

Constraints page: displays the valid input ranges the model was trained
on, and a clear notice that predictions outside these ranges are not
reliable.
"""

import pandas as pd
import streamlit as st

from config import FEATURES, VALIDITY_NOTICE
from styles import inject_global_styles, hull_section_divider, sidebar_brand, render_footer

st.set_page_config(page_title="Constraints | Froude's Circular Constant", layout="wide")
inject_global_styles()
sidebar_brand()

st.markdown('<div class="eyebrow">Model Validity</div>', unsafe_allow_html=True)
st.title("Constraints")
st.write(
    "The model was trained exclusively on Series 60 hull forms within the "
    "ranges listed below. Inputs are restricted to these limits throughout "
    "the application."
)

st.markdown(hull_section_divider(), unsafe_allow_html=True)

st.markdown("## Model Validity Limits")

limits_rows = [
    {
        "Parameter": f.symbol,
        "Minimum": f.minimum,
        "Maximum": f.maximum,
    }
    for f in FEATURES
]
limits_df = pd.DataFrame(limits_rows)
st.dataframe(
    limits_df,
    hide_index=True,
    width="stretch",
    column_config={
        "Minimum": st.column_config.NumberColumn(format="%.3f"),
        "Maximum": st.column_config.NumberColumn(format="%.3f"),
    },
)

st.markdown(
    f"""
    <div class="notice-band">
        {VALIDITY_NOTICE}
    </div>
    """,
    unsafe_allow_html=True,
)

render_footer()
