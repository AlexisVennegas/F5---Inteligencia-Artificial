import hashlib
import mysql.connector
from logs import Logs
from decouple import config

class Data:
    
    def __init__(self):   
        self.logs = Logs()
        try:
            self.conexion = mysql.connector.connect(
                host = config("MYSQL_HOST"),
                user = config("MYSQL_USER"),
                password = config("MYSQL_PASSWORD"),
                database = config("MYSQL_DATABASE")
            )
        except mysql.connector.Error as error:
            self.logs.error("Error databa_data.py al conectar a la base de datos:", error)
            print("Error al conectar a la base de datos:", error)
           
    
    def precios(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT precio_mov, precio_det FROM data")
        fila = cursor.fetchall()
        precios = []
        for fila in fila:
            precio = {
                "precio_mov":fila[0],
                "precio_det":fila[1]
            }
            precios.append(precio)
        return precios
        
    def editarPrecios(self, precio_det, precio_mov):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE data SET precio_mov = %s, precio_det = %s", (precio_mov, precio_det))
        
        self.conexion.commit()
        # self.conexion.close()
        # cursor.close()
        
        
        
    def password_hash(self, password):
        hash_object = hashlib.sha256()
        contraseña_bytes = password.encode('utf-8')
        hash_object.update(contraseña_bytes)
        hash_hex = hash_object.hexdigest()
        # Retornar el hash
        return hash_hex

    def password_insert(self,password):
        hash_object = hashlib.sha256()
        contraseña_bytes = password.encode('utf-8')
        hash_object.update(contraseña_bytes)
        hash_hex = hash_object.hexdigest()
        # Retornar el hash

        cursor = self.conexion.cursor()
        cursor.execute(f"INSERT INTO DATA (password) VALUE ('{hash_hex}')")
        self.conexion.commit()
        
        # fila = cursor.fetchall()
        # print(fila)
        return hash_hex

    def password_get(self):
        cursor = self.conexion.cursor()
        cursor.execute(f"SELECT * FROM DATA ")
        fila = cursor.fetchall()
        return fila[0][0]
  
  
  
