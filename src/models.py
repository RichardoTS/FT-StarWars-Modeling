import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100))
    favorite_characters = relationship('People', secondary="favorite_characters")
    favorite_planets = relationship('Planet', secondary="favorite_planets")
    favorite_vehicles = relationship('Vehicle', secondary="favorite_vehicles")

class Favorite_characters(Base):
    __tablename__ = 'favorite_characters'
    character_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), primary_key=True)

class Favorite_planets(Base):
    __tablename__ = 'favorite_planets'
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), primary_key=True)

class favorite_vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    vechile_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), primary_key=True)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(10))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(200))
    gravity = Column(String(200))
    terrain = Column(String(200))
    surface_water = Column(String(200))
    population = Column(Integer)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    model = Column(String(200))
    manufacturer = Column(String(200))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(100))
    vehicle_class = Column(String(100))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
