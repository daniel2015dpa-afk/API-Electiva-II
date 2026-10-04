from fastapi import APIRouter, HTTPException
from app.models.practicas import Practicas
from app.repositories.practicas_repo import PracticasRepository

router = APIRouter(prefix="/practica", tags=["Gestión de práctica"])
repo = PracticasRepository()

@router.get("/")
def listar_practicas():
    return repo.obtener_todos()

@router.get("/{id_practica}")
def obtener_practica(id_practica: int):
    practica = repo.obtener_por_id(id_practica)
    if not practica:
        raise HTTPException(status_code=404, detail="Practica no encontrada")
    return practica

@router.post("/")
def crear_practica(practica: Practicas):
    nuevo_id = repo.crear(practica)
    return {"mensaje": "Practica registrada exitosamente", "id": nuevo_id}

@router.delete("/{id_practica}")
def eliminar_practica(id_practica: int):
    exito = repo.eliminar(id_practica)
    if not exito:
        raise HTTPException(status_code=404, detail="Practica no encontrada")
    return {"mensaje": "Practica eliminada correctamente"}

@router.put("/{id_practica}")
def actualizar_practica(id_practica: int, practica: Practicas):

    exito = repo.actualizar(id_practica, practica)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Practica no encontrada"
        )

    return {"mensaje": "Practica actualizada correctamente"}