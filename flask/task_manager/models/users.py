#!/usr/bin/python3
# models/user.py

from models.base_model import BaseModel
from sqlalchemy import Column, String

# Define the User model
class UserModel(BaseModel):
    """Model for the users table."""
    __tablename__ = 'users'

    # Define columns
    username = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None, username=None):
        """
        Initialize a new User instance.

        :param name: The user's name
        :param email: The user's email address
        :param username: The user's username
        """
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        """
        Return a string representation of the User instance.

        :return: String representation of the User instance
        """
        return f'<User {self.name!r}>'
    
    def to_json(self):
        """
        Serialize the User instance to a JSON-compatible dictionary.

        :return: Dictionary representation of the User instance
        """
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'email': self.email
        }
