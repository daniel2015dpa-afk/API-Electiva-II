from fastapi import APIRouter, HTTPException
from app.models.seguimiento_practicas import Seguimiento_practicas
from app.repositories.seguimiento_practicas_repo import Seguimiento_practicasRepository

router = APIRouter(prefix="/seguimiento_practicas", tags=["Gestión de seguimiento de prácticas"])
repo = Seguimiento_practicasRepository()

@router.get("/")
def listar_seguimiento():
    return repo.obtener_todos()

@router.get("/{id_seguimiento}")
def obtener_seguimiento(id_seguimiento: int):
    seguimiento_practicas = repo.obtener_por_id(id_seguimiento)
    if not seguimiento_practicas:
        raise HTTPException(status_code=404, detail="Seguimiento no encontrado")
    return seguimiento_practicas

@router.post("/")
def crear_seguimiento(seguimiento_practicas: Seguimiento_practicas):
    nuevo_id = repo.crear(seguimiento_practicas)
    return {"mensaje": "Seguimiento registrado exitosamente", "id": nuevo_id}

@router.delete("/{id_seguimiento}")
def eliminar_seguimiento(id_seguimiento: int):
    exito = repo.eliminar(id_seguimiento)
    if not exito:
        raise HTTPException(status_code=404, detail="Seguimiento no encontrado")
    return {"mensaje": "Seguimiento eliminado correctamente"}

@router.put("/{id_seguimiento}")
def actualizar_seguimiento(id_seguimiento: int, seguimiento_practicas: Seguimiento_practicas):

    exito = repo.actualizar(id_seguimiento, seguimiento_practicas)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Seguimiento no encontrado"
        )

    return {"mensaje": "Seguimiento actualizado correctamente"}