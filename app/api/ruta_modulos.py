from fastapi import APIRouter, HTTPException
from app.models.modulos import Modulos
from app.repositories.modulos_repo import ModulosRepository

router = APIRouter(prefix="/modulos", tags=["Gestión de módulos"])
repo = ModulosRepository()

@router.get("/")
def listar_modulos():
    return repo.obtener_todos()

@router.get("/{id_modulo}")
def obtener_modulo(id_modulo: int):

    modulo = repo.obtener_por_id(id_modulo)

    if not modulo:
        raise HTTPException(
            status_code=404,
            detail="Módulo no encontrado"
        )

    return modulo

@router.post("/")
def crear_modulo(modulo: Modulos):

    nuevo_id = repo.crear(modulo)

    return {"mensaje": "Módulo registrado exitosamente","id": nuevo_id
    }

@router.delete("/{id_modulo}")
def eliminar_modulo(id_modulo: int):

    exito = repo.eliminar(id_modulo)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Módulo no encontrado"
        )

    return {
        "mensaje": "Módulo eliminado correctamente"
    }

@router.put("/{id_modulo}")
def actualizar_modulo(
    id_modulo: int,
    modulo: Modulos
):

    exito = repo.actualizar(
        id_modulo,
        modulo
    )

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Módulo no encontrado"
        )

    return {
        "mensaje": "Módulo actualizado correctamente"
    }

