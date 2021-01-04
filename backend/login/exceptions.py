"""Define exception for app
"""

class BaseError(Exception):
    """BaseError for owner app
    """
    pass

class AuthorizationError(BaseError):
    """Error raise when authenticate error occur
    """
    pass


class ActionError(BaseError):
    """Error raise when error of normal action
    """
    pass
