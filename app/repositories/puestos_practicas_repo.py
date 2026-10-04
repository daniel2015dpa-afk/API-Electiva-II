from app.core.database import Database
from app.models.puestos_practicas import Puestos_practica


class Puestos_practicasRepository:

    def __init__(self):
        self.db = Database()

  
    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM puestos_practica
                ORDER BY id_puesto ASC
                """
                )
            puestos_practica = cursor.fetchall()

            cursor.close()
            conn.close()

            return puestos_practica

        except Exception as e:
             raise Exception(f"Error al obtener los puestos de practicas: {e}")

  
    def obtener_por_id(self, id_puesto: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM puestos_practica
                WHERE id_puesto = %s
                """,
                (id_puesto,)
                )
            puesto_practica = cursor.fetchone()

            cursor.close()
            conn.close()
            return puesto_practica

        except Exception as e:
              raise Exception(f"Error al obtener el puesto de practica : {e}")

   
    def crear(self, puestos_practica: Puestos_practica):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO puestos_practica
                (
                    id_empresa,
                    titulo,
                    descripcion,
                    requisitos,
                    area,
                    modalidad,
                    fecha_inicio,
                    fecha_fin,
                    cupos_disponibles,
                    estado
                    )
                    VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s
                    )
                    RETURNING id_puesto;
                    """

            cursor.execute(
                query,
                (
                    puestos_practica.id_empresa,
                    puestos_practica.titulo,
                    puestos_practica.descripcion,
                    puestos_practica.requisitos,
                    puestos_practica.area,
                    puestos_practica.modalidad,
                    puestos_practica.fecha_inicio,
                    puestos_practica.fecha_fin,
                    puestos_practica.cupos_disponibles,
                    puestos_practica.estado
                    )
                    )
            nuevo_id = cursor.fetchone()["id_puesto"]
            conn.commit()

            cursor.close()
            conn.close()

            return nuevo_id

        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            raise Exception(f"Error al crear el puesto de practica: {e}")

  
    def eliminar(self, id_puesto: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                 """
                 DELETE FROM puestos_practica
                 WHERE id_puesto = %s
                 RETURNING id_puesto;
                 """,
                 (id_puesto,)
                 )

            eliminado = cursor.fetchone()
            conn.commit()
            cursor.close() 
            conn.close()
            return eliminado is not None

        except Exception as e:
                    conn.rollback()
                    cursor.close()
                    conn.close()
                    raise Exception(f"Error al eliminar el puesto de practica: {e}")
        
    def actualizar(self,id_puesto: int,puestos_practica: Puestos_practica):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """ 
                UPDATE puestos_practica
                SET
                    titulo = %s,
                    descripcion = %s,
                    requisitos = %s,
                    area = %s,
                    modalidad = %s,
                    fecha_inicio = %s,
                    fecha_fin = %s,
                    cupos_disponibles = %s,
                    estado = %s
                    WHERE id_puesto = %s
                    RETURNING id_puesto;
                    """

            cursor.execute(
                query,
                (
                    puestos_practica.titulo,
                    puestos_practica.descripcion,
                    puestos_practica.requisitos,
                    puestos_practica.area,
                    puestos_practica.modalidad,
                    puestos_practica.fecha_inicio,
                    puestos_practica.fecha_fin,
                    puestos_practica.cupos_disponibles,
                    puestos_practica.estado,
                    id_puesto
                    )
                    )

            actualizado = cursor.fetchone()
            conn.commit()
            cursor.close()
            conn.close()

            return actualizado is not None
        
        except Exception as e:
                    conn.rollback()
                    cursor.close()
                    conn.close()
                    raise Exception(f"Error al actualizar el puesto de practica: {e}")
        

