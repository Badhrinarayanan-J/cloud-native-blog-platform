from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application":"Cloud Native Blogging Platform",
        "status":"Backend Running Successfully"
    }

@app.route("/health")
def health():
    return "Healthy"

app.run(host="0.0.0.0",port=5000)
