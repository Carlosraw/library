from sqlalchemy import Column, Integer, String
from app.database import Base

class LibroDB(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    autor = Column(String)
    categoria = Column(String)
    anio_publicacion = Column(Integer)
    total_ejemplares = Column(Integer)
    ejemplares_disponibles = Column(Integer)