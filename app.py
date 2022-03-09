from dotenv import load_dotenv
import os
from flask import Flask, Blueprint
from api.endpoints.user import user_ns
from api.api import api
from database import db

load_dotenv()

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(user_ns)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


def main():
    initialize_app(app)
    app.run()


if __name__ == "__main__":
    main()

