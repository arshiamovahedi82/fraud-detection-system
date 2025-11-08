import streamlit as st
import requests
import numpy as np

st.title("💳 Credit Card Fraud Detection App")

st.write("Enter transaction values below to predict fraud:")

# Create input boxes for 30 features
features = []
feature_names = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]

for name in feature_names:
    val = st.number_input(f"Enter {name}", value=0.0, step=0.01)
    features.append(val)

if st.button("Predict Fraud"):
    data = {"features": features}
    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"🔍 Prediction: {result['result']} (0=Not Fraud, 1=Fraud)")
    else:
        st.error("API request failed. Check server.")
