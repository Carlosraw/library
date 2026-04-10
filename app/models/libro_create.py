from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


class LibroCreate(BaseModel):
    titulo: str
    autor: str
    categoria: str
    anio_publicacion: int
    total_ejemplares: int


    @field_validator("titulo")
    @classmethod
    def titulo_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El titulo no puede estar vacío")
        return v

    @field_validator("autor")
    @classmethod
    def autor_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El autor no puede estar vacío")
        return v

    @field_validator("categoria")
    @classmethod
    def  categoria_no_vacia(cls, v):
        if not v.strip():
            raise ValueError("La categoria no puede estar vacía")
        return v

    @field_validator("anio_publicacion")
    @classmethod
    def anio_valido(cls, v):
        if v > datetime.now().year:
            raise ValueError("El año no puede ser mayor al actual")
        if v < 0:
            raise ValueError("El año no puede ser negativo")
        return v

    @field_validator("total_ejemplares")
    @classmethod
    def total_valido(cls, v):
        if v <= 0:
            raise ValueError("Debe haber al menos un ejemplar")
        return v