from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Book(BaseModel):
    __tablename__ = 'books'

    title = Column(String(255), nullable=False)
    publisher = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    is_available = Column(Boolean, default=True)
    borrowed_at = Column(DateTime, default=None)
    return_by = Column(DateTime, default=None)
    borrowed_by_id = Column(Integer, ForeignKey('users.id'))

    # Define a relationship with User
    borrower = relationship('User', backref='borrowed_books')

    def __repr__(self):
        return f'<Book {self.title}>'

    def to_dict(self):
        """
        Convert the book instance to a dictionary.

        :return: Dictionary representation of the book instance
        """
        data = super().to_dict()
        # Add the available_on field (borrowed_until) if not available
        if not self.is_available:
            data['available_on'] = self.borrowed_until.isoformat() if self.borrowed_until else None
        return data