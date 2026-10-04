from pydantic import BaseModel
from typing import Optional


class Roles(BaseModel):
    id_rol: Optional[int] = None
    nombre: str
    descripcion: str
