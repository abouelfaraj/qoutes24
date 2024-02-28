#!/usr/bin/python3
""" holds class Quotes user role"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


"""Class user role"""


class Role(BaseModel, Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='role')
