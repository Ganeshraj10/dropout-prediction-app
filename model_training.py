import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Fake dataset (replace with real if available)
data = pd.DataFrame({
    "attendance": [80, 60, 95, 50],
    "gpa": [3.5, 2.0, 3.9, 1.8],
    "financial_stress": [2, 8, 1, 9],
    "dropout": [0, 1, 0, 1]
})

X = data.drop("dropout", axis=1)
y = data["dropout"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "dropout_model.pkl")
