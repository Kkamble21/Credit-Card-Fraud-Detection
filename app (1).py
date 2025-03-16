from flask import Flask, request, jsonify
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["features"]
        prediction = model.predict([data])
        result = "Fraudulent" if prediction[0] == 1 else "Legitimate"
        return jsonify({"Fraud Prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
