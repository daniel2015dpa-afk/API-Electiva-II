from fastapi import APIRouter, HTTPException
from app.models.modulos_x_roles import Modulos_x_roles
from app.repositories.modulos_x_roles_repo import Modulos_x_rolesRepository

router = APIRouter(prefix="/modulos_x_roles", tags=["Gestión de Modulos y roles"])
repo = Modulos_x_rolesRepository()

@router.get("/")
def listar_modulo_rol():
    return repo.obtener_todos()

@router.get("/{id_modulo_rol}")
def obtener_modulos_roles(id_modulo_rol: int):
    modulos_x_roles = repo.obtener_por_id(id_modulo_rol)
    if not modulos_x_roles:
        raise HTTPException(status_code=404, detail="Modulo_x_rol no encontrado")
    return modulos_x_roles

@router.post("/")
def crear_modulo_rol(modulos_x_roles: Modulos_x_roles):
    nuevo_id = repo.crear(modulos_x_roles)
    return {"mensaje": "Modulo_x_rol registrado exitosamente", "id": nuevo_id}

@router.delete("/{id_modulo_rol}")
def eliminar_modulo_rol(id_modulo_rol: int):
    exito = repo.eliminar(id_modulo_rol)
    if not exito:
        raise HTTPException(status_code=404, detail="Modulo_x_rol no encontrado")
    return {"mensaje": "Modulo_x_rol eliminado correctamente"}

@router.put("/{id_modulo_rol}")
def actualizar_modulo_rol(id_modulo_rol: int, modulo_x_rol: Modulos_x_roles):

    exito = repo.actualizar(id_modulo_rol, modulo_x_rol)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Modulo_x_rol no encontrado"
        )

    return {"mensaje": "Modulo_x_rol actualizado correctamente"}
