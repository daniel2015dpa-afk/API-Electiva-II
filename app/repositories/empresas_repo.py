from app.core.database import Database
from app.models.empresas import Empresas


class EmpresasRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                 """
                 SELECT *
                 FROM empresas
                 ORDER BY id_empresa ASC
                 """
                 )
            empresas = cursor.fetchall()
            cursor.close()
            conn.close()
            return empresas
        except Exception as e:
            raise Exception(f"Error al obtener las empresas: {e}")

    def obtener_por_id(self, id_empresa: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                 """
                 SELECT *
                 FROM empresas
                 WHERE id_empresa = %s
                 """,
                 (id_empresa,)
                 )
            empresa = cursor.fetchone()
            cursor.close()
            conn.close()
            return empresa
        except Exception as e:
            raise Exception(f"Error al obtener la empresa: {e}")

    def crear(self, empresa: Empresas):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            query = """
                INSERT INTO empresas
                (
                    nombre,
                    identificacion_fiscal,
                    direccion,
                    telefono,
                    correo,
                    persona_contacto,
                    estado
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id_empresa;
                    """
            cursor.execute(
                query,
                (
                    empresa.nombre,
                    empresa.identificacion_fiscal,
                    empresa.direccion,
                    empresa.telefono,
                    empresa.correo,
                    empresa.persona_contacto,
                    empresa.estado
                    )
                    )
            nuevo_id = cursor.fetchone()["id_empresa"]
            conn.commit()
            cursor.close()
            conn.close()

            return nuevo_id
        
        except Exception as e:
                    conn.rollback()
                    cursor.close()
                    conn.close()
                    raise Exception(f"Error al crear la empresa: {e}")
        

    def eliminar(self, id_empresa: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM empresas
                WHERE id_empresa = %s
                RETURNING id_empresa;
                """,
                (id_empresa,)
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
                    raise Exception(f"Error al eliminar la empresa: {e}")

    def actualizar(self, id_empresa: int, empresa: Empresas):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            UPDATE empresas
            SET
                nombre = %s,
                identificacion_fiscal = %s,
                direccion = %s,
                telefono = %s,
                correo = %s,
                persona_contacto = %s,
                estado = %s
            WHERE id_empresa = %s
            RETURNING id_empresa;
              """
            cursor.execute(
                query,
                (
                    empresa.nombre,
                    empresa.identificacion_fiscal,
                    empresa.direccion,
                    empresa.telefono,
                    empresa.correo,
                    empresa.persona_contacto,
                    empresa.estado,
                    id_empresa
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
                    raise Exception(f"Error al actualizar la empresa: {e}")

