"""
pages/3_resistance_estimation.py

Resistance Estimation page: the core functionality of the application.
Collects the seven model inputs via number inputs (engineers typically
know exact values rather than needing sliders), runs the trained model,
and displays the predicted Froude's Circular Constant.
"""

import streamlit as st

from config import FEATURE_BY_KEY
from model_utils import load_model, predict_resistance_coefficient
from styles import inject_global_styles, hull_section_divider, sidebar_brand, render_footer

st.set_page_config(page_title="Froude's Circular Constant Estimation | Froude's Circular Constant Prediction", layout="wide")
inject_global_styles()
sidebar_brand()

st.markdown('<div class="eyebrow">Prediction</div>', unsafe_allow_html=True)
st.title("Resistance Estimation")
st.write(
    "Enter the seven hull-form parameters within their valid ranges to "
    "estimate the Froude's Circular Constant."
)

st.markdown(hull_section_divider(), unsafe_allow_html=True)

st.markdown("## Hull Form Parameters")

cb_feature = FEATURE_BY_KEY["CB"]
cp_feature = FEATURE_BY_KEY["Cp"]
cw_feature = FEATURE_BY_KEY["CW"]
slr_feature = FEATURE_BY_KEY["Speed_Length_Ratio"]
froude_feature = FEATURE_BY_KEY["Froude_Number"]
lcb_feature = FEATURE_BY_KEY["LCB_Final"]
wetted_feature = FEATURE_BY_KEY["S_Wetted_Coeff"]

input_values: dict[str, float] = {}

row_one = st.columns(2)
row_two = st.columns(2)
row_three = st.columns(2)

