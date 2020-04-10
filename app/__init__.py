from flask import Flask
from flask_mongoengine import MongoEngine
from . import config

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevConfig)

    db.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.bot import routes
    from app.data import scrapping
    app.register_blueprint(routes.bot_bp)
    app.register_blueprint(scrapping.scrap_bp)