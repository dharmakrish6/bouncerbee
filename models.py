from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    age = Column(String)
    location = Column(String)

class Bouncer(Base):
    __tablename__ = 'bouncers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    age=Column(String)
    height=Column(String)
    weight=Column(String)
    experience=Column(String)
    city=Column(String)