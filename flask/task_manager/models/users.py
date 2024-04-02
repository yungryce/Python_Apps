# models.py
from models.base_model import BaseModel
from sqlalchemy import Column, String


# Define your database models
class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None, username=None):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'