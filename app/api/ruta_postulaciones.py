from fastapi import APIRouter, HTTPException
from app.models.postulaciones import Postulaciones
from app.repositories.postulaciones_repo import PostulacionesRepository


router = APIRouter( prefix="/postulaciones", tags=["Gestión de postulaciones"])

repo = PostulacionesRepository()

@router.get("/")
def listar_postulaciones():
    return repo.obtener_todos()

@router.get("/{id_postulacion}")
def obtener_postulacion(id_postulacion: int):
    postulacion = repo.obtener_por_id(id_postulacion)

    if not postulacion:
        raise HTTPException(
            status_code=404,
            detail="Postulación no encontrada"
        )

    return postulacion

@router.post("/")
def crear_postulacion(postulacion: Postulaciones):

    nuevo_id = repo.crear(postulacion)

    return {
        "mensaje": "Postulación registrada exitosamente",
        "id": nuevo_id
    }

@router.delete("/{id_postulacion}")
def eliminar_postulacion(id_postulacion: int):

    exito = repo.eliminar(id_postulacion)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Postulación no encontrada"
        )

    return {
        "mensaje": "Postulación eliminada correctamente"
    }

@router.put("/{id_postulacion}")
def actualizar_postulacion(id_postulacion: int,postulacion: Postulaciones):

    exito = repo.actualizar( id_postulacion,postulacion)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Postulación no encontrada"
        )

    return {"mensaje": "Postulación actualizada correctamente"}

