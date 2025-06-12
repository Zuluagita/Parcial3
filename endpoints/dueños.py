from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import dueños
from operations import DueñoCreate, DueñoUpdate, DueñoOut

router = APIRouter()

@router.post("/", response_model=DueñoOut, status_code=201)
def crear_desarrollador(data: DueñoCreate, db: Session = Depends(get_db)):
    nuevo = dueños(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[DueñoOut])
def listar_desarrolladores(db: Session = Depends(get_db)):
    return db.query(dueños).filter(dueños.estado == True).all()

@router.get("/{dueño_id}", response_model=DueñoOut)
def obtener_desarrollador(dueño_id: int, db: Session = Depends(get_db)):
    dev = db.query(dueños).get(dueño_id)
    if not dev or not dev.estado:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    return dev

@router.put("/{dueño_id}", response_model=DueñoOut)
def actualizar_desarrollador(dueño_id: int, data: DueñoUpdate, db: Session = Depends(get_db)):
    dev = db.query(dueños).get(dueño_id)
    if not dev or not dev.estado:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(dev, key, value)
    db.commit()
    db.refresh(dev)
    return dev

@router.delete("/{dueño_id}", status_code=204)
def eliminar_desarrollador(dueño_id: int, db: Session = Depends(get_db)):
    dev = db.query(dueños).get(dueño_id)
    if not dev or not dev.estado:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    dev.estado = False
    db.commit()
