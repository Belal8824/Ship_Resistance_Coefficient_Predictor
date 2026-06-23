"""
model_utils.py

Handles loading the trained XGBoost model and running predictions.
Loading is cached so the model is read from disk only once per session.
"""

import pandas as pd
import streamlit as st
from xgboost import XGBRegressor

from config import MODEL_PATH, FEATURE_ORDER


@st.cache_resource(show_spinner=False)
def load_model() -> XGBRegressor:
    """
    Loads the trained XGBoost Regressor from its JSON file.
    Cached as a resource so the model is deserialized only once per
    running session rather than on every prediction.
    """
    model = XGBRegressor()
    model.load_model(MODEL_PATH)
    return model


def predict_resistance_coefficient(model: XGBRegressor, feature_values: dict) -> float:
    """
    Runs a single prediction.

    Parameters
    ----------
    model : XGBRegressor
        The loaded, trained model.
    feature_values : dict
        Mapping of feature key -> numeric value. Must contain every key
        in FEATURE_ORDER.

    Returns
    -------
    float
        The predicted Resistance Coefficient.
    """
    ordered_row = {key: [feature_values[key]] for key in FEATURE_ORDER}
    input_frame = pd.DataFrame(ordered_row, columns=FEATURE_ORDER)
    prediction = model.predict(input_frame)
    return float(prediction[0])
