from dynaconf import FlaskDynaconf
from flask import Flask

from app.configs import config_db


def create_app(env='development'):

    app = Flask(__name__)
    FlaskDynaconf(app, settings_files=["settings.toml", ".secrets.toml"], ENV_FOR_DYNACONF=env)

    # app.register_blueprint(bp_commands)
    # app.register_blueprint(bp_status)

    config_db(app)

    return app
