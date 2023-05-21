import multiprocessing

from flask import Flask

from .mock import Mock
from .models import Article, Review, Video

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello"


def flask_thread(port):
    texts = Mock.create_mock("texts", Article)
    videos = Mock.create_mock("videos", Video)
    reviews = Mock.create_mock("reviews", Review)
    app.register_blueprint(texts)
    app.register_blueprint(videos)
    app.register_blueprint(reviews)
    app.run(host="0.0.0.0", port=port)


def start_mock_server():
    process = multiprocessing.Process(target=flask_thread, args=[3000], daemon=True)
    process.start()
    return process
