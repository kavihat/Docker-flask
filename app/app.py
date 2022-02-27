"""A simple flask web app"""
from flask import Flask, render_template

from .controllers.about_controller import AboutController
from .controllers.index_controller import IndexController
from werkzeug.debug import DebuggedApplication


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
    return app

api = create_app()

@api.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@api.route("/about", methods=['GET'])
def about_get():
    return AboutController.get()
