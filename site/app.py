from flask import Flask, render_template, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "DockerOps Dashboard")
APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        environment=APP_ENV,
        version=APP_VERSION,
        hostname=socket.gethostname(),
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "hostname": socket.gethostname()
    })


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION,
        "hostname": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
