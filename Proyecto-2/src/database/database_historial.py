import mysql.connector
import hashlib
import os
import asyncio
from logs import Logs
import shutil
import os
from decouple import config

class Database_historial:
    #CONEXION A BASE DE DATOS
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
            self.logs.error("Error en Database_historial.py al conectar a la base de datos:", error)
            print("Error al conectar a la base de datos:", error)
           
    
    # EXTRAER HISTORIAL COMPLETO 
    def all(self):
        # conexion = self.conexion()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM  `historial-carreras`")
        fila = cursor.fetchall()
        
        historial = []
        for element in fila:
            data = {
                "id":element[0],
                "tarifa":element[1],
                "fecha":element[2]
            }
            historial.append(data)
        # self.guardarEnTextoPlano(historial)
        return historial
    
    # INSERTAR
    def insertar(self, data):
        self.guardarEnTextoPlano(data)
        tarifa =  data["tarifa"]
        fecha =  data["fecha"]
        cursor = self.conexion.cursor()
        query = "INSERT INTO `historial-carreras` (tarifa, fecha) VALUES (%s, %s)"
        values = (tarifa, fecha)
        cursor.execute(query, values)
        self.conexion.commit()


   
    
     #guardar en un archivo .txt
    def guardarEnTextoPlano(self, historial):
        carpeta = "../historial"
        archivo = "historial.txt"

        # Comprobar si la carpeta existe, si no, crearla
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Ruta completa del archivo
        ruta_archivo = os.path.join(carpeta, archivo)

        # Leer contenido existente (si hay)
        contenido_existente = ""
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r") as archivo_txt:
                # print(archivo_txt.read())
                contenido_existente = archivo_txt.read()

        # Verificar si el nuevo dato ya existe en el contenido existente
        texto_nuevo = f" TARIFA: {historial['tarifa']} FECHA: {historial['fecha']} \n"
        if texto_nuevo not in contenido_existente:
            # Abrir archivo de texto en modo de añadir (append) para agregar el nuevo dato al final
            with open(ruta_archivo, "a") as archivo_txt:
                archivo_txt.write(texto_nuevo)

        self.generarCopiaEnPC()

    
    
    
    def generarCopiaEnPC(self):
       
        ruta_original = "../historial/historial.txt"
        carpeta_descargas = os.path.expanduser("~/Downloads")
        archivoCopia = "historial_del_taximetro.txt"
        
        ruta_destino = os.path.join(carpeta_descargas, archivoCopia)
        shutil.copy(ruta_original, ruta_destino)

        return "Se descargo en la carpeta de descargas"



