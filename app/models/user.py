from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db.base import Base


class User(Base):
    """
    Tabela 'user' no banco de dados.
    """

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<User(email='{self.email}')>"
