# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🏦 Customer Churn Predictor")
st.write("Enter customer data to predict the probability of churn.")

# Input fields
age = st.slider("Age", 18, 100, 35)
balance = st.number_input("Account Balance", min_value=0.0, value=50000.0)
salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)
products = st.selectbox("Number of Products", [1, 2, 3, 4])
tenure = st.slider("Tenure (years with bank)", 0, 10, 5)
credit_score = st.slider("Credit Score", 300, 900, 600)
active = st.selectbox("Is Active Member", ["Yes", "No"])

# Encode binary input
active_encoded = 1 if active == "Yes" else 0

# Predict button
if st.button("Predict Churn"):
    input_data = pd.DataFrame([[age, balance, salary, products, tenure, credit_score, active_encoded]],
                              columns=['Age', 'Balance', 'EstimatedSalary', 'NumOfProducts',
                                       'Tenure', 'CreditScore', 'IsActiveMember'])

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    # Predict probability
    prob_churn = model.predict_proba(input_scaled)[0][1]

    # Display result
    st.subheader("🔮 Prediction")
    st.write(f"Probability of Churn: **{prob_churn:.2%}**")

    if prob_churn > 0.5:
        st.error("⚠️ High risk of churn")
    else:
        st.success("✅ Low risk of churn")