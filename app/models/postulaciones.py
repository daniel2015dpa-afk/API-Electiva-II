from pydantic import BaseModel
from typing import Optional
from datetime import date


class Postulaciones(BaseModel):
    id_postulaciones: Optional[int] = None
    id_estudiante: int
    id_puesto: int
    fecha_postulacion: date
    estado: str
    comentarios: str
    
