"""models package
"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from ._user import User


__all__ = ["User"]
