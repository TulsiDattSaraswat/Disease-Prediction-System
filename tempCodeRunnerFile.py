@app.route('/predict', methods=['POST'])
def predict():
    symptoms = [int(x) for x in request.form.values()]
    df = pd.DataFrame([symptoms])
    result = model.predict(df)[0]
    return render_template("index.html", prediction_text=f"Predicted Disease: {result}")