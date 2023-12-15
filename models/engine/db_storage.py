#!/usr/bin/python3
"""
    File to manage storage using implementations from SQL
"""
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage():
    """Class definition and attributes"""
    __engine = None
    __session = None

    def __init__(self):
        """__init__"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the specified cls (All if cls is None)"""
        dic = {}
        if cls is None:
            for i in dict_class.values():
                for j in self.__session.query(i).all():
                    key = type(j).__name__ + "." + j.id
                    dic[key] = j
        else:
            for j in self.__session.query(cls).all():
                key = type(j).__name__ + "." + j.id
                dic[key] = j
        return dic

    def new(self, obj):
        """The way to add a new object"""
        self.__session.add(obj)

    def save(self):
        """Saves the changes of the files"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the specified object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all the tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        self.__session.close()
