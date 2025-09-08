import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

# ---- Train model quickly or load ----
try:
    model = joblib.load("dropout_model.pkl")
except:
    # Fake dataset for demo
    data = pd.DataFrame({
        "attendance": [80, 60, 95, 50],
        "gpa": [3.5, 2.0, 3.9, 1.8],
        "financial_stress": [2, 8, 1, 9],
        "dropout": [0, 1, 0, 1]
    })
    X = data.drop("dropout", axis=1)
    y = data["dropout"]

    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, "dropout_model.pkl")

# ---- Streamlit UI ----
st.title("🎓 AI-Based Dropout Prediction & Counseling System")

attendance = st.slider("Attendance %", 0, 100, 75)
gpa = st.slider("GPA", 0.0, 4.0, 3.0)
stress = st.slider("Financial Stress (1-10)", 1, 10, 5)

if st.button("Predict"):
    features = np.array([[attendance, gpa, stress]])
    prob = model.predict_proba(features)[0][1]  # dropout probability
    risk = "High" if prob > 0.7 else "Medium" if prob > 0.4 else "Low"

    recommendation = {
        "High": "⚠️ Meet with counselor for academic guidance.",
        "Medium": "📘 Focus on time management and mentorship.",
        "Low": "✅ Keep up your good performance!"
    }[risk]

    st.subheader(f"Dropout Probability: {round(prob, 2)}")
    st.subheader(f"Risk Level: {risk}")
    st.success(recommendation)
