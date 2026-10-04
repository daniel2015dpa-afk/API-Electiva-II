from app.core.database import Database
from app.models.modulos import Modulos


class ModulosRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM modulos
                ORDER BY id_modulo ASC
                """
                )

            modulos = cursor.fetchall()

            cursor.close()
            conn.close()

            return modulos
        except Exception as e:
             raise Exception(f"Error al obtener los modulos: {e}")
        

    def obtener_por_id(self, id_modulo: int):
        try:

            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM modulos
                WHERE id_modulo = %s
                """,
                (id_modulo,)
                )

            modulo = cursor.fetchone()
            cursor.close()
            conn.close()
            return modulo
        except Exception as e:
                     raise Exception(f"Error al obtener el modulo: {e}")
        

    def crear(self, modulo: Modulos):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO modulos
            (
                nombre,
                descripcion
            )
            VALUES (%s, %s)
            RETURNING id_modulo;
            """
            cursor.execute(
                query,
                (
                    modulo.nombre,
                    modulo.descripcion
                    )
                    )

            nuevo_id = cursor.fetchone()["id_modulo"]

            conn.commit()
            cursor.close()
            conn.close()
            return nuevo_id
        
        except Exception as e:
                    conn.rollback()
                    cursor.close()
                    conn.close()
                    raise Exception(f"Error al crear modulo: {e}")

    def eliminar(self, id_modulo: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM modulos
                WHERE id_modulo = %s
                RETURNING id_modulo;
                """,
                (id_modulo,)
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
                    raise Exception(f"Error al eliminar modulo: {e}")

    def actualizar(self, id_modulo: int, modulo: Modulos):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            UPDATE modulos
            SET
                nombre = %s,
                descripcion = %s
            WHERE id_modulo = %s
            RETURNING id_modulo;
            """

            cursor.execute(
                query,
                (
                    modulo.nombre,
                    modulo.descripcion,
                    id_modulo
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
            raise Exception(f"Error al actualizar modulo: {e}")

