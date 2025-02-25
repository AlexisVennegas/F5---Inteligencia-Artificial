# Utiliza una imagen base de Python 3.11
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /airline

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

# # Cambia al directorio ./Views
WORKDIR /airline/Views

# Define el comando de inicio del contenedor
CMD ["streamlit", "run", "App.py", "--server.port=8501",  "--server.address=0.0.0.0"]

# Expone el puerto 5000 (opcional, si necesitas acceder a la aplicación desde fuera del contenedor)
#
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
