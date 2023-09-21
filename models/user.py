#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship('Place', cascade='all, delete-orphan',
                              backref='user')
        reviews = relationship('Review', cascade='all, delete-orphan',
                               backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""


-------------------------------------------------------------------------------------------------------------------------------
setup_mysql_dev.sql (this will be in the base folder, where README.md, console.py and AUTHORS.MD is located)
-- Create Database and grant permission to User

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT USAGE ON * . *
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON `performance_schema`.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;


--------------------------------------------------------------------------------------------------------------------------------
setup_mysql_test.sql (same as above)
-- Create Database and grant permission for test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT USAGE ON *.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON `performance_schema`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
