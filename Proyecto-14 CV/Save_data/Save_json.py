from PIL import Image
import base64
import json
import time
import logging
from datetime import datetime

# PRIMEROS CONFIGURAMOS EL SISTEMA DE LOGGING
logging.basicConfig(
    filename='Save_data\Logs\Register.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# FUNCION PARA GUARDAR LOS DATOS EN UN ARCHIVO JSON
def save_json(name, imagen_path):
    # obtener la fecha y hora actual
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")

    # crear un diccionario con los datos
    data = {
        'name': name,
        'date': date,
        'photo': imagen_path
    }

    # Leer datos actuales del archivo JSON si existe
    try:
        # Leer datos actuales del archivo JSON si existe
        with open('Save_data/Logs/Register.json', 'r') as file:
            data_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío, inicializar con una lista vacía
        data_list = []

    # Agregar el diccionario a la lista
    data_list.append(data)

    # Guardar la lista completa en un archivo JSON
    with open('Save_data/Logs/Register.json', 'w') as file:
        json.dump(data_list, file)

    # registrar el evento en el sistema de logging
    logging.info(f'El usuario {name} se ha registrado correctamente')


# FUNCION PARA CODIFICAR LA IMAGEN
def encode_image(imagen_path):
    with open(imagen_path, 'rb') as file:
        # leer la imagen
        image_bytes = file.read()

        # codificar la imagen en base64
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')

    return encoded_string


# FUNCION PRINCIPAL
def main_json(name_person, imagen_path):
    try:
        # codificar la imagen
        imagen_path = "./data/" + imagen_path + "/" + imagen_path + '.jpg'
        # encoded_image = encode_image(imagen_path)
        save_json(name_person, imagen_path)
    except Exception as e:
        logging.error(f'Error al guardar los datos en el archivo JSON: {e}')