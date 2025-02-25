import os
import logging

class Logs():
    
    def __init__(self):
        logs_dir = '../logs'
        log_file = 'archivo.log'
        # Verificar si la carpeta de logs existe, de lo contrario, crearla
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        # Ruta completa del archivo de logs
        log_path = os.path.join(logs_dir, log_file)

        logging.basicConfig(filename=log_path, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        
    # Registros
    def debug(self, mensaje):
        logging.debug(mensaje)
        
        
    def info(self, mensaje):
        logging.info(mensaje)
        
         
    def warning(self, mensaje):
        logging.warning(mensaje)
        
         
    def error(self, mensaje):
        logging.error(mensaje)
        
          
    def critical(self, mensaje):
        logging.critical(mensaje)


























