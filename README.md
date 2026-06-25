# Ship Resistance Coefficient Predictor

**AI-based prediction of the Series 60 ship hull Resistance Coefficient for the preliminary design stage using XGBoost.**

Live application:
https://shipresistancecoefficientpredictor-k4pibvgdawzpmpc5tq4xci.streamlit.app/

---

## Overview

This project presents an **AI-based prediction tool for the Resistance Coefficient of Series 60 single-screw merchant ship hull forms** during the **preliminary ship design stage**. The application is intended to provide a fast engineering estimate of resistance behavior using a compact set of high-level hull-form and operating parameters, without requiring detailed hull geometry.

The predictive model is an **XGBoost Regressor** trained on **484 experimental examples** derived from the classical **Series 60 methodical experiments**. The model was evaluated using **unseen hull-form testing**, where complete hull forms were withheld from training in order to assess true generalization performance rather than interpolation across already-seen models.

The final application is built as a **multi-page Streamlit engineering tool** aimed at:

* Naval Architecture students
* Marine engineering students
* Researchers working on preliminary ship design
* Anyone interested in applying machine learning to classical ship hydrodynamics datasets

---

## Project Objective

The objective of this project is to estimate the **Resistance Coefficient** of **Series 60 hull forms** from a small set of **dimensionless input parameters** suitable for **preliminary design**.

The main design philosophy behind the model is:

* All selected model inputs are **dimensionless parameters**
* The selected feature set is intended specifically for the **preliminary design stage**
* Parameters that require detailed hull geometry were intentionally excluded
* The final feature set was selected to provide a balance between:

  * **practical usability**
  * **engineering relevance**
  * **high predictive accuracy**

This means the tool is designed to be useful **before a detailed hull surface model exists**, which is exactly the stage where quick performance estimates are valuable.

---

## Model Summary

| Item                     | Value                    |
| ------------------------ | ------------------------ |
| Model type               | XGBoost Regressor        |
| Training examples        | 484                      |
| Number of input features | 7                        |
| Target output            | Resistance Coefficient   |
| Validation strategy      | Unseen hull-form testing |
| Held-out test hulls      | 4211 and 4213            |
| R² score                 | 99.20%                   |
| MAE                      | 0.01633                  |

---

## Dataset Source

The dataset used in this project originates from the classical Series 60 experimental report:

> **Series 60 Methodical Experiments with Models of Single-Screw Merchant Ships**
> **F. H. Todd, Ph.D.**
> **Research and Development Report 1712**
> **July 1963**

The experimental tables from this report were digitized and converted into structured CSV files, then processed into a machine-learning-ready dataset.

---

## Input Parameters Used by the Model

The model uses **7 input features**, all of which are **dimensionless**.

| Symbol                 | Description                                      |
| ---------------------- | ------------------------------------------------ |
| **CB**                 | Block Coefficient                                |
| **Cp**                 | Prismatic Coefficient                            |
| **CW**                 | Waterplane Coefficient                           |
| **Speed_Length_Ratio** | Speed-Length Ratio, ( V / \sqrt{LWL} )           |
| **Froude_Coefficient** | Froude coefficient                               |
| **LCB_Final**          | Longitudinal Center of Buoyancy                  |
| **S_Wetted_Coeff**     | Wetted Surface Coefficient, ( S / \nabla^{2/3} ) |

### Notes on the input set

* The model intentionally uses **dimensionless variables only**
* This choice makes the model more suitable for **preliminary design work**
* Parameters such as **L/B** and **B/H** were not used as predictive inputs in the final model
* These excluded parameters are instead treated as **fixed constraints of the Series 60 family**, not as free design variables to be entered by the user

### LCB sign convention

For **LCB_Final**:

* **Positive values** indicate **forward of midships**
* **Negative values** indicate **aft of midships**

---

## Why Some Parameters Were Excluded

Although the original Series 60 data includes additional geometric ratios such as **L/B** and **B/H**, these were not included in the final feature set.

The reason is practical and engineering-based:

1. The goal of the model is to support the **preliminary design stage**
2. The final model should rely on parameters that a designer can reasonably estimate early
3. Within the available Series 60 dataset, some geometric quantities behave more like **family constraints** than truly independent design variables
4. Keeping the input set compact improves usability without sacrificing accuracy

As a result, the final feature set focuses on the parameters that best represent the hull form and operating condition while remaining practical for early-stage estimation.

---

## Train/Test Strategy and Why It Matters

A central challenge in this project was building a test strategy that genuinely measures **generalization to unseen hull forms**, rather than allowing hidden leakage from the same model family into both train and test data.

### Initial concern: possible data leakage

Each hull model in the Series 60 dataset appears at multiple operating conditions. If rows are split carelessly, the model may end up seeing some operating points of the **same hull form** during training and different operating points of that same hull during testing. That would inflate performance and give a misleading picture of how well the model truly generalizes.

### Solution: grouped split logic

To avoid this issue, the splitting logic was designed so that the final evaluation is performed on **entire unseen hull forms**, not random individual rows.

The **stratify column** was constructed from both Model Number and CB together during preprocessing to support safer splitting and better dataset organization.

### Final evaluation approach

For the final model evaluation:

* Hull **4211** was withheld completely from training
* Hull **4213** was withheld completely from training
* The trained model was then tested on those unseen hulls only

This means the reported performance reflects the model’s ability to estimate the target for **new hull forms it never saw during training**, which is much more meaningful from an engineering point of view than a random row-wise split.

---

## Project Workflow

The repository follows a clear pipeline from raw processed data to final application deployment.

