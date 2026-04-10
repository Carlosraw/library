from pydantic import BaseModel


class libro:
    titulo: str
    autor: str
    categoria: str
    anio_publicacion: int
    total_ejemplares: int
    ejemplares_disponibles: int
