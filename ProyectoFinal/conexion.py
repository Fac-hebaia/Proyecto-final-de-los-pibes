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
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f'Error al conectar a la base de datos: {e}')

    def consulta(self, sql, valores):
        try:
            self.conectar()
            self.cursor.execute(sql, valores)
            self.connection.commit()
            print("Consulta ejecutada correctamente.")
        except Error as e:
            print(f'Error al ejecutar la consulta: {e}')
        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

        
        
        

    
   
    
        
    
  
        
    
    
      
    
        
    
           

          
        
        

    
   
    
            
        
     