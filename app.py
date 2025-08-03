from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)
model_path = "model/student_ridge_model.pkl"

if os.path.exists(model_path):
    model, scaler, features = joblib.load(model_path)
else:
    model = scaler = features = None

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST" and model:
        try:
            data = [
                float(request.form["studytime"]),
                float(request.form["failures"]),
                float(request.form["absences"]),
                float(request.form["G1"]),
                float(request.form["G2"])
            ]
            df = pd.DataFrame([data], columns=features)
            df_scaled = scaler.transform(df)
            prediction = model.predict(df_scaled)[0]
            result = f"Predicted Final Grade (G3): {round(prediction, 2)}"
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
