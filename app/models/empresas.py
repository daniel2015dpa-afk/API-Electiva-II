from pydantic import BaseModel
from typing import Optional


class Empresas(BaseModel):
    id_empresa: Optional[int] = None 
    nombre: str
    identificacion_fiscal: str
    direccion: str
    telefono: str
    correo: str
    persona_contacto: str
    estado: str