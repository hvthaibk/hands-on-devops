from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Display Hello, Docker!"""
    return "Hello, Docker!!!"


if __name__ == "__main__":
    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
