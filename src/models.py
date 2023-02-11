import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    favorito_id = Column(Integer, ForeignKey('favorito.id'),
         nullable=False)
    favoritousuario = relationship('Favorito', backref='usuario', lazy=True)

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favoritoplaneta = relationship('Favorito', backref='planeta', lazy=True)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favoritopersonaje = relationship('Favorito', backref='personaje', lazy=True)

class Favorito(Base):
    __tablename__ = 'favorito'
    id= Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'),
         nullable=False) 
    personaje_id = Column(Integer, ForeignKey('personaje.id'),
        nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'),
        nullable=False)  
    

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')
