from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class mascotas(Base):
    __tablename__ = "MASCOTAS"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    raza= Column(String)
    edad= Column(String)
    dueño_id = Column(Integer, ForeignKey("DUEÑOS.id"))
    estado = Column(Boolean, default=True)
dueños = relationship("dueños", back_populates="mascotas")
reservas = relationship("reservas", back_populates="mascotas")

class dueños(Base):
    __tablename__ = "DUEÑOS"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    telefono= Column(String)
    email= Column(String)
    estado = Column(Boolean, default=True)
mascotas = relationship("mascotas", back_populates="dueño")
reservas = relationship("reserva dueño_ids", back_populates="dueño")
class vuelos(Base):
    __tablename__ = "VUELOS"
    id = Column(Integer, primary_key=True, index=True)
    fecha= Column(String)
    capacidad = Column(String)
    origen = Column(String)
    destino= Column(Boolean)
    estado = Column(Boolean, default=True)
reservas = relationship("reservas", back_populates="vuelos")

class reservas(Base):
    __tablename__ = "RESERVAS"
    id = Column(Integer, primary_key=True, index=True)
    dueño_id = Column(Integer, ForeignKey("DUEÑOS.id"))
    mascotas_id = Column(Integer, ForeignKey("MASCOTAS.id"))
    vuelo_id = Column(Integer, ForeignKey("VUELOS.id"))
    estado = Column(Boolean, default=True)
mascotas = relationship("mascotas", back_populates="reservas")
dueños = relationship("dueños", back_populates="reservas")
vuelos = relationship("vuelos", back_populates="reservas")