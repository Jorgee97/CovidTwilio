from flask import Flask
from flask_mongoengine import MongoEngine
from . import config
from app.data.task import scrap_every_day

db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevConfig)

    db.init_app(app)
    register_blueprints(app)

    scrap_every_day()

    return app


def register_blueprints(app):
    from app.bot import routes    
    app.register_blueprint(routes.bot_bp)

