
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "DevOps Lab – CA-I is running successfully!"

@app.route("/health")
def health():
    return "Healthy"

@app.route("/error")
def error():
    return "Test error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
