from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("disease_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = [int(x) for x in request.form.values()]
    df = pd.DataFrame([symptoms])
    result = model.predict(df)[0]
    return render_template("index.html", prediction_text=f"Predicted Disease: {result}")

if __name__ == "__main__":
    app.run(debug=True)
