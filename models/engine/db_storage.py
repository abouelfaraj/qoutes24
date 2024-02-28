#!/usr/bin/python3
# db myapp/models/engine/storage.py
"""
Contains the class DBStorage
"""

from models.base_model import BaseModel, Base
from models.quote import Quote
from models.role import Role
from models.user_detail import UserDetail
from models.quote_category import QuoteCategory
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash

classes = {"Quote": Quote, "QuoteCategory": QuoteCategory,
           "Review": Review, "User": User, "Role": Role, "UserDetail": UserDetail}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        Q_MYSQL_USER = 'aef'
        Q_MYSQL_PWD = '123'
        Q_MYSQL_HOST = 'localhost'
        Q_MYSQL_DB = 'quotes_db'

        # Q_ENV = 'Q_ENV'
        # Q_MYSQL_USER = getenv('Q_MYSQL_USER')
        # Q_MYSQL_PWD = getenv('Q_MYSQL_PWD')
        # Q_MYSQL_HOST = getenv('Q_MYSQL_HOST')
        # Q_MYSQL_DB = getenv('Q_MYSQL_DB')
        # Q_ENV = getenv('Q_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(Q_MYSQL_USER,
                                             Q_MYSQL_PWD,
                                             Q_MYSQL_HOST,
                                             Q_MYSQL_DB))
        # if Q_ENV == "test":
        # Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or None if not
        found
        """
        objects = self.__session.query(classes[cls])
        for obj in objects:
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """
        Returns the number of objects in storage matching the given class name.
        If no name is passed, returns the count of all objects in storage.
        """
        nobjects = 0
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                nobjects += len(self.__session.query(classes[clss]).all())
        return nobjects

    def authenticate(self, cls, login, password):
        user = self.__session.query(
            classes[cls]).filter_by(login=login, password=password).first()
        if user:
            return user
        return None
