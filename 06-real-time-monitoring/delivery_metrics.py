from flask import Flask, jsonify
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import random
import time

app = Flask(__name__)

total_deliveries = Counter(
    "delivery_total",
    "Total deliveries processed"
)
pending_deliveries = Gauge(
    "delivery_pending",
    "Current number of pending deliveries"
)
in_transit_deliveries = Gauge(
    "delivery_in_transit",
    "Current number of deliveries in transit"
)
delivery_time = Histogram(
    "delivery_time_seconds",
    "Delivery processing time in seconds"
)

@app.route("/")
def home():
    return jsonify({
        "message": "Delivery Operations Monitoring API",
        "metrics": "/metrics",
        "health": "/health"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/simulate")
def simulate():
    pending = random.randint(5, 100)
    in_transit = random.randint(10, 200)
    duration = random.uniform(1, 30)

    pending_deliveries.set(pending)
    in_transit_deliveries.set(in_transit)
    total_deliveries.inc()
    delivery_time.observe(duration)

    return jsonify({
        "pending_deliveries": pending,
        "in_transit_deliveries": in_transit,
        "delivery_time_seconds": round(duration, 2),
        "status": "metrics updated"
    })

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    "/metrics": make_wsgi_app()
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
