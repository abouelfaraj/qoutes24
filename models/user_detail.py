#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import Column, String, ForeignKey, Integer, Date, DateTime
from sqlalchemy.orm import relationship

"""Class of user details """


class UserDetail(BaseModel, Base):
    __tablename__ = 'user_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    email = Column(String(128), nullable=False)
    birthday = Column(Date, nullable=False)
    address = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    # Define a back reference to User
    user = relationship("User", back_populates="user_detail")
