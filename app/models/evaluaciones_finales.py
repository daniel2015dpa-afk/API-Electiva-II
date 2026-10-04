from pydantic import BaseModel
from typing import Optional
from datetime import date


class EvaluacionesFinales(BaseModel):
    id_evaluacion: Optional[int] = None
    id_seguimiento: int
    id_evaluador: int
    fecha_evaluacion: date
    resultado: str
    calificacion: float
    cumplimiento_objetivos: str
    desempeno: str
    fortalezas: str
    aspectos_mejora: str
    observaciones: str
    recomendaciones: str
