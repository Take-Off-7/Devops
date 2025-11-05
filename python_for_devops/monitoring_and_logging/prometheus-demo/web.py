from flask import Flask, Response
import prometheus_client
from prometheus_client import Counter, Histogram
import random
import time


app = Flask("prometheus-app")

REQUESTS = Counter(
    'requests', 'Application Request Count', ['endpoint']
)
TIMER = Histogram(
    'slow', 'Slow Requests', ['endpoint']
)

@app.route('/')
def index():
    REQUESTS.labels(endpoint='/').inc()
    return '<h1>Development Prometheus-backed Flask App</h1>'

@app.route('/database/')
def database():
    with TIMER.labels(endpoint='/database').time():
        time.sleep(random.uniform(1, 3))
    return '<h1>Completed expensive database operations</h1>'

@app.route('/metrics/')
def metrics():
    return Response(
        prometheus_client.generate_latest(),
        mimetype='text/plain; version=0.0.4; charset=utf-8'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
