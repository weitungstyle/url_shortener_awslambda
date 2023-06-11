from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(UserMixin):
    def __init__(self, email, password, username="", is_admin=False):
        """To initiate the class."""
        self.email = email
        self.username = username
        self.password_hash = self.generate_password_hash(password)
        self.password = password
        self.is_admin = is_admin

    def generate_password_hash(self, password):
        """To generate password hash."""
        return generate_password_hash(password)

    def check_password(self, password):
        """To check password is correct."""
        return check_password_hash(self.password, password)

    def validator():
        pass
