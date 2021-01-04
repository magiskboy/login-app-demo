"""Common decorators
"""

from functools import wraps
from flask import current_app
from flask import request
from flask_restful import reqparse
import jwt
from . import exceptions
from .models import User


def required_authenticate(func):
    """Check request authenticate
    """
    @wraps(func)
    def decorator(*args, **kwargs):
        if "Authorization" not in request.headers:
            raise exceptions.AuthorizationError("Token is missing")
        auth_type, token = request.headers['Authorization'].split(" ")
        if auth_type != "Bearer":
            raise exceptions.AuthorizationError(
                "Type of authorization is invalid"
            )
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], current_app.config['JWT_ALGORITHMS'])
        except jwt.exceptions.DecodeError as error:
            raise exceptions.AuthorizationError("Token is invalid")
        else:
            user = User.find_by([("email", data["email"])], find_one=True)
            if user is None:
                raise exceptions.ActionError("Token is valid")
            else:
                if not user.is_login:
                    raise exceptions.ActionError("Token is expired")
                else:
                    kwargs.update({"user_detail": data})
                    return func(*args, **kwargs)
    return decorator


def exception_handler(func):
    """Exception handler
    """
    @wraps(func)
    def decorator(*args, **kwargs):
        print('-------------')
        print(request.json)
        re_v = {}
        try:
            re_v = func(*args, **kwargs)
        except exceptions.BaseError as error:
            current_app.logger.error(str(error))
            re_v["message"] = str(error)
            return re_v, 401
        except Exception as error:
            current_app.logger.error(str(error))
            re_v["message"] = "Server error"
            return re_v, 401
        else:
            if isinstance(re_v, tuple):
                return re_v
            else:
                return re_v, 201
    return decorator


def parameter(name, type, location, required=False, default=None):
    """Add parameters for api
    """
    def decorator(endpoint_fn):
        @wraps(endpoint_fn)
        def wrapper(*args, **kwargs):
            if "parser" not in kwargs:
                parser = reqparse.RequestParser()
                kwargs.update({"parser": parser})
            # Check origin function or wrapped function
            kwargs["parser"].add_argument(name, type=type, location=location,
                                          required=required, default=default)
            if not hasattr(endpoint_fn, "__wrapped__"):
                _args = kwargs["parser"].parse_args()
                kwargs.pop("parser")
                kwargs.update(_args)
            return endpoint_fn(*args, **kwargs)
        return wrapper
    return decorator
