"""Config flask app
"""

import os
import secrets


class BaseConfig:
    BASEDIR = os.getcwd()

    SECRET_KEY = secrets.token_hex(16)

    JWT_ALGORITHMS = os.getenv('JWT_ALGORITHMS', 'HS256')

    DEBUG = False

    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

    REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))

    REDIS_DB = int(os.getenv('REDIS_DB', '0'))


class TestingConfig(BaseConfig):
    DEBUG = False

    TESTING = True

    SQLALCHEMY_DATABASE_URI = os.getenv(
            'SQLALCHEMY_DATABASE_URI',
            'sqlite:///:memory:',
        )


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    TESTING = False


class ProductionConfig(BaseConfig):
    pass


def get_config(config_name):
    return {
        'production': ProductionConfig,
        'development': DevelopmentConfig,
        'testing': TestingConfig,
    }.get(config_name)
