#!/usr/bin/python3
# myapp/models/__init__.py
"""
initialize the models package
"""
from models.engine.db_storage import DBStorage

storage = DBStorage()

storage.reload()
