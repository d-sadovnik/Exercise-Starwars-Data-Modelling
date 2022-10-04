import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
  
    

class FavouritePlanets(Base):
    __tablename__ = 'favouriteplanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))

class FavouriteCharacters(Base):
    __tablename__ = 'favouritecharacters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column (Integer, ForeignKey('characters.id'))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    planet_climate = Column(String(250), nullable=False)
    planet_gravity = Column(String(250), nullable=False)
    planet_orbital_period = Column(Integer, primary_key=True)
    planet_population = Column(Integer, primary_key=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    character_gender = Column(String(250), nullable=False)
    character_skin_color = Column(String(250), nullable=False)
    character_birthdate = Column(String(250), nullable=False)
    character_eye_color = Column(String(250), nullable=False)


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')