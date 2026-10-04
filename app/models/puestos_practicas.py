from pydantic import BaseModel
from typing import Optional
from datetime import date


class Puestos_practica(BaseModel):
    id_puesto: Optional[int] = None
    id_empresa: int
    titulo: str
    descripcion: str
    requisitos: str
    area: str
    modalidad:str
    fecha_inicio: date
    fecha_fin: date
    estado: str
    cupos_disponibles: int

