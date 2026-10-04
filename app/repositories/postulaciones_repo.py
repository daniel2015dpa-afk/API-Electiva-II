from app.core.database import Database
from app.models.postulaciones import Postulaciones

class PostulacionesRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM postulaciones
                ORDER BY id_postulacion ASC
                """
                )
            postulaciones = cursor.fetchall()

            cursor.close()
            conn.close()

            return postulaciones
        except Exception as e:
            raise Exception(f"Error al obtener las postulaciones: {e}")

    def obtener_por_id(self, id_postulacion: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM postulaciones
                WHERE id_postulacion = %s
                """,
                (id_postulacion,)
                )

            postulacion = cursor.fetchone()

            cursor.close()
            conn.close()
            return postulacion
        except Exception as e:
            raise Exception(f"Error al obtener la postulacion: {e}")
        

    def crear(self, postulacion: Postulaciones):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO postulaciones
                (
                    id_estudiante,
                    id_puesto,
                    fecha_postulacion,
                    estado,
                    comentarios
                    )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id_postulacion;
                """

            cursor.execute(
                query,
                (
                    postulacion.id_estudiante,
                    postulacion.id_puesto,
                    postulacion.fecha_postulacion,
                    postulacion.estado,
                    postulacion.comentarios
                    )
                    )

            nuevo_id = cursor.fetchone()["id_postulacion"]
            conn.commit()

            cursor.close()
            conn.close()

            return nuevo_id
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            raise Exception(f"Error al crear la postulacion: {e}")

    def eliminar(self, id_postulacion: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM postulaciones
                WHERE id_postulacion = %s
                RETURNING id_postulacion;
                """,
                (id_postulacion,)
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
            raise Exception(f"Error al crear la practica: {e}")

    def actualizar(self, id_postulacion: int, postulacion: Postulaciones):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                UPDATE postulaciones
                SET
                    id_estudiante = %s,
                    id_puesto = %s,
                    fecha_postulacion = %s,
                    estado = %s,
                    comentarios = %s
                    WHERE id_postulacion = %s
                    RETURNING id_postulacion;
                    """

            cursor.execute(
                query,
                (
                    postulacion.id_estudiante,
                    postulacion.id_puesto,
                    postulacion.fecha_postulacion,
                    postulacion.estado,
                    postulacion.comentarios,
                    id_postulacion
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
            raise Exception(f"Error al crear la practica: {e}")
