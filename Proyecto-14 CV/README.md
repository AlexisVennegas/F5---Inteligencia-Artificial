# Proyecto Reconocimiento Facial por Computer Vision
## Integrantes:
- **Alexis Venegas González**
- **Sandra Gómez Santamaría.**

## Planteamiento del problema:
La empresa organizará un evento importante y ha asignado a sus dos principales expertos en inteligencia artificial (IA)
la tarea de desarrollar un sistema de reconocimiento facial mediante Computer Vision. El propósito es agilizar el 
proceso de entrada al evento, eliminando la necesidad de verificar entradas e identificaciones. La propuesta consiste 
en que los empleados se acerquen a un portátil, donde un sistema basado en IA reconocerá sus rostros en tiempo real, 
otorgándoles o denegándoles el acceso.

La solicitud implica la implementación de un sistema de machine learning que, 
a través de una cámara, pueda determinar si la persona frente al dispositivo es un empleado o no. Es importante 
destacar que no se dispone de datos externos, por lo que los expertos en IA deberán generar los datos necesarios. 
Antes de implementar el sistema en producción, se requiere una prueba que garantice el correcto reconocimiento de los 
miembros del equipo (los desarrolladores). Cabe señalar que tanto el modelo como los datos deben ejecutarse en un 
ordenador portátil, y no se permitirá el uso de servicios en la nube debido a consideraciones de privacidad.

## Nuestra solución:
Para abordar esta problemática, se ha empleado el lenguaje de programación Python, junto con las bibliotecas OpenCV y 
face_recognition. Se ha desarrollado un modelo de reconocimiento facial que ha sido entrenado utilizando imágenes de 
los empleados de la empresa. Al iniciar el programa, se activa la cámara en tiempo real, y al detectar la presencia de 
uno o varios empleados frente a la misma, se procede automáticamente a identificar sus rostros, determinando si tienen 
autorización para acceder al evento.

El programa compara el rostro capturado con las imágenes de los empleados almacenadas en el sistema. En caso de 
reconocimiento exitoso, se muestra en pantalla, debajo del rostro identificado, el nombre del empleado y el porcentaje 
de confiabilidad, garantizando la entrada si este porcentaje es igual o superior al 70%. La indicación visual 
"ACCESO PERMITIDO" se presenta en estos casos. Por otro lado, si el rostro no es reconocido, el recuadro delimitador 
se resalta en rojo, y se muestra el mensaje "Desconocido - ACCESO DENEGADO", indicando la prohibición de acceso.

Si el empleado no ha sido registrado previamente, se le solicita que se tome una fotografía, la cual será almacenada
en el sistema para su posterior uso. El programa solicita al usuario que ingrese su nombre, y posteriormente, se
procede a capturar su rostro. Una vez capturada la imagen, se muestra en pantalla, y se le pregunta al usuario si
desea guardarla. Si la respuesta es afirmativa, se procede a almacenar la imagen en el sistema, y se le indica al
usuario que se ha registrado exitosamente. En caso contrario, se le solicita que se tome otra fotografía, y se repite
el proceso.

El programa permite registrar a un número ilimitado de empleados, y se puede ejecutar tantas veces como sea necesario.
El modelo de reconocimiento facial se entrena automáticamente cada vez que se ejecuta el programa, utilizando las
imágenes de los empleados almacenadas en el sistema. Esto garantiza que el modelo se actualice constantemente, y que
sean reconocidos los rostros de todos los empleados registrados.

## Descripción de estructura de archivos:
- **faces**: Carpeta que contiene las imágenes de los empleados y las imágenes de prueba.
  - **Save_data**: Carpeta que contiene los logs.
- **main.py**: Archivo que contiene el código principal del proyecto.
- **README.md**: Archivo que contiene la descripción del proyecto.
- **requirements.txt**: Archivo que contiene las dependencias del proyecto.
 
## Instrucciones de uso:
1. Clonar el repositorio. [Link](.....)
2. Ir a tu directorio del proyecto
3. Opcional, pero muy recomendado: crear un entorno virtual
4. Instalar las dependencias requeridas ejecutando el siguiente comando:
```
pip install -r requirements.txt
```
5. Ejecutar el archivo main.py con el siguiente comando:
```
python app.py
```

## Observaciones:
- Si se utiliza Windows, se debe instalar [Visual Studio](https://visualstudio.microsoft.com/) con las herramientas de C++.
- También se , se debe instalar CMake.
- A continuación, se debe instalar dlib con el siguiente comando:
```
pip install dlib
```
-Seguida de la instalación de face_recognition:
```
pip install face_recognition
```
## Referencias:
- [Face_recognition library](https://github.com/ageitgey/face_recognition?tab=readme-ov-file)
- [OpenCV](https://opencv.org/)
 

  



