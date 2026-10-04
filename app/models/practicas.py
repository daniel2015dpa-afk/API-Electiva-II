from pydantic import BaseModel
from typing import Optional
from datetime import date


class Practicas(BaseModel):
    id_practica: Optional[int] = None
    id_postulacion: int
    id_tutor: int
    fecha_inicio: date
    fecha_fin: date
    horas_requeridas: int
    horas_completadas: int
    objetivo: str
    estado: str
