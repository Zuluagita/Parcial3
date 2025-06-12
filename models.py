from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class mascotas(Base):
    __tablename__ = "MASCOTAS"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    raza= Column(String)
    edad= Column(String)

class dueños(Base):
    __tablename__ = "DUEÑOS"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    telefono= Column(String)
    email= Column(String)

class vuelos(Base):
    __tablename__ = "VUELOS"
    id = Column(Integer, primary_key=True, index=True)
    fecha= Column(String)
    capacidad = Column(String)
    origen = Column(String)
    destino= Column(Boolean)

class reservas(Base):
    __tablename__ = "RESERVAS"
    id = Column(Integer, primary_key=True, index=True)
