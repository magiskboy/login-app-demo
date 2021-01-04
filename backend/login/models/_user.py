"""User model
"""

from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db
from . import _base



class User(_base.BaseModel, db.Model):
    """User model
    """

    __tablename__ = "users"
    __metadata__ = ['username', 'email', 'create_at', 'update_at',
                    'is_login', 'is_admin', 'is_active', 'last_login']

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now())
    update_at = db.Column(db.DateTime, nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_login = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime, nullable=True)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self):
        """Protect attribute
        """
        raise AttributeError("This is a read only attribute")

    @password.setter
    def password(self, password):
        """Set password include hash raw password follow SHA256
        Parameters:
        -----------
        password: str, raw text
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Verify password
        Parameters:
        -----------
        password: str, raw password need verify

        Returns:
        --------
        rv: bool, True if password valid, else False
        """
        return check_password_hash(self.password_hash, password)

