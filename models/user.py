#!/usr/bin/python3
# myapp/models/user.py
""" holds class User"""

from models.base_model import Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

import hashlib
"""Class User inherit from BaseModel"""


class User(Base):
    """Representation of a user """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(128), nullable=False)
    password = Column(String(1000), nullable=False)
    status = Column(Boolean, nullable=False)

    role = relationship('Role', uselist=False, back_populates='user')

    # Define a one-to-one relationship with UserDetail
    user_detail = relationship(
        "UserDetail", uselist=False, back_populates="user")
