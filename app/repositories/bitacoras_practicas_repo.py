from app.core.database import Database
from app.models.bitacoras_practicas import Bitacoras_practicas


class BitacorasPracticasRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM bitacoras_practica
                ORDER BY id_bitacora ASC
                """
                )
            bitacoras = cursor.fetchall()

            cursor.close()
            conn.close()
            return bitacoras
        except Exception as e:
            raise Exception(f"Error al obtener las bitacoras de practicas: {e}")

    def obtener_por_id(self, id_bitacora: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(
                """
                SELECT * FROM bitacoras_practica
                WHERE id_bitacora = %s
                """,
                (id_bitacora,)
                )
            bitacora = cursor.fetchone()
            cursor.close()
            conn.close()
            return bitacora
        except Exception as e:
                    raise Exception(f"Error al obtener la bitacora de practica: {e}")

    def crear(self, bitacora: Bitacoras_practicas):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO bitacoras_practica
            (
                id_practica,
                numero_semana,
                fecha_inicio,
                fecha_fin,
                actividades,
                logros,
                dificultades,
                horas_trabajadas,
                comentarios_tutor,
                estado
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s
            )
            RETURNING id_bitacora;
            """
            cursor.execute(
                query,
                (
                    bitacora.id_practica,
                    bitacora.numero_semana,
                    bitacora.fecha_inicio,
                    bitacora.fecha_fin,
                    bitacora.actividades,
                    bitacora.logros,
                    bitacora.dificultades,
                    bitacora.horas_trabajadas,
                    bitacora.comentarios_tutor,
                    bitacora.estado
                    )
                    )
            nuevo_id = cursor.fetchone()["id_bitacora"]
            conn.commit()

            cursor.close()
            conn.close()
            return nuevo_id
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            raise Exception(f"Error al crear la bitacora de practica: {e}")

    def eliminar(self, id_bitacora: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM bitacoras_practica
                WHERE id_bitacora = %s
                RETURNING id_bitacora;
                """,
                (id_bitacora,)
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
            raise Exception(f"Error al eliminar la bitacora de practica: {e}")
        
    def actualizar(self, id_bitacora: int, bitacora: Bitacoras_practicas):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            UPDATE bitacoras_practica
            SET
                id_practica = %s,
                numero_semana = %s,
                fecha_inicio = %s,
                fecha_fin = %s,
                actividades = %s,
                logros = %s,
                dificultades = %s,
                horas_trabajadas = %s,
                comentarios_tutor = %s,
                estado = %s
            WHERE id_bitacora = %s
            RETURNING id_bitacora;
            """

            cursor.execute(
                query,
                (
                    bitacora.id_practica,
                    bitacora.numero_semana,
                    bitacora.fecha_inicio,
                    bitacora.fecha_fin,
                    bitacora.actividades,
                    bitacora.logros,
                    bitacora.dificultades,
                    bitacora.horas_trabajadas,
                    bitacora.comentarios_tutor,
                    bitacora.estado,
                    id_bitacora
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
            raise Exception(f"Error al actualizar la bitacora de practica: {e}")
    
    
