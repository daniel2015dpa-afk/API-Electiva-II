from pydantic import BaseModel
from typing import Optional



class Modulos(BaseModel):
    id_modulo: Optional[int] = None
    nombre: str
    descripcion: str

