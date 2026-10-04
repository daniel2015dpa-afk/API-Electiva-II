from pydantic import BaseModel
from typing import Optional


class Modulos_x_roles(BaseModel):
    id_modulo_rol: Optional[int] = None
    id_modulo: int
    id_rol: int
    puede_ver: bool
    puede_crear: bool
    puede_actualizar: bool
    puede_eliminar: bool