import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/house_price_model.pkl")

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏠 House Price Prediction System")

st.write("Enter house details below:")

# User inputs
OverallQual = st.slider("Overall Quality (1–10)", 1, 10, 5)
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", 300, 6000, 1500)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", 0, 6000, 800)
GarageCars = st.slider("Garage Cars Capacity", 0, 4, 2)
YearBuilt = st.number_input("Year Built", 1870, 2025, 2000)
Neighborhood = st.selectbox(
    "Neighborhood",
    [
        "NAmes", "CollgCr", "OldTown", "Edwards", "Somerst",
        "Gilbert", "NridgHt", "Sawyer", "BrkSide", "Mitchel"
    ]
)

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "OverallQual": [OverallQual],
        "GrLivArea": [GrLivArea],
        "TotalBsmtSF": [TotalBsmtSF],
        "GarageCars": [GarageCars],
        "YearBuilt": [YearBuilt],
        "Neighborhood": [Neighborhood]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated House Price: ${prediction:,.2f}")
