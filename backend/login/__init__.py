"""Login Project
"""

from flask import Flask
from flask import Blueprint, current_app, g
from flask_cors import CORS
import redis
from . import models
from . import decorators
from . import exceptions
from .config import get_config
from .resources import user_api, admin_api


def create_app(config_name):
    """Function factory for application
    Parameters:
    -----------
    config_path: str, relative path for config file, base is working directory

    Return:
    -------
    application: object, WSGI object
    """
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    user_bp = Blueprint("user_bp", __name__)
    user_api.init_app(user_bp)
    admin_bp = Blueprint("admin_bp", __name__)
    admin_api.init_app(admin_bp)

    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    models.db.init_app(app)

    @app.before_first_request
    def on_startup():
        cache = redis.Redis(
            host=app.config['REDIS_HOST'],
            port=app.config['REDIS_PORT'],
            db=app.config['REDIS_DB'],
        )

        setattr(g, 'cache', cache)


    CORS(app)

    return app
