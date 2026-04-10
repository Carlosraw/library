from pydantic import BaseModel

class LibroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    categoria: str
    anio_publicacion: int
    total_ejemplares: int
    ejemplares_disponibles: int

    class Config:
        from_attributes = True