from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("dropout_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array([[data["attendance"], data["gpa"], data["financial_stress"]]])
    prob = model.predict_proba(features)[0][1]  # dropout probability
    risk = "High" if prob > 0.7 else "Medium" if prob > 0.4 else "Low"

    recommendation = {
        "High": "Meet with counselor for academic guidance.",
        "Medium": "Focus on time management and mentorship.",
        "Low": "Keep up your good performance."
    }[risk]

    return jsonify({
        "dropout_probability": round(float(prob), 2),
        "risk_level": risk,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(debug=True)
