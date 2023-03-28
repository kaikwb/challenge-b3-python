import threading

from flask import Flask

from .mock import create_mock

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello"


def flask_thread(port):
    texts = create_mock("texts")
    videos = create_mock("videos")
    reviews = create_mock("reviews")
    app.register_blueprint(texts)
    app.register_blueprint(videos)
    app.register_blueprint(reviews)
    app.run(host="0.0.0.0", port=port)


def start_mock_server():
    thread = threading.Thread(target=flask_thread, args=[3000], daemon=True)
    thread.start()
    return thread
