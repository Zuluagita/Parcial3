from pydantic import BaseModel

# ----- MODELO VIDEOJUEGO -----
class   MascotaBase(BaseModel):
    nombre: str
    raza: str | None = None
    edad: float | None = None
    dueño_id: int | None = None


class MascotaCreate(MascotaBase):
    pass

class MascotaUpdate(MascotaBase):
    pass

class DueñoOut(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: str | None = None


    class Config:
        from_attributes = True

class MascotaOut(MascotaBase):
    id: int
    dueño: DueñoOut | None = None

    class Config:
        from_attributes = True

# ----- MODELO DESARROLLADOR -----
class DueñoBase(BaseModel):
    nombre: str
    tipo: str
    pais: str | None = None
    fundacion: int | None = None

class DueñoCreate(DueñoBase):
    pass

class DueñoUpdate(DueñoBase):
    pass