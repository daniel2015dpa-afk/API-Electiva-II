from fastapi import APIRouter, HTTPException
from app.models.evaluaciones_finales import EvaluacionesFinales
from app.repositories.evaluaciones_finales_repo import EvaluacionesFinalesRepository


router = APIRouter( prefix="/evaluacionesfinales", tags=["Gestión de evaluaciones finales"])
repo = EvaluacionesFinalesRepository()

@router.get("/")
def listar_evaluaciones():
    return repo.obtener_todos()

@router.get("/{id_evaluacion}")
def obtener_evaluacion(id_evaluacion: int):
    evaluacion = repo.obtener_por_id(id_evaluacion)

    if not evaluacion:
        raise HTTPException(
            status_code=404,
            detail="Evaluación no encontrada"
        )

    return evaluacion


@router.post("/")
def crear_evaluacion(evaluacion: EvaluacionesFinales):
    nuevo_id = repo.crear(evaluacion)

    return {
        "mensaje": "Evaluación registrada exitosamente",
        "id": nuevo_id
    }

@router.delete("/{id_evaluacion}")
def eliminar_evaluacion(id_evaluacion: int):
    exito = repo.eliminar(id_evaluacion)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Evaluación no encontrada"
        )

    return {
        "mensaje": "Evaluación eliminada correctamente"
    }

@router.put("/{id_evaluacion}")
def actualizar_evaluacion(
    id_evaluacion: int,
    evaluacion: EvaluacionesFinales
):
    exito = repo.actualizar(
        id_evaluacion,
        evaluacion
    )

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Evaluación no encontrada"
        )

    return {
        "mensaje": "Evaluación actualizada correctamente"
    }
