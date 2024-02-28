#!/usr/bin/python3
""" holds class Quotes"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

quote_user = Table('quote_user', Base.metadata,
                   Column('user_id', Integer,
                          ForeignKey('user.id', onupdate='CASCADE',
                                     ondelete='CASCADE'),
                          primary_key=True),
                   Column('quote_id', Integer,
                          ForeignKey('quote.id', onupdate='CASCADE',
                                     ondelete='CASCADE'),
                          primary_key=True))

"""Class quotes"""


class Quote(BaseModel, Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    content = Column(String(300), nullable=False)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=False)
    visibility = Column(Boolean, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    modified_by = Column(String(45), nullable=False)
    deleted_by = Column(String(45), nullable=False)

    category_id = Column(Integer, ForeignKey('quotes_category.id'))
    category = relationship('QuoteCategory', back_populates='quotes')
