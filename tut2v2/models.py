# from pydantic import BaseModel


# class User(BaseModel):
#     name: str
#     age: int

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# SQLAlchemy User model with auto-incrementing ID
class UserDB(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Pydantic model for request validation
class User(BaseModel):
    name: str
    age: int
