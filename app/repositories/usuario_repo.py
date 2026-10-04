from app.core.database import Database
from app.models.usuario import Usuario


class UsuarioRepository:

    def __init__(self):
        self.db = Database()

 
    def obtener_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                  SELECT * FROM usuarios
                  ORDER BY id_usuario ASC
                  """
                    )
            usuarios = cursor.fetchall()
            cursor.close()
            conn.close()
            return usuarios
        
        except Exception as e:
            raise Exception(f"Error al obtener los usuarios: {e}")

    def obtener_por_id(self, id_usuario: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                 """
                 SELECT *
                 FROM usuarios
                   WHERE id_usuario = %s
                   """,
                   (id_usuario,)
                   )
            usuario = cursor.fetchone()
            cursor.close()
            conn.close()

            return usuario
        
        except Exception as e:
            raise Exception(f"Error al obtener el usuario: {e}")

 
    def crear(self, usuario: Usuario):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO usuarios
            (
                nombre,
                apellido,
                edad,
                celular,
                correo,
                ciudad,
                contraseña,
                estado,
                direccion,
                id_rol
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s
            )
            RETURNING id_usuario;
            """
            cursor.execute(
                query,
                (
                    usuario.nombre,
                    usuario.apellido,
                    usuario.edad,
                    usuario.celular,
                    usuario.correo,
                    usuario.ciudad,
                    usuario.contraseña,
                    usuario.estado,
                    usuario.direccion,
                    usuario.id_rol
                    )
                    )
            nuevo_id = cursor.fetchone()["id_usuario"]
            conn.commit()
            cursor.close()
            conn.close()
            return nuevo_id
        
        except Exception as e:

            conn.rollback()
            cursor.close()
            conn.close()

            raise Exception(f"Error al crear el usuario: {e}")

    def eliminar(self, id_usuario: int):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM usuarios
                WHERE id_usuario = %s
                RETURNING id_usuario;
                """,
                (id_usuario,)
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

            raise Exception(f"Error al eliminar el usuario: {e}")
      
    def actualizar(self, id_usuario: int, usuario: Usuario):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            query = """
              UPDATE usuarios
              SET 
              nombre = %s, 
              apellido = %s, 
              edad = %s, 
              celular = %s, 
              correo = %s, 
              ciudad = %s, 
              contraseña = %s, 
              estado = %s, 
              direccion = %s, 
              id_rol = %s
              WHERE id_usuario = %s
                RETURNING id_usuario;
                  """
            cursor.execute(
                query,
                (
                    usuario.nombre,
                    usuario.apellido,
                    usuario.edad,
                    usuario.celular,
                    usuario.correo,
                    usuario.ciudad,
                    usuario.contraseña,
                    usuario.estado,
                    usuario.direccion,
                    usuario.id_rol,
                    id_usuario
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

