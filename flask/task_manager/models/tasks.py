#!/usr/bin/python3
# models/task.py

from .base_model import BaseModel
from sqlalchemy import Column, String, Boolean, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship


task_user_association = Table('task_user_association', BaseModel.metadata,
    Column('task_id', String(36), ForeignKey('tasks.id')),
    Column('user_id', String(36), ForeignKey('users.id'))
)

class TaskModel(BaseModel):
    """Model for the tasks table."""
    __tablename__ = 'tasks'

    # Define columns
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    done = Column(Boolean, default=False)
    
    # Define relationship with users
    users = relationship("UserModel", secondary=task_user_association, back_populates="tasks")

    def __init__(self, title=None, description=None, done=False):
        """
        Initialize a new Task instance.

        :param title: The title of the task
        :param description: The description of the task
        :param done: Whether the task is done or not
        """
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        """
        Return a string representation of the Task instance.

        :return: String representation of the Task instance
        """
        return f'<Task title={self.title!r}, description={self.description!r}, done={self.done}>'
    
    def to_json(self):
        """
        Serialize the Task model instance attributes to a dictionary

        :return: Dictionary representation of the Task instance
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Import UserModel after it's defined
from .users import UserModel