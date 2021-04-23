from flask import Flask,Blueprint
from .bookstore import bk
from .extentions import mongo

def create_app(config_file = 'settings.py'):
    app = Flask(__name__)
    app.config. from_pyfile(config_file)
    mongo.init_app(app)

    app.register_blueprint(bk)

    return app

from book import bookstore
if __name__ == "__main__":
    app.run(debug=True)