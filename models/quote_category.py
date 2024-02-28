#!/usr/bin/python3
""" holds class Quotes category"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

"""CLass quotes category"""


class QuoteCategory(BaseModel, Base):
    __tablename__ = 'quotes_category'

    id = Column(Integer, primary_key=True)
    title = Column(String(45), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(45), nullable=False)
    modified_at = Column(DateTime, nullable=False)
    modified_by = Column(String(45), nullable=False)
    deleted_by = Column(String(45), nullable=False)
    deleted_at = Column(DateTime, nullable=False)

    quotes = relationship('Quote', back_populates='category')
