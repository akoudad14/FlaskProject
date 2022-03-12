
from dotenv import load_dotenv
from flask import Flask, Blueprint
import os

from api.endpoints.character import character_ns
from api.endpoints.comment import comment_ns
from api.endpoints.episode import episode_ns
from api.api import api
from database import db

load_dotenv()

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(episode_ns)
    api.add_namespace(character_ns)
    api.add_namespace(comment_ns)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


def main():
    initialize_app(app)
    app.run()


if __name__ == "__main__":
    main()
