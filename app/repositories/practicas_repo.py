from app.core.database import Database
from app.models.practicas import Practicas


class PracticasRepository:

    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        try:
                conn = self.db.get_connection()
                cursor = conn.cursor()

                cursor.execute(
                        "SELECT * FROM practicas ORDER BY id_practica ASC"
                        )
                practicas = cursor.fetchall()
                cursor.close()
                conn.close()

                return practicas

        except Exception as e:
                raise Exception(f"Error al obtener las practicas: {e}")
    
    def obtener_por_id(self, id_practica: int):
            try:
                    conn = self.db.get_connection()
                    cursor = conn.cursor()

                    cursor.execute(
                            "SELECT * FROM practicas WHERE id_practica = %s",
                            (id_practica,)
                            )
                    practica = cursor.fetchone()
                    cursor.close()
                    conn.close()

                    return practica
            except Exception as e:
                    raise Exception(f"Error al obtener la practica: {e}")
    
    
    def crear(self, practica: Practicas):
                try:
                        conn = self.db.get_connection()
                        cursor = conn.cursor()
        
                        query = """
                            INSERT INTO practicas
                                (id_postulacion, id_tutor, fecha_inicio, fecha_fin,
                                horas_requeridas, horas_completadas, objetivo, estado)
                            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)
                            RETURNING id_practica;
                            """
                        cursor.execute(
                                query,
                                (   practica.id_postulacion,
                                    practica.id_tutor,
                                    practica.fecha_inicio,
                                    practica.fecha_fin,
                                    practica.horas_requeridas,
                                    practica.horas_completadas,
                                    practica.objetivo,
                                    practica.estado                     
                                    )
                                    )
                        nuevo_id = cursor.fetchone()["id_practica"]
                        conn.commit()

                        cursor.close()
                        conn.close()

                        return nuevo_id
                except Exception as e:
                    conn.rollback()
                    cursor.close()
                    conn.close()
                    raise Exception(f"Error al crear la practica: {e}")
                

    def eliminar(self, id_practica: int):
                try:
                        conn = self.db.get_connection()
                        cursor = conn.cursor()
                        cursor.execute(
                                """
                                DELETE FROM practica
                                WHERE id_practica = %s
                                RETURNING id_practica;
                                """,
                                (id_practica)
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
                    raise Exception(f"Error al eliminar la practica: {e}")
    
    def actualizar(self, id_practica: int, practica: Practicas):
                try:
                        conn = self.db.get_connection()
                        cursor = conn.cursor()
                        query = """
                        
                            UPDATE practicas
                            SET 
                                id_postulacion=%s,
                                id_tutor=%s,
                                fecha_inicio = %s, 
                                fecha_fin = %s,
                                horas_requeridas = %s, 
                                horas_completadas = %s, 
                                estado=%s,
                                objetivo = %s 
                        
                        WHERE id_practica= %s
                        RETURNING id_practica;
                        """
                        cursor.execute(
                                query,
                                (  
                                        practica.id_postulacion,
                                        practica.id_tutor,
                                        practica.fecha_inicio,
                                        practica.fecha_fin,
                                        practica.horas_requeridas,
                                        practica.horas_completadas,
                                        practica.objetivo,
                                        practica.estado,
                                        id_practica
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
                                    raise Exception(f"Error al actualizar la practica: {e}")

    