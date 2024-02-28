#!/usr/bin/python3
""" holds class Review"""
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from models.base_model import BaseModel, Base

"""Class Review"""

review_user = Table('review_user', Base.metadata,
                    Column('user_id', Integer,
                           ForeignKey('user.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True),
                    Column('review_id', Integer,
                           ForeignKey('review.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True))


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    content = Column(String(450), nullable=False)
    score = Column(Integer, nullable=False)
