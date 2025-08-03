
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import joblib
import os

df = pd.read_csv("data/processed/student_data.csv")

features = ["studytime", "failures", "absences", "G1", "G2"]
target = "G3"
X = df[features]
y = df[target]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump((model, scaler, features), "model/student_ridge_model.pkl")

print("✅ Ridge Regression model trained and saved.")
