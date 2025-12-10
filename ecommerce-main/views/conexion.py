import mysql.connector
from mysql.connector import *


class Conexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None


    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)
            self.cursor = self.connection.cursor()
            print("Conexión exitosa a la base de datos.")
            return True
            
        except Error as e:
            print(f'Error al conectar a la base de datos: {e}')
            return False
    def consulta(self, sql, valores=None):
        try:
            
            sql_upper = str(sql).strip()

            # Asegurar estructura correcta
            if valores is not None and isinstance(valores, str):
                valores = (valores,)  # convertir string → tupla

            self.cursor.execute(sql, valores)

            if any(op in sql_upper for op in ['INSERT', 'UPDATE', 'DELETE']):
                self.connection.commit()

            print("Consulta ejecutada correctamente.")

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        

    def cerrar(self):
        """Cierra el cursor y la conexión a la base de datos de forma segura."""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a DB cerrada.")
        
        

    
   
    
        
    
  
        
    
    
      
    
        
    
           

          
        
        

    
   
    
            
        
     