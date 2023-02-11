import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    favorito_id = Column(Integer, ForeignKey('favorito.id'),
         nullable=False)
    favoritousuario = relationship('Favorito', backref='usuario', lazy=True)

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favoritoplaneta = relationship('Favorito', backref='planeta', lazy=True)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favoritopersonaje = relationship('Favorito', backref='personaje', lazy=True)

class Favorito(Base):
    __tablename__ = 'favorito'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'),
         nullable=False) 
    personaje_id = Column(Integer, ForeignKey('personaje.id'),
        nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'),
        nullable=False)  
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
