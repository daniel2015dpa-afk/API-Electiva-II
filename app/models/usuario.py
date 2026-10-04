from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    id_usuario: Optional[int] = None
    id_rol: Optional[int] = None
    nombre: str
    apellido: str
    edad: int
    celular: str
    direccion: str
    correo: str
    ciudad: str
    contraseña: str
    estado: bool

