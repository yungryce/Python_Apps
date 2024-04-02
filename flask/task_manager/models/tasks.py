from models.base_model import BaseModel
from sqlalchemy import Column, String, Boolean

class Task(BaseModel):
    __tablename__ = 'tasks'

    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    done = Column(Boolean, default=False)

    def __init__(self, title=None, description=None, done=False):
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return f'<Task title={self.title!r}, description={self.description!r}, done={self.done}>'