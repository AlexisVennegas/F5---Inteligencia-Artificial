# Proyecto 2: API+SQL Danza Fénix

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Descripción del Proyecto

Este proyecto es parte de un trabajo de consultoría tecnológica para la escuela de baile Danza Fénix. El objetivo es desarrollar una solución para gestionar los alumnos y las clases de la escuela mediante una API REST y una base de datos SQL.

## Planteamiento

La dueña de Danza Fénix, Mar, necesita una forma más eficiente y digitalizada para gestionar los datos de los alumnos y las clases de su escuela de baile. Actualmente, todo se lleva a cabo en papel y bolígrafo, lo que resulta en un trabajo tedioso y propenso a errores. El objetivo es implementar una solución utilizando una base de datos SQL y una API REST para facilitar la gestión de los datos.

## Funcionalidades

- Gestión de alumnos: registro, actualización y eliminación de alumnos.
- Gestión de clases: creación, actualización y eliminación de clases.
- Cálculo de precios: aplicación de descuentos y precios según el tipo de clase y nivel.
- Relaciones entre alumnos y clases: un alumno puede estar inscrito en múltiples clases y viceversa.
- Gestión de profesores: asignación de profesores a las clases.

## Tecnologías Utilizadas

- Framework de desarrollo: [FastAPI](https://fastapi.tiangolo.com/)
- Base de datos: [PostgreSQL](https://www.postgresql.org/)
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Herramienta de diagrama de base de datos: [dbdiagram.io](https://dbdiagram.io/)

## Requisitos de Instalación

- Python 3.7 o superior
- PostgreSQL 10 o superior
- Pipenv (opcional, pero recomendado)

## Instalación y Configuración

1. Clona el repositorio:

   ```bash
   git clone https://github.com/AI-School-F5-P2/danza_fenix.git


2.- crea un entorno virtual e instala los requirements.txt

    ```bash
    cd proyecto-danza-fenix
    python -m venv "fenix"  
    cd fenix/Scripts/ && ./activate

    pip install -r .\requirementes.txt  

3.- Configura la base de datos en el archivo :

    ```bash
    DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    crea un archivo config.py y rellan la sig informacion

    db_host = "localhost"
    db_port = "tu-puerto"
    db_name = "crudfastapi"
    db_user = "tu-usuario"
    db_password = "tu-contraseña"


4.- Ejecuta las migraciones de la base de datos:

    ```bash
    alembic upgrade head

5.- Inicia el servidor de desarrollo:

    ```bash    
    uvicorn app.main:app --reload
# Proyecto Academia de danza Fénix

Este proyecto consiste en un sistema de gestión basado en API's para una academia de baile llamada Danza Fénix.
El acceso a los datos se realizará mediante API's a través de una interfaz de Swagger de la librería FastAPI, lo que lo hace especialmente útil para comunicarlo con otra aplicación, aunque lo limita pra su uso por parte de humanos.

### Estructura de archivos.
Los archivos y paquetes que componen la aplicación son los siguientes:
- **main.py**. Contiene la raíz del proyecto. Es desde donde arrancan todas las API's. No contiene API's de gestión de datos en sí mismo, sino importaciones de los archivos donde está dicha gestión.
- **/apis**. Este directorio contiene todos los archivos de API's que, a su vez, son importados en **main.py**.
- **/classes**. Contiene las clases más generales de la aplicación, como la de encriptación de contraseñas, las validaciones de Pydantic, la raíz de modelos, la raíz de consultas o los logs.
- **/conf**. Contiene archivos de configuración.
- **/connection**. Contiene la conexión a base de datos.
- **/models**. Contiene los archivos de modelos de las clases de las tablas.
- **/queries**. Contiene los archivos con las consultas para el CRUD de las distintas tablas.

### El CRUD de una tabla.
Cuando hay que crear el CRUD de una tabla debemos actuar sobre los siguientes puntos de la estructura de la aplicación:
- **/models**. Debemos asegurarnos de que exista el modelo de la tabla, tanto si es una tabla maestra como relacional.
- **/queries**. Debe existir un archivo con funciones especialmente diseñadas para todas las operaciones de CRUD sobre la tabla que nos interese.
- **/apis**. Debe existir un script con las API's que llaman a las fuunciones de **/queries**.
En los tres directorios mencionados se creará un archivo por cada CRUD, con el nombre de la tabla a la que se refiere dicho CRUD.

Además, para crear las API's de un CRUD hay que tocar los siguientes arcivos:
- **/classes/models.py**. Aquí importaremos el modelo de la tabla.
- **/classes/queries.py**. Aquí importaremos el archivo de consultas de la tabla.
- **/classes/validations.py**. Aquí incluimos los esquemas de tipos de datos de PyDantic relativos a la tabla con la que estamos trabajando.
- **main.py**. En este archivo se importa la API de cada tabla.
Estos cuatro archivos son comunes a todas las tablas, por lo que pueden dar problemas a la hora de mergear.


