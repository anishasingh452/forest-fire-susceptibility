# Forest Fire Burned Area Prediction with Spatial Validation and SHAP Interpretability

This repository contains a regression modeling pipeline for predicting forest fire burned area using meteorological, temporal, and spatial variables from the UCI Forest Fires dataset. The project integrates spatial cross-validation and SHAP (SHapley Additive exPlanations) to evaluate model performance and interpretability in a transparent and reproducible way.

---

## Project Structure
FOREST-FIRE-SUSCEPTIBILITY/
│
├── data/
│ └── raw/ # Original dataset (forestfires.csv)
│
├── figures/ # Visualizations and plots
│
├── notebooks/ # Jupyter or Colab notebooks
│
├── src/
│ └── data_preprocessing.py # Feature engineering and preprocessing scripts
│
├── requirements.txt # Dependency list
└── README.md # Project overview and documentation


---

## Problem Statement

The objective is to predict the log-transformed burned area of forest fires using daily weather variables, encoded time features, and spatial coordinates (X, Y). A core emphasis is placed on ensuring models generalize spatially and remain interpretable.

---

## Models Implemented

- Linear Regression (baseline)
- Random Forest Regressor
- XGBoost Regressor

Model performance is evaluated using:

- Mean Squared Error (MSE)
- R² Score
- 5-Fold Spatial Cross-Validation (based on KMeans clustering of spatial coordinates)

---

## Explainability using SHAP

SHAP was used to interpret feature contributions both globally and locally:

- Global: SHAP beeswarm and bar plots reveal `DMC`, `temperature`, `RH`, and `X` as primary predictors.
- Local: Force and waterfall plots highlight how individual feature values affect single predictions.

---

## Spatial Evaluation

Spatial cross-validation ensures the model is evaluated on geographically distinct regions, addressing the issue of spatial autocorrelation present in naive random splits. Residual heatmaps and scatter plots assess spatial generalization.

---

## Key Insights

- Predictive performance remains low, indicating limited learnable signal in the dataset alone.
- SHAP reveals that dryness indices and temperature contribute most to predictions.
- Many temporal and categorical encodings (e.g., weekday, month) had little impact.

---

## Limitations

- The dataset lacks vegetation cover, elevation, wind direction, and land surface information.
- Target variable is highly imbalanced with many zero values.
- No time-lagged variables or multi-day temporal context is incorporated.

---

## Future Work

- Integrate remote sensing variables (NDVI, LST) and topographic data.
- Include wind direction, vegetation type, and slope as predictors.
- Test time series models or hybrid architectures that account for spatial-temporal trends.

---

## Installation Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/forest-fire-susceptibility.git
cd forest-fire-susceptibility

# Set up virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

## References

- UCI Forest Fires Dataset: https://archive.ics.uci.edu/ml/datasets/Forest+Fires
- Lundberg, S. & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. *NeurIPS*.
- Valavi et al. (2019). Predictive performance of spatial models. *Journal of Environmental Management*.

## Author

This project was developed by Anisha Singh for research and academic purposes.