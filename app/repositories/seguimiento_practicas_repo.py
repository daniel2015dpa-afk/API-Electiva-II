from app.core.database import Database
from app.models.seguimiento_practicas import Seguimiento_practicas

class Seguimiento_practicasRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM seguimiento_practicas ORDER BY id_seguimiento ASC"
                )
            seguimiento_practicas = cursor.fetchall()

            cursor.close()
            conn.close()
            return seguimiento_practicas
        except Exception as e:
                    raise Exception(f"Error al obtener los seguimientos de las practicas: {e}")

    def obtener_por_id(self, id_seguimiento: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM seguimiento_practicas WHERE id_seguimiento = %s",
                (id_seguimiento,)
                )

            seguimiento_practicas = cursor.fetchone()

            cursor.close()
            conn.close()

            return seguimiento_practicas
        except Exception as e:
                    raise Exception(f"Error al obtener el seguimiento de la practica: {e}")
        

    def crear(self, seguimiento_practicas: Seguimiento_practicas):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO seguimiento_practicas
                (id_practica, id_tutor, id_evaluacion_final, fecha_seguimiento,
                porcentaje_avance, observaciones, dificultades, recomendaciones,
                fecha_proximo_seguimiento,estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                RETURNING id_seguimiento;
                """

            cursor.execute(
                query,
                (
                    seguimiento_practicas.id_practica,
                    seguimiento_practicas.id_tutor,
                    seguimiento_practicas.id_evaluacion_final,
                    seguimiento_practicas.fecha_seguimiento,
                    seguimiento_practicas.porcentaje_avance,
                    seguimiento_practicas.observaciones,
                    seguimiento_practicas.dificultades,
                    seguimiento_practicas.recomendaciones,
                    seguimiento_practicas.fecha_proximo_seguimiento,
                    seguimiento_practicas.estado
                    )
                    )

            nuevo_id = cursor.fetchone()["id_seguimiento"]

            conn.commit()

            cursor.close()
            conn.close()

            return nuevo_id

        except Exception as e:       
                    conn.rollback()
                    cursor.close()
                    conn.close()        
                    raise Exception(f"Error al crear el seguimiento de la practica: {e}")

    def eliminar(self, id_seguimiento: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM seguimiento_practicas
                WHERE id_seguimiento = %s
                RETURNING id_seguimiento;
                """,
                (id_seguimiento,)
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
        
                    raise Exception(f"Error al eliminar el seguimiento de la practica: {e}")

    def actualizar(self, id_seguimiento: int, seguimiento_practicas: Seguimiento_practicas):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            UPDATE seguimiento_practicas
                SET id_practica = %s,
                    id_tutor = %s,
                    id_evaluacion_final = %s,
                    fecha_seguimiento = %s,
                    porcentaje_avance = %s,
                    observaciones = %s,
                    dificultades = %s,
                    estado=%s,
                    recomendaciones = %s,
                    fecha_proximo_seguimiento = %s
                    WHERE id_seguimiento = %s
                    RETURNING id_seguimiento;
                    """
            cursor.execute(
                query,
                (
                    seguimiento_practicas.id_practica,
                    seguimiento_practicas.id_tutor,
                    seguimiento_practicas.id_evaluacion_final,
                    seguimiento_practicas.fecha_seguimiento,
                    seguimiento_practicas.porcentaje_avance,
                    seguimiento_practicas.observaciones,
                    seguimiento_practicas.dificultades,
                    seguimiento_practicas.estado,
                    seguimiento_practicas.recomendaciones,
                    seguimiento_practicas.fecha_proximo_seguimiento,
                    id_seguimiento
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
                    raise Exception(f"Error al actualizar el seguimiento de la practica: {e}")
