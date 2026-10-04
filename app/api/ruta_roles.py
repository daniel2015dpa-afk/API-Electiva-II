from fastapi import APIRouter, HTTPException
from app.models.roles import Roles
from app.repositories.roles_repo import RolesRepository

router = APIRouter(prefix="/roles", tags=["Gestión de roles"])
repo = RolesRepository()

@router.get("/")
def listar_roles():
    return repo.obtener_todos()

@router.get("/{id_rol}")
def obtener_roles(id_rol: int):
    rol = repo.obtener_por_id(id_rol)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

@router.post("/")
def crear_rol(rol: Roles):
    nuevo_id = repo.crear(rol)
    return {"mensaje": "Rol registrado exitosamente", "id": nuevo_id}

@router.delete("/{id_rol}")
def eliminar_rol(id_rol: int):
    exito = repo.eliminar(id_rol)
    if not exito:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"mensaje": "Rol eliminado correctamente"}

@router.put("/{id_rol}")
def actualizar_rol(id_rol: int, rol: Roles):

    exito = repo.actualizar(id_rol, rol)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Rol no encontrado"
        )

    return {"mensaje": "Rol actualizado correctamente"}
