"""User resource
"""

from flask_restful import Resource
from flask_restful import request
from sqlalchemy import exc
from login import decorators
from login import models
from login import exceptions


class User(Resource):
    @decorators.exception_handler
    @decorators.parameter("username", str, "json", True)
    @decorators.parameter("email", str, "json", True)
    @decorators.parameter("password", str, "json", True)
    def post(self, username, email, password, *args, **kwargs):
        """Register task
        """
        user = models.User.find_by([("email", email)], find_one=True)
        if user:
            raise exceptions.ActionError("User existed")
        user = models.User(username, email, password)
        user.save()
        return {"message": "success"}

    @decorators.exception_handler
    @decorators.required_authenticate
    @decorators.parameter("current_password", str, "json", True)
    @decorators.parameter("new_password", str, "json", True)
    def put(self, current_password, new_password, *args, **kwargs):
        """Set password
        """
        email = kwargs["user_detail"]["email"]
        user = models.User.find_by([("email", email)], find_one=True)
        if user is None:
            raise exceptions.ActionError("User not exist")
        if not user.verify_password(current_password):
            raise exceptions.ActionError("Current password is invalid")
        else:
            user.password = new_password
            user.save()
        return {"message": "success"}

    @decorators.exception_handler
    @decorators.required_authenticate
    def get(self, *args, **kwargs):
        email = kwargs["user_detail"]["email"]
        user = models.User.find_by([("email", email)], find_one=True)
        if user is None:
            raise exceptions.ActionError("User not exist")
        else:
            data_json = user.json
            rv = {
                "username": data_json["username"],
                "email": data_json["email"]
            }
            return rv
