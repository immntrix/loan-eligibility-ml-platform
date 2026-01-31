import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "age": [25, 40, 35, 28, 50, 23, 33, 45],
    "income": [5, 10, 7, 6, 12, 4, 8, 11],
    "credit_score": [650, 700, 680, 690, 720, 640, 710, 730],
    "approved": [0, 1, 1, 0, 1, 0, 1, 1],
}

df = pd.DataFrame(data)
X = df[["age", "income", "credit_score"]]
y = df["approved"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "models/model.joblib")
print("Model saved!")
