# Biblioteca Universitaria — API REST con FastAPI

**Actividad 1 | Backend con FastAPI**
Estructuras de Datos y Algoritmos 1 — Universidad Autónoma de Occidente

---

## Integrantes

| Nombre completo | Código |
|---|---|
| Carlos Andrés Aristizabal Hernandez | 2230750 |


---

## Descripción

API REST desarrollada con **FastAPI** para la gestión del catálogo de libros de una biblioteca universitaria. Permite registrar, consultar, actualizar y eliminar libros, además de gestionar préstamos de ejemplares. La API incluye validaciones con Pydantic y documentación automática con Swagger.

---

## Persistencia de datos

Se utiliza **SQLite** como base de datos a través de **SQLAlchemy**. El archivo `libros.db` se genera automáticamente al iniciar el servidor en la raíz del proyecto. Esta decisión permite persistencia real entre reinicios sin requerir instalación de un motor de base de datos externo.

---

## Estructura del proyecto

```
app/
├── main.py                # Punto de entrada, instancia FastAPI
├── database.py            # Configuración de SQLite y SQLAlchemy
├── models/
│   ├── libro_create.py    # Schema de entrada con validaciones Pydantic
│   ├── libro_response.py  # Schema de salida
│   └── libro_db.py        # Modelo ORM (tabla en base de datos)
└── routers/
    └── libros.py          # Endpoints de la API
```

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/biblioteca-fastapi.git
cd biblioteca-fastapi
```

### 2. Crear entorno virtual

```bash
python -m venv .venv

# Linux / Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

La API queda disponible en: `http://localhost:8000`
Documentación Swagger: `http://localhost:8000/docs`

> La base de datos `libros.db` se crea automáticamente al iniciar por primera vez.

---

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/libros/` | Registrar un nuevo libro |
| `GET` | `/libros/` | Listar todos los libros |
| `GET` | `/libros/{id}` | Consultar un libro por ID |
| `PUT` | `/libros/{id}` | Actualizar un libro existente |
| `DELETE` | `/libros/{id}` | Eliminar un libro |
| `POST` | `/libros/{id}/prestar` | Registrar el préstamo de un ejemplar |

---

## Ejemplos de uso

### Crear un libro — `POST /libros/`

**Request:**
```json
{
  "titulo": "Cien años de soledad",
  "autor": "Gabriel García Márquez",
  "categoria": "Novela",
  "anio_publicacion": 1967,
  "total_ejemplares": 5
}
```

**Response `201`:**
```json
{
  "id": 1,
  "titulo": "Cien años de soledad",
  "autor": "Gabriel García Márquez",
  "categoria": "Novela",
  "anio_publicacion": 1967,
  "total_ejemplares": 5,
  "ejemplares_disponibles": 5
}
```

> `ejemplares_disponibles` se asigna automáticamente igual a `total_ejemplares` al crear.

---

### Listar todos los libros — `GET /libros/`

**Response `200`:**
```json
[
  {
    "id": 1,
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "categoria": "Novela",
    "anio_publicacion": 1967,
    "total_ejemplares": 5,
    "ejemplares_disponibles": 4
  }
]
```

---

### Actualizar un libro — `PUT /libros/1`

**Request:**
```json
{
  "titulo": "Cien años de soledad",
  "autor": "Gabriel García Márquez",
  "categoria": "Novela",
  "anio_publicacion": 1967,
  "total_ejemplares": 8
}
```

**Response `200`:** devuelve el libro actualizado. Los ejemplares prestados se conservan y los disponibles se recalculan automáticamente.

---

### Prestar un libro — `POST /libros/1/prestar`

**Response `200`:**
```json
{
  "message": "Libro prestado correctamente"
}
```

**Response `400` (sin ejemplares disponibles):**
```json
{
  "detail": "No hay ejemplares disponibles para prestamo"
}
```

**Response `404` (libro no existe):**
```json
{
  "detail": "libro no encontrado"
}
```

---

### Eliminar un libro — `DELETE /libros/1`

**Response `200`:**
```json
{
  "message": "Libro eliminado correctamente"
}
```

---

##  Validaciones implementadas

- `titulo`, `autor` y `categoria` no pueden estar vacíos ni contener solo espacios
- `anio_publicacion` no puede ser mayor al año actual ni negativo
- `total_ejemplares` debe ser mayor a 0
- Al actualizar, `total_ejemplares` no puede ser menor que los ejemplares actualmente prestados
- No se puede registrar un préstamo si `ejemplares_disponibles` es 0
- Se retorna `404` con mensaje claro si el libro no existe

---

##  Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Uvicorn](https://www.uvicorn.org/)
- Python 3.11+