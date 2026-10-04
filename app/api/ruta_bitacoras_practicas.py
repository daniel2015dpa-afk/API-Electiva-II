from fastapi import APIRouter, HTTPException
from app.models.bitacoras_practicas import Bitacoras_practicas
from app.repositories.bitacoras_practicas_repo import BitacorasPracticasRepository

router = APIRouter(
    prefix="/bitacoraspracticas",
    tags=["Gestión de bitácoras de prácticas"]
)

repo = BitacorasPracticasRepository()

@router.get("/")
def listar_bitacoras():
    return repo.obtener_todos()

@router.get("/{id_bitacora}")
def obtener_bitacora(id_bitacora: int):

    bitacora = repo.obtener_por_id(id_bitacora)

    if not bitacora:
        raise HTTPException(
            status_code=404,
            detail="Bitácora no encontrada"
        )

    return bitacora

@router.post("/")
def crear_bitacora(bitacora: Bitacoras_practicas):

    nuevo_id = repo.crear(bitacora)

    return {
        "mensaje": "Bitácora registrada exitosamente",
        "id": nuevo_id
    }

@router.delete("/{id_bitacora}")
def eliminar_bitacora(id_bitacora: int):

    exito = repo.eliminar(id_bitacora)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Bitácora no encontrada"
        )

    return {
        "mensaje": "Bitácora eliminada correctamente"
    }

@router.put("/{id_bitacora}")
def actualizar_bitacora(id_bitacora: int, bitacora: Bitacoras_practicas):

    exito = repo.actualizar( id_bitacora, bitacora)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Bitácora no encontrada"
        )

    return {
        "mensaje": "Bitácora actualizada correctamente"
    }

