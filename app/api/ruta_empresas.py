from fastapi import APIRouter, HTTPException
from app.models.empresas import Empresas
from app.repositories.empresas_repo import EmpresasRepository

router = APIRouter( prefix="/empresas",tags=["Gestión de empresas"])

repo = EmpresasRepository()

@router.get("/")
def listar_empresas():
    return repo.obtener_todos()

@router.get("/{id_empresa}")
def obtener_empresa(id_empresa: int):
    empresa = repo.obtener_por_id(id_empresa)

    if not empresa:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return empresa


@router.post("/")
def crear_empresa(empresa: Empresas):
    nuevo_id = repo.crear(empresa)
    return {
        "mensaje": "Empresa registrada exitosamente",
        "id": nuevo_id
    }

@router.delete("/{id_empresa}")
def eliminar_empresa(id_empresa: int):

    exito = repo.eliminar(id_empresa)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return {
        "mensaje": "Empresa eliminada correctamente"
    }


@router.put("/{id_empresa}")
def actualizar_empresa(id_empresa: int,empresa: Empresas):
    exito = repo.actualizar(id_empresa,empresa)

    if not exito:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return {
        "mensaje": "Empresa actualizada correctamente"
    }

