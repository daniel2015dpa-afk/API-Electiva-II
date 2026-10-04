from app.core.database import Database
from app.models.modulos_x_roles import Modulos_x_roles


class Modulos_x_rolesRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM modulos_x_roles ORDER BY id_modulo_rol ASC"
                  )
            modulos_x_rol = cursor.fetchall()

            cursor.close()
            conn.close()
            return modulos_x_rol
        except Exception as e:
              raise Exception(f"Error al obtener los modulos_x_roles: {e}")
        
        

    def obtener_por_id(self, id_modulo_rol: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM modulos_x_roles WHERE id_modulo_rol = %s",
                (id_modulo_rol,)
                )
            modulos_x_roles = cursor.fetchone()
            cursor.close()
            conn.close()
            return modulos_x_roles
        
        except Exception as e:
              raise Exception(f"Error al obtener modulo_x_rol: {e}")
        

    def crear(self, modulos_x_roles: Modulos_x_roles):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO modulos_x_roles
            (id_modulo, id_rol, puede_ver, puede_crear, puede_actualizar, puede_eliminar)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_modulo_rol;
            """

            cursor.execute(
                query,
                (
                    modulos_x_roles.id_modulo,
                    modulos_x_roles.id_rol,
                    modulos_x_roles.puede_ver,
                    modulos_x_roles.puede_crear,
                    modulos_x_roles.puede_actualizar,
                    modulos_x_roles.puede_eliminar
                    ) 
                    )
            nuevo_id = cursor.fetchone()["id_modulo_rol"]
            conn.commit()
            cursor.close()
            conn.close()
            return nuevo_id
        
        except Exception as e:
                    conn.rollback()
                    cursor.close()
                    conn.close()
                    raise Exception(f"Error al crear modulo_x_rol: {e}")

    def eliminar(self, id_modulo_rol: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute( 
                """
                DELETE FROM modulos_x_roles
                WHERE id_modulo_rol = %s
                RETURNING id_modulo_rol;
                """,
                (id_modulo_rol,)
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
                    raise Exception(f"Error al eliminar modulo_x_rol: {e}")
        

    def actualizar(self, id_modulo_rol: int, modulos_x_roles: Modulos_x_roles):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
            UPDATE modulos_x_roles
                SET id_modulo = %s,
                    id_rol = %s,
                    puede_ver = %s,
                    puede_crear = %s,
                    puede_actualizar = %s,
                    puede_eliminar = %s
                    WHERE id_modulo_rol = %s
                      RETURNING id_modulo_rol;
                        """
            cursor.execute(
                query,
                (
                    modulos_x_roles.id_modulo,
                    modulos_x_roles.id_rol,
                    modulos_x_roles.puede_ver,
                    modulos_x_roles.puede_crear,
                    modulos_x_roles.puede_actualizar,
                    modulos_x_roles.puede_eliminar,
                    id_modulo_rol
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
                    raise Exception(f"Error al actualizar modulos_x_roles: {e}")
                
        
        
        
