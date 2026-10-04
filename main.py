from fastapi import FastAPI
from app.api import ruta_usuario, ruta_roles, ruta_puestos_practicas, ruta_practicas, ruta_postulaciones, ruta_modulos, ruta_modulos_x_roles, ruta_seguimiento_practicas, ruta_evaluaciones_finales,ruta_bitacoras_practicas,ruta_empresas

app = FastAPI(title="API de Seguimiento de Prácticas Profesionales ",
description="API REST para gestionar y monitorear las prácticas profesionales de los estudiantes, incluyendo usuarios, estudiantes, empresas y seguimiento de sus actividades.",
version="1.0.0")

app.include_router(ruta_usuario.router)
app.include_router(ruta_roles.router) 
app.include_router(ruta_puestos_practicas.router)
app.include_router(ruta_practicas.router)
app.include_router(ruta_postulaciones.router)
app.include_router(ruta_modulos.router)
app.include_router(ruta_modulos_x_roles.router)
app.include_router(ruta_seguimiento_practicas.router)
app.include_router(ruta_evaluaciones_finales.router)
app.include_router(ruta_bitacoras_practicas.router)
app.include_router(ruta_empresas.router)

@app.get("/")
def estado_api():
    return {"mensaje": "La API de monitoreo se encuentra en línea y funcional"}
