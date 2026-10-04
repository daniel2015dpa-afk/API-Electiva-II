from pydantic import BaseModel
from typing import Optional
from datetime import date


class Seguimiento_practicas(BaseModel):
    id_seguimiento: Optional[int] = None
    id_practica: int
    id_tutor: Optional[int] = None
    id_evaluacion_final: Optional[int] = None
    fecha_seguimiento: date
    porcentaje_avance: float
    observaciones: str
    dificultades: str
    recomendaciones: str
    estado: str
    fecha_proximo_seguimiento: date
