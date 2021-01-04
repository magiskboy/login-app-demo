"""Session resource
"""

import secrets
import jwt
from flask import current_app, g
from flask_restful import Resource
from login import models
from login import decorators
from login import exceptions


class Session(Resource):
    @decorators.exception_handler
    @decorators.parameter("username", str, "json", True)
    @decorators.parameter("password", str, "json", True)
    def post(self, username, password, *args, **kwargs):
        """Login task
        """
        user = models.User.find_by([("username", username)], find_one=True)
        if user is None:
            raise exceptions.AuthorizationError("username is invalid")
        if not user.verify_password(password):
            raise exceptions.AuthorizationError("Password is invalid")
        data = {
            "username": user.username,
            "email": user.email
        }
        access_token = jwt.encode(
            data,
            current_app.config['SECRET_KEY'],
           current_app.config['JWT_ALGORITHMS'],
        )
        refresh_token = secrets.token_urlsafe(32)
        g.cache.set(refresh_token, user.id)
        user.is_login = True
        user.save()
        rv = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        return rv

    @decorators.exception_handler
    @decorators.parameter("refresh_token", str, "json", True)
    def put(self, refresh_token, *args, **kwargs):
        cache = g.cache
        if store.exists(refresh_token):
            user_id = cache.get(refresh_token)
            user = models.User.find_by([("id", user_id)])
            if user.is_login:
                cache.delete(refresh_token)
                refresh_token = secrets.token_urlsafe(8)
                payload = {
                    "username": user.username,
                    "email": user.email
                }
                cache.set(refresh_token, user.id)
                access_token = jwt.encode(
                    payload,
                    current_app.config['SECRET_KEY'],
                    current_app.config['JWT_ALGORITHMS'],
                ).decode("utf-8")
                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
            else:
                raise exceptions.AuthorizationError("User logout")
        else:
            raise exceptions.AuthorizationError("Refresh token invalid")

    @decorators.exception_handler
    @decorators.required_authenticate
    def delete(self, *args, **kwargs):
        """Logout task
        """
        email = kwargs["user_detail"]["email"]
        user = models.User.find_by([("email", email)], find_one=True)
        if user is None:
            raise exceptions.AuthorizationError("Session is not exist")
        user.is_login = False
        user.save()

        # Don't delete refresh token in redis

        rv = {
            "message": "Logout success"
        }
        return rv
