"""
config.py

Central configuration for the Froude's Circular Constant Prediction application.
Holds model metadata, feature definitions, validity ranges, and dataset
information in one place so every page stays consistent and the app
remains easy to maintain.
"""

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Model metadata
# ---------------------------------------------------------------------------

MODEL_PATH = "ship_resistance_model.json"

MODEL_INFO = {
    "Algorithm": "XGBoost Regressor",
    "Training Samples": "484",
    "Input Features": "7",
    "Output": "Froude's Circular Constant",
    "Validation Method": "Unseen Hull Forms Testing",
    "Test Hulls": "4211 and 4213",
    "R\u00b2 Score": "99.20%",
    "MAE": "0.01633",
}

DATASET_SOURCE = {
    "title": "Series 60 Methodical Experiments with Models of Single-Screw Merchant Ships",
    "author": "F. H. Todd, Ph.D.",
    "report": "Research and Development Report 1712",
    "date": "July 1963",
}


# ---------------------------------------------------------------------------
# Feature definitions
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Feature:
    key: str            # column name expected by the trained model
    symbol: str          # short symbol shown in tables / inputs
    full_name: str        # descriptive name
    minimum: float
    maximum: float
    default: float
    help_text: str
    step: float = 0.001


# Order matters: must match the exact column order the model was trained on.
FEATURES: list[Feature] = [
    Feature(
        key="CB",
        symbol="CB",
        full_name="Block Coefficient",
        minimum=0.60,
        maximum=0.80,
        default=0.70,
        help_text="Ratio of the hull's underwater volume to the volume of a "
                   "rectangular block with the same length, breadth, and draft. "
                   "Higher values indicate a fuller, less streamlined hull.",
    ),
    Feature(
        key="Cp",
        symbol="CP",
        full_name="Prismatic Coefficient",
        minimum=0.614,
        maximum=0.805,
        default=0.70,
        help_text="Ratio of the hull's underwater volume to the volume of a "
                   "prism with length equal to the hull and cross-section "
                   "equal to the maximum section area. Describes the "
                   "longitudinal distribution of volume.",
    ),
    Feature(
        key="CW",
        symbol="CW",
        full_name="Waterplane Coefficient",
        minimum=0.700,
        maximum=0.871,
        default=0.78,
        help_text="Ratio of the waterplane area to the area of a rectangle "
                   "with the same length and breadth. Reflects the fullness "
                   "of the hull at the waterline.",
    ),
    Feature(
        key="Speed_Length_Ratio",
        symbol="V / \u221aLWL",
        full_name="Speed-Length Ratio",
        minimum=0.25,
        maximum=1.20,
        default=0.70,
        help_text="Speed-to-length ratio relating ship speed to the square "
                   "root of the waterline length. A classical non-dimensional "
                   "speed parameter used throughout Series 60 resistance data.",
    ),
    Feature(
        key="Froude_Number",
        symbol="K",
        full_name="Froude's Speed Coefficient",
        minimum=0.60,
        maximum=3.17,
        default=1.80,
        help_text="Froude's Speed Coefficient (K), the non-dimensional speed "
                   "parameter used in the original Series 60 resistance "
                   "experiments by Todd (1963).",
    ),
    Feature(
        key="LCB_Final",
        symbol="LCB",
        full_name="Longitudinal Center of Buoyancy",
        minimum=-2.48,
        maximum=3.51,
        default=0.00,
        help_text="Position of the longitudinal center of buoyancy as a "
                   "percentage of waterline length, measured from midships. "
                   "Positive values are forward of midships; negative values "
                   "are aft of midships.",
    ),
    Feature(
        key="S_Wetted_Coeff",
        symbol="S / \u2207^(2/3)",
        full_name="Wetted Surface Coefficient",
        minimum=6.01,
        maximum=6.527,
        default=6.27,
        help_text="Ratio of the wetted surface area to the volumetric "
                   "displacement raised to the two-thirds power. Relates the "
                   "frictional resistance area to the hull's displaced volume.",
    ),
]

FEATURE_BY_KEY: dict[str, Feature] = {f.key: f for f in FEATURES}

# Exact column order expected by the trained model.
FEATURE_ORDER: list[str] = [f.key for f in FEATURES]


# ---------------------------------------------------------------------------
# Application copy
# ---------------------------------------------------------------------------

APP_TITLE = "AI-Based Froude's Circular Constant Prediction for Series 60 Hull Forms"
APP_SUBTITLE = "Preliminary Design Stage"

PROJECT_DESCRIPTION = (
    "This application uses an XGBoost machine learning model trained on "
    "Series 60 resistance data to estimate the Froude's Circular Constant "
    "during the preliminary ship design stage."
)

DESIGN_PHILOSOPHY = [
    "All selected inputs are dimensionless parameters.",
    "The feature set was chosen specifically for the preliminary ship "
    "design stage.",
    "Parameters requiring detailed hull geometry were intentionally excluded.",
    "The final feature set was selected to achieve a balance between "
    "practical usability and prediction accuracy.",
]

VALIDITY_NOTICE = (
    "Predictions are intended only for Series 60 hull forms within the "
    "specified parameter ranges."
)

FOOTER_NAME = "Belal Moustafa"
FOOTER_ROLE = "Naval Architecture and Marine Engineering Student"
FOOTER_TAGLINE = "Powered by XGBoost Machine Learning"
