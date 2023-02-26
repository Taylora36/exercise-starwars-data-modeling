import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    #These are all the properties of people in the SW universe
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer)
    is_bby = Column(Boolean)
    eye_color = Column(String(64))
    gender = Column(String(64))
    hair_color = Column(String(64))
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String(64))

    #These are things that people are related to (other than people)
    homeworld_id = Column(Integer, ForeignKey("planets.id"))
    starships_id = Column(Integer, ForeignKey("starships.id"))

    #This is just letting us know that things have changed.
    created = Column(DateTime, default=datetime.now)
    edited = Column(DateTime, default=None, onupdate=datetime.now)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(64))
    gravity = Column(String(64))
    terrain = Column(String(64))
    surface_water = Column(Integer)
    population = Column(Integer)
    residents = Column(Integer, ForeignKey("people.id"))
    films = ""
    created = Column(DateTime, default=datetime.now)
    edited = Column(DateTime, default=None, onupdate=datetime.now)

class Vehicles(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(64))
    vehicle_class = Column(String(64))
    pilots = Column(Integer, ForeignKey("people.id"))
    created = Column(DateTime, default=datetime.now)
    edited = Column(DateTime, default=None, onupdate=datetime.now)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(64))
    hyperdrive_rating = Column(Integer)
    MGLT = Column(Integer)
    starship_class = Column(String(64))
    pilots = Column(Integer, ForeignKey("people.id"))
    created = Column(DateTime, default=datetime.now)
    edited = Column(DateTime, default=None, onupdate=datetime.now)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
