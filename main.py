import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("🏡 House Price Prediction App")

st.write("Enter house details to predict the price:")

# Inputs
area = st.number_input("Area (sq ft)", value=1000)
bedrooms = st.number_input("Number of Bedrooms", value=2, step=1)
age = st.number_input("Age of House (years)", value=10)

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, age]])
    prediction = model.predict(features)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")

