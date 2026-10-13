from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.repositories.usuario_repo import UsuarioRepository

router = APIRouter(prefix="/auth", tags=["Autenticación"])

class LoginRequest(BaseModel):
    correo: str
    contraseña: str

@router.post("/login")
def login(credentials: LoginRequest):
    """
    Autentica un usuario y retorna su información básica.
    """
    repo = UsuarioRepository()
    usuario = repo.obtener_por_correo(credentials.correo)
    
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    if usuario.get('contraseña') != credentials.contraseña:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    if not usuario.get('estado'):
        raise HTTPException(status_code=403, detail="Usuario inactivo")
    
    return {
        "id_usuario": usuario.get('id_usuario'),
        "nombre": usuario.get('nombre'),
        "apellido": usuario.get('apellido'),
        "correo": usuario.get('correo'),
        "id_rol": usuario.get('id_rol'),
        "estado": usuario.get('estado')
    }