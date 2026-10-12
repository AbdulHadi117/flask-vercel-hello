from flask import Flask, jsonify

# Expose this module-level application for Vercel's Flask detection.
app = Flask(__name__)


# Return a small JSON greeting to verify the root route.
@app.get("/")
def hello():
    return jsonify({"message": "Hello from Flask on Vercel"})


# Expose a simple health check for deployment smoke tests.
@app.get("/health")
def health():
    return jsonify({"status": "ok"})


# Return a fixed placeholder prediction without files or external services.
@app.get("/predict")
def predict():
    return jsonify({"churn_probability": 0.42, "note": "dummy value"})
