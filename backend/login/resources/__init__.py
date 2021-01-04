"""API resources
"""

from flask_restful import Api
from .user._session import Session
from .user._user import User
from .user._password import Password


user_api = Api()
admin_api = Api()

user_api.add_resource(User, "/user")
user_api.add_resource(Session, "/session")
user_api.add_resource(Password, "/password/reset")

__all__ = ["user_api", "admin_api"]
