from app.core.database import Database
from app.models.roles import Roles


class RolesRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM roles ORDER BY id_rol ASC"
                  )
            roles = cursor.fetchall()
            cursor.close()
            conn.close()
            return roles
        except Exception as e:
                    raise Exception(f"Error al obtener los roles: {e}")

    def obtener_por_id(self, id_rol: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                 "SELECT * FROM roles WHERE id_rol = %s",
                   (id_rol,)
                     )
            rol = cursor.fetchone()
            cursor.close()
            conn.close()

            return rol
        except Exception as e:
                    raise Exception(f"Error al obtener el rol: {e}")
           

    def crear(self, roles: Roles):
        try:
             conn = self.db.get_connection()
             cursor = conn.cursor()

             query = """

             INSERT INTO roles
             (nombre, descripcion)
               VALUES (%s, %s)
                 RETURNING id_rol;
                 """
             cursor.execute(
                  query,
                  (
                        roles.nombre,
                        roles.descripcion
                        )
                        )
             nuevo_id = cursor.fetchone()["id_rol"]
             conn.commit()
             cursor.close()

             conn.close()
             return nuevo_id
        
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            raise Exception(f"Error al crear el rol: {e}")
            

    def eliminar(self, id_rol: int):
        try:
             conn = self.db.get_connection()
             cursor = conn.cursor()

             cursor.execute(
                """
                DELETE FROM roles
                WHERE id_rol = %s
                RETURNING id_rol;
                """,
                (id_rol,)
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
            raise Exception(f"Error al eliminar el rol: {e}")

    def actualizar(self, id_rol: int, roles: Roles):
        try:
             conn = self.db.get_connection()
             cursor = conn.cursor()

             query = """
             UPDATE roles
             SET nombre = %s,
               descripcion = %s
               WHERE id_rol = %s
               RETURNING id_rol;
               """
             cursor.execute(
                  query,
                  (
                       roles.nombre,
                       roles.descripcion,
                       id_rol
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
            raise Exception(f"Error al actualizar el usuario: {e}")
        