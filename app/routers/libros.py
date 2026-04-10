from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.database import SessionLocal

from app.models.libro_create import LibroCreate
from app.models.libro_response import LibroResponse
from app.models.libro_db import LibroDB

router = APIRouter(prefix="/libros", tags=["Libros"])

# dependencia db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST crear libro
@router.post("/", response_model=LibroResponse, status_code=201)
def crear_libro(libro:LibroCreate, db: Session = Depends(get_db)):

    db_libro = LibroDB(
        titulo=libro.titulo,
        autor=libro.autor,
        categoria=libro.categoria,
        anio_publicacion=libro.anio_publicacion,
        total_ejemplares=libro.total_ejemplares,
        ejemplares_disponibles=libro.total_ejemplares
    )

    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)

    return db_libro

# GET traer libros
@router.get("/", response_model=List[LibroResponse])
def listar_libros(db: Session = Depends(get_db)):
    libros = db.query(LibroDB).all()
    return libros

# GET traer libro por id
@router.get("/{id}", response_model=LibroResponse)
def obtener_libro(id:int, db: Session = Depends(get_db)):
    libro = db.query(LibroDB).filter(LibroDB.id == id).first()
    
    if not libro:
        raise HTTPException(status_code=404, detail="libro no encontrado")
    
    return libro