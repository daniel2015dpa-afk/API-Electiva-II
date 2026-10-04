from app.core.database import Database
from app.models.evaluaciones_finales import EvaluacionesFinales


class EvaluacionesFinalesRepository:

    def __init__(self):
        self.db = Database()


    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM evaluaciones_finales
                ORDER BY id_evaluacion ASC
                """
                )
            evaluaciones_finales = cursor.fetchall()
            cursor.close()
            conn.close()
            return evaluaciones_finales
        except Exception as e:
               raise Exception(f"Error al obtener las evaluaciones finales: {e}")
        

    def obtener_por_id(self, id_evaluacion: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM evaluaciones_finales
                WHERE id_evaluacion = %s
                """,
                (id_evaluacion,)
                )
            evaluaciones_finales = cursor.fetchone()
            cursor.close()
            conn.close()

            return evaluaciones_finales
        except Exception as e:
               raise Exception(f"Error al obtener la evaluacion final: {e}")

    def crear(self, evaluaciones_finales: EvaluacionesFinales):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO evaluaciones_finales
            (
                id_seguimiento,
                id_evaluador,
                fecha_evaluacion,
                resultado,
                calificacion,
                cumplimiento_objetivos,
                desempeno,
                fortalezas,
                aspectos_mejora,
                observaciones,
                recomendaciones
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
            RETURNING id_evaluacion;
            """
            cursor.execute(
                query,
                (
                    evaluaciones_finales.id_seguimiento,
                    evaluaciones_finales.id_evaluador,
                    evaluaciones_finales.fecha_evaluacion,
                    evaluaciones_finales.resultado,
                    evaluaciones_finales.calificacion,
                    evaluaciones_finales.cumplimiento_objetivos,
                    evaluaciones_finales.desempeno,
                    evaluaciones_finales.fortalezas,
                    evaluaciones_finales.aspectos_mejora,
                    evaluaciones_finales.observaciones,
                    evaluaciones_finales.recomendaciones
                    )
                    )
            nuevo_id = cursor.fetchone()["id_evaluacion"]
            conn.commit()

            cursor.close()
            conn.close()

            return nuevo_id
        except Exception as e:
                            conn.rollback()
                            cursor.close()
                            conn.close()
                            raise Exception(f"Error al crear la evaluacion final: {e}")
        
    def eliminar(self, id_evaluacion: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM evaluaciones_finales
                WHERE id_evaluacion = %s
                RETURNING id_evaluacion;
                """,
                (id_evaluacion,)
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
                            raise Exception(f"Error al eliminar la evaluacion final: {e}")

    def actualizar(self, id_evaluacion: int, evaluaciones_finales: EvaluacionesFinales):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """           
            UPDATE evaluaciones_finales
            SET
                id_seguimiento = %s,
                id_evaluador = %s,
                fecha_evaluacion = %s,
                resultado = %s,
                calificacion = %s,
                cumplimiento_objetivos = %s,
                desempeno = %s,
                fortalezas = %s,
                aspectos_mejora = %s,
                observaciones = %s,
                recomendaciones = %s,
                fecha_actualizacion = CURRENT_TIMESTAMP
            WHERE id_evaluacion = %s
            RETURNING id_evaluacion;
            """

            cursor.execute(
                query,
                (
                    evaluaciones_finales.id_seguimiento,
                    evaluaciones_finales.id_evaluador,
                    evaluaciones_finales.fecha_evaluacion,
                    evaluaciones_finales.resultado,
                    evaluaciones_finales.calificacion,
                    evaluaciones_finales.cumplimiento_objetivos,
                    evaluaciones_finales.desempeno,
                    evaluaciones_finales.fortalezas,
                    evaluaciones_finales.aspectos_mejora,
                    evaluaciones_finales.observaciones,
                    evaluaciones_finales.recomendaciones,
                    id_evaluacion
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
                    raise Exception(f"Error al actualizar la evaluacion final: {e}")



    