from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Simple message"""
    return "Hello, Docker!!!\n"
