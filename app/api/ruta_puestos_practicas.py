from fastapi import APIRouter, HTTPException
from app.models.puestos_practicas import Puestos_practica
from app.repositories.puestos_practicas_repo import Puestos_practicasRepository

router = APIRouter(prefix="/puestos_practica", tags=["Gestión de puestos de práctica"])
repo = Puestos_practicasRepository()

@router.get("/")
def listar_puesto():
    return repo.obtener_todos()

@router.get("/{id_puesto}")
def obtener_puesto(id_puesto: int):
    puesto_practica = repo.obtener_por_id(id_puesto)
    if not puesto_practica:
        raise HTTPException(status_code=404, detail="Puesto de practica no encontrado")
    return puesto_practica

@router.post("/")
def crear_puesto(puestos_practica: Puestos_practica):
    nuevo_id = repo.crear(puestos_practica)
    return {"mensaje": "Puesto registrado exitosamente", "id": nuevo_id}

@router.delete("/{id_puesto}")
def eliminar_puesto(id_puesto: int):
    exito = repo.eliminar(id_puesto)
    if not exito:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return {"mensaje": "Puesto eliminado correctamente"}

@router.put("/{id_puesto}")
def actualizar_puesto(id_puesto: int, puestos_practica: Puestos_practica):

    exito = repo.actualizar(id_puesto, puestos_practica)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Puesto no encontrado"
        )

    return {"mensaje": "Puesto actualizado correctamente"}
