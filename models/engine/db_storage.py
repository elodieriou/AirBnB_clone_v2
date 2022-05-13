#!/usr/bin/python3
"""New engine DBStorage"""
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage:
    """The class defines all method to manage the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method: creation of the engine. All the tables
        are deleted if the environment variable is equal to test """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """All method: display all information about a specific class"""
        my_dict = {}
        my_list = []
        if cls is None:
            my_list += self.__session.query(State).all()
            my_list += self.__session.query(City).all()
            my_list += self.__session.query(User).all()
            my_list += self.__session.query(Place).all()
            my_list += self.__session.query(Review).all()
            my_list += self.__session.query(Amenity).all()
        else:
            my_list = self.__session.query(cls).all()

        for obj in my_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """New method: add the object to the session"""
        self.__session.add(obj)

    def save(self):
        """Save method: commit all changes to the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete method: delete an object from the session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload method: create all the table and the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close method: close or remove the session"""
        self.__session.close()
