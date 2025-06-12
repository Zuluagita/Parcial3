from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session, joinedload
from database import get_db
from models import mascotas
from operations import MascotaCreate, MascotaUpdate, MascotaOut

router = APIRouter()

@router.post("/", response_model=   MascotaOut, status_code=201)
def crear_videojuego(data: MascotaCreate, db: Session = Depends(get_db)):
    nuevo = mascotas(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[MascotaOut])
def listar_videojuegos(
    titulo: str | None = Query(None),
    genero: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(mascotas).options(joinedload(mascotas.dueño))
    query = query.filter(mascotas.estado == True)
    if titulo:
        query = query.filter(mascotas.nombre.ilike(f"%{titulo}%"))
    if genero:
        query = query.filter(mascotas.raza.ilike(f"%{genero}%"))
    return query.all()

@router.get("/{mascota_id}", response_model=MascotaOut)
def obtener_videojuego(mascota_id: int, db: Session = Depends(get_db)):
    mascota = db.query(mascotas).options(joinedload(mascotas.dueño)).get(mascota_id)
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrado")
    return mascota

@router.put("/{mascota_id}", response_model=MascotaOut)
def actualizar_videojuego(mascota_id: int, data: MascotaUpdate, db: Session = Depends(get_db)):
    mascota = db.query(mascotas).get(mascota_id)
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrado")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(mascota, key, value)
    db.commit()
    db.refresh(mascota)
    return mascota

@router.delete("/{mascota_id}", status_code=204)
def eliminar_videojuego(mascota_id: int, db: Session = Depends(get_db)):
    mascota = db.query(mascotas).get(mascota_id)
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    mascota.estado = False
    db.commit()