---

## 1) Data Preparation

**Folder:** `notebooks_and_data/1_Data_Preparation/`

This stage contains the dataset preparation work.

### Main files

* `Series60_Data.csv`
* `making new file.ipynb`

### Purpose of this stage

This step is responsible for preparing the dataset before splitting or model training. It includes operations such as:

* organizing the digitized data
* computing or arranging the required model inputs
* preparing the data structure used in later stages
* creating the additional **stratify column** needed for safe splitting logic

---

## 2) Train/Test Split

**Folder:** `notebooks_and_data/2_Train_Test_Split/`

This stage contains the logic used to prepare the train and test sets.

### Main files

* `Series60_with_stratify_column.csv`
* `making train and test.ipynb`

### Purpose of this stage

This step handles:

* preparing the dataset for training/testing
* using the **stratify column**
* selecting the unseen hulls for evaluation
* generating the final training and testing CSV files used later in model development

This is the stage where the leakage-aware split logic is applied.

---

## 3) Model Evaluation

**Folder:** `notebooks_and_data/Resistance Predictor 4/`

-This stage contains the notebook used to train and evaluate the predictive model before final deployment.
-Early stopping determines the optimal tree count (best_iteration = 290).
-Feature importance was assessed using permutation importance rather than default gain-based importance.

### Main files

* `3_MAE_and_R2_Calc.ipynb`
* `Series60_train_3.csv`
* `Series60_test_3.csv`

### Purpose of this stage

This notebook is used to:

* train the XGBoost regression model
* evaluate the model on the held-out unseen hull forms
* compute the final reported metrics:

  * **R² score**
  * **MAE**

The reported performance of the project comes from this stage.

---

## 4) Final Model Training

**Folder:** `notebooks_and_data/Resistance Predictor 5/`

This stage contains the final training notebook used to generate the deployable model file.

### Main files

* `Final_Model_Training.ipynb`
* `Series60_with_stratify_column.csv`

### Purpose of this stage

After confirming the model’s performance in the evaluation stage, the final model is retrained for deployment purposes and saved as:

* `ship_resistance_model.json`

This is the model file loaded by the Streamlit application.

---

## 5) Streamlit Application

The deployed application provides a clean engineering interface for interacting with the trained model.

### Main files

* `app.py`
* `config.py`
* `model_utils.py`
* `styles.py`
* `pages/1_input_guide.py`
* `pages/2_constraints.py`
* `pages/3_resistance_estimation.py`

---

## Application Pages

The Streamlit app is organized into multiple pages:

### 1. Home

Provides:

* project overview
* model summary
* dataset citation
* academic framing of the tool

### 2. Input Guide

Explains:

* each model input
* its symbol
* its engineering meaning
* the LCB sign convention

### 3. Constraints

Displays the validity ranges for the model inputs and clarifies the boundaries within which the model should be used.

### 4. Resistance Estimation

This is the main prediction page where the user enters the seven input parameters and receives the predicted **Resistance Coefficient**.

---

## Model Validity Limits

The model should be used **only within the parameter ranges represented in the training data**.

| Parameter              | Minimum | Maximum |
| ---------------------- | ------: | ------: |
| **CB**                 |    0.60 |    0.80 |
| **Cp**                 |   0.614 |   0.805 |
| **CW**                 |   0.700 |   0.871 |
| **Speed_Length_Ratio** |    0.25 |    1.20 |
| **Froude_Coefficient** |    0.60 |    3.17 |
| **LCB_Final**          |   -2.48 |    3.51 |
| **S_Wetted_Coeff**     |    6.01 |   6.527 |

### Important note

Predictions are intended **only for Series 60 hull forms within these parameter ranges**.
Using the model outside these limits falls outside the experimental envelope of the training data and should not be considered reliable.

---

## Repository Structure

```text
Ship_Resistance_Coefficient_Predictor/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── notebooks_and_data/
│   │
│   ├── 1_Data_Preparation/
│   │   ├── Series60_Data.csv
│   │   └── making new file.ipynb
│   │
│   ├── 2_Train_Test_Split/
│   │   ├── Series60_with_stratify_column.csv
│   │   └── making train and test.ipynb
│   │
│   ├── Resistance Predictor 4/
│   │   ├── 3_MAE_and_R2_Calc.ipynb
│   │   ├── Series60_train_3.csv
│   │   └── Series60_test_3.csv
│   │
│   └── Resistance Predictor 5/
│       ├── Final_Model_Training.ipynb
│       └── Series60_with_stratify_column.csv
│
├── pages/
│   ├── 1_input_guide.py
│   ├── 2_constraints.py
│   └── 3_resistance_estimation.py
│
├── app.py
├── config.py
├── model_utils.py
├── styles.py
├── ship_resistance_model.json
├── requirements.txt
└── README.md
```

---

## Running the Application Locally

Clone the repository, install the dependencies, and run the Streamlit app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Engineering Notes

This project is intentionally positioned at the intersection of:

* **Naval Architecture**
* **Ship Hydrodynamics**
* **Preliminary Ship Design**
* **Applied Machine Learning**

The emphasis is not simply on obtaining a high numerical score, but on building a model whose inputs make engineering sense for early-stage ship design and whose validation strategy respects the structure of the underlying experimental data.

The final application is therefore meant to function not only as a prediction tool, but also as a compact academic demonstration of how classical ship-design data can be integrated with modern machine learning methods in a disciplined engineering workflow.

---

## Author

**Belal Moustafa**
Naval Architecture and Marine Engineering Student
