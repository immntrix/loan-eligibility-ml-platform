import streamlit as st
import requests

st.title("Loan Eligibility Predictor")

age = st.number_input("Age")
income = st.number_input("Income")
credit_score = st.number_input("Credit Score")

if st.button("Predict"):
    res = requests.post(
<<<<<<< HEAD
        "http://localhost:8000/predict",
=======
        "http://api:8000/predict",
>>>>>>> 3484937c944dda464e8e498c4aea9791a8956c7c
        params={"age": age, "income": income, "credit_score": credit_score},
    )
    st.write(res.json())

