"""Base model
"""

from sqlalchemy import exc
from flask import current_app
from . import db

class BaseModel():
    """Base model with some common method
    """
    __metadata__ = []

    def save(self):
        """Save model to db
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get(cls, id):
        """Get model by id
        Parameters:
        -----------
        id: int, id of object

        Returns:
        --------
        re_v: instance of model, None if not found
        """
        re_v = None
        try:
            re_v = cls.query.get(id)
        except exc.SQLAlchemyError as error:
            current_app.logger.error(f"Can't get instance of {cls.__name__} by id: {id}")
            current_app.logger.error(str(error))
        else:
            current_app.logger.info(f"Get instance of {cls.__name__} by id: {id}")
        finally:
            return re_v

    @property
    def json(self, force=True):
        """JSON parser for model
        Parameters:
        -----------
        force: bool, if True, skip any error, else False

        Returns:
        --------
        re_v: dict
        """
        try:
            re_v = {}
            for attr in self.__metadata__:
                if hasattr(self, attr):
                    re_v[attr] = getattr(self, attr)
                else:
                    if not force:
                        raise RuntimeError(f"Attrubute {attr} not in \
                                           {self.__class__.__name__} model")
        except RuntimeError as error:
            current_app.logger.error(str(error))
        else:
            return re_v

    @classmethod
    def find_by(cls, cond, find_one=False):
        """Search record with field and value"""
        kwargs = dict(cond)
        re_v = []
        try:
            if find_one:
                re_v = cls.query.filter_by(**kwargs).first()
            else:
                re_v = cls.query.filter_by(**kwargs)
        except exc.SQLAlchemyError as error:
            pass
        finally:
            return re_v

    @classmethod
    def all(cls):
        """Get all objects of model
        """
        return cls.query.all()
