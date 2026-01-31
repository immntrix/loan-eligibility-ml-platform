from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("models/model.joblib")

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/predict")
def predict(age: int, income: int, credit_score: int):
    data = np.array([[age, income, credit_score]])
    prediction = model.predict(data)[0]
    return {"loan_approved": int(prediction)}

