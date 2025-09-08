import streamlit as st
import requests

st.title("AI Dropout Prediction System")

attendance = st.slider("Attendance %", 0, 100, 75)
gpa = st.slider("GPA", 0.0, 4.0, 3.0)
stress = st.slider("Financial Stress (1-10)", 1, 10, 5)

if st.button("Predict"):
    response = requests.post("http://127.0.0.1:5000/predict", 
                             json={"attendance": attendance, "gpa": gpa, "financial_stress": stress})
    result = response.json()
    st.write("Dropout Probability:", result["dropout_probability"])
    st.write("Risk Level:", result["risk_level"])
    st.write("Recommendation:", result["recommendation"])
