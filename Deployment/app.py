import streamlit as st
import joblib
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🩺",
    layout="centered"
)

# Load model
model = joblib.load("random_forest_model.joblib")

# Title
st.title("🩺 Liver Disease Prediction System")
st.write("Enter patient medical details to predict liver disease.")

# Input fields
total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, format="%.3f")
direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, format="%.3f")
alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0.0, format="%.3f")
alamine_aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0.0, format="%.3f")
total_protiens = st.number_input("Total Proteins", min_value=0.0, format="%.3f")
albumin = st.number_input("Albumin", min_value=0.0, format="%.3f")
albumin_and_globulin_ratio = st.number_input("Albumin & Globulin Ratio", min_value=0.0, format="%.3f")

# Predict button
if st.button("Predict"):

    features = np.array([[ 
        total_bilirubin,
        direct_bilirubin,
        alkaline_phosphotase,
        alamine_aminotransferase,
        total_protiens,
        albumin,
        albumin_and_globulin_ratio
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ Liver Disease Detected")
    else:
        st.success("✅ Liver is Healthy")