# -- CB ------------------------------------------------------------------
with row_one[0]:
    st.markdown(
        f"""<div class="app-card"><h3>{cb_feature.symbol} &mdash; {cb_feature.full_name}</h3>""",
        unsafe_allow_html=True,
    )
    input_values["CB"] = st.number_input(
        label="Value",
        min_value=cb_feature.minimum,
        max_value=cb_feature.maximum,
        value=cb_feature.default,
        step=cb_feature.step,
        format="%.3f",
        help=cb_feature.help_text,
        key="input_CB",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -- Cp --------------------------------------------------------------------
with row_one[1]:
    st.markdown(
        f"""<div class="app-card"><h3>{cp_feature.symbol} &mdash; {cp_feature.full_name}</h3>""",
        unsafe_allow_html=True,
    )
    input_values["Cp"] = st.number_input(
        label="Value",
        min_value=cp_feature.minimum,
        max_value=cp_feature.maximum,
        value=cp_feature.default,
        step=cp_feature.step,
        format="%.3f",
        help=cp_feature.help_text,
        key="input_Cp",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -- CW ------------------------------------------------------------------
with row_two[0]:
    st.markdown(
        f"""<div class="app-card"><h3>{cw_feature.symbol} &mdash; {cw_feature.full_name}</h3>""",
        unsafe_allow_html=True,
    )
    input_values["CW"] = st.number_input(
        label="Value",
        min_value=cw_feature.minimum,
        max_value=cw_feature.maximum,
        value=cw_feature.default,
        step=cw_feature.step,
        format="%.3f",
        help=cw_feature.help_text,
        key="input_CW",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -- Speed-Length Ratio -----------------------------------------------------
with row_two[1]:
    st.markdown(
        f"""<div class="app-card"><h3>{slr_feature.symbol} &mdash; {slr_feature.full_name}</h3>""",
        unsafe_allow_html=True,
    )
    input_values["Speed_Length_Ratio"] = st.number_input(
        label="Value",
        min_value=slr_feature.minimum,
        max_value=slr_feature.maximum,
        value=slr_feature.default,
        step=slr_feature.step,
        format="%.3f",
        help=slr_feature.help_text,
        key="input_SLR",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -- Froude's Speed Coefficient (K) -----------------------------------------
with row_three[0]:
    st.markdown(
        f"""<div class="app-card"><h3>{froude_feature.symbol} &mdash; {froude_feature.full_name}</h3>""",
        unsafe_allow_html=True,
    )
    input_values["Froude_Number"] = st.number_input(
        label="Value",
        min_value=froude_feature.minimum,
        max_value=froude_feature.maximum,
        value=froude_feature.default,
        step=froude_feature.step,
        format="%.3f",
        help=froude_feature.help_text,
        key="input_K",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -- Wetted Surface Coefficient ----------------------------------------------
with row_three[1]:
    st.markdown(
        f"""<div class="app-card"><h3>{wetted_feature.symbol} &mdash; {wetted_feature.full_name}</h3>""",
        unsafe_allow_html=True,
    )
    input_values["S_Wetted_Coeff"] = st.number_input(
        label="Value",
        min_value=wetted_feature.minimum,
        max_value=wetted_feature.maximum,
        value=wetted_feature.default,
        step=wetted_feature.step,
        format="%.3f",
        help=wetted_feature.help_text,
        key="input_Wetted",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -- LCB: direction + magnitude, combined internally -------------------------
lcb_col = st.columns(1)[0]
with lcb_col:
    st.markdown(
        f"""<div class="app-card"><h3>{lcb_feature.symbol} &mdash; {lcb_feature.full_name}</h3>""",
        unsafe_allow_html=True,
    )
    direction_col, value_col = st.columns([1, 1.4])
    with direction_col:
        lcb_direction = st.radio(
            label="LCB Direction",
            options=["Fore (+)", "Aft (-)"],
            help=lcb_feature.help_text,
            key="input_LCB_direction",
        )
    with value_col:
        lcb_magnitude = st.number_input(
            label="LCB Value",
            min_value=0.0,
            max_value=max(abs(lcb_feature.minimum), abs(lcb_feature.maximum)),
            value=abs(lcb_feature.default),
            step=lcb_feature.step,
            format="%.3f",
            help="Enter the magnitude only. Use LCB Direction to set the sign.",
            key="input_LCB_value",
        )

    signed_lcb = lcb_magnitude if lcb_direction == "Fore (+)" else -lcb_magnitude
    signed_lcb = max(lcb_feature.minimum, min(lcb_feature.maximum, signed_lcb))
    input_values["LCB_Final"] = signed_lcb

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(hull_section_divider(), unsafe_allow_html=True)

# -- Prediction trigger -------------------------------------------------------
predict_clicked = st.button("Estimate Resistance Coefficient", width="content")

if predict_clicked:
    model = load_model()
    predicted_value = predict_resistance_coefficient(model, input_values)

    st.markdown("## Result")
    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-label">Predicted Resistance Coefficient</div>
            <div class="result-value">{predicted_value:.6f}</div>
            <div class="result-unit">Unitless Coefficient</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown("### Input Parameters Used")

    display_rows = [
        {"Input Parameter": cb_feature.symbol, "Value Used": f"{input_values['CB']:.3f}"},
        {"Input Parameter": cp_feature.symbol, "Value Used": f"{input_values['Cp']:.3f}"},
        {"Input Parameter": cw_feature.symbol, "Value Used": f"{input_values['CW']:.3f}"},
        {"Input Parameter": slr_feature.symbol, "Value Used": f"{input_values['Speed_Length_Ratio']:.3f}"},
        {"Input Parameter": froude_feature.symbol, "Value Used": f"{input_values['Froude_Number']:.3f}"},
        {"Input Parameter": lcb_feature.symbol, "Value Used": f"{input_values['LCB_Final']:.3f}"},
        {"Input Parameter": wetted_feature.symbol, "Value Used": f"{input_values['S_Wetted_Coeff']:.3f}"},
    ]
    st.dataframe(display_rows, hide_index=True, width="stretch")

render_footer()
