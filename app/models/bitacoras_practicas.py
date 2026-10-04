from pydantic import BaseModel
from typing import Optional
from datetime import date

class Bitacoras_practicas(BaseModel):
    id_bitacora: Optional[int] = None 
    id_practica: int
    numero_semana: int
    fecha_inicio: date
    fecha_fin: date
    actividades: str
    logros: str
    dificultades: str
    horas_trabajadas: float
    comentarios_tutor: str
    estado: str 
    

