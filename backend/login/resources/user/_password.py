"""Password resource
"""

from flask_restful import Resource
from login import decorators
from login import models
from login import exceptions


class Password(Resource):
    @decorators.exception_handler
    @decorators.parameter("username", str, "body", True)
    @decorators.parameter("email", str, "body", True)
    def post(self, username, email, *args, **kwargs):
        """Reset password
        """
        user = models.User.find_by(
            [("username", username), ("email", email)],
            find_one=True
        )
        if user is None:
            raise exceptions.ActionError("Detail is invalid")
        
        # Send email with new password
        rv = {"message": "success"}
        return rv
