from fastapi.testclient import TestClient
from main import app
import time
import warnings


# para que no muestre informacion de deprecacion
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

# from apis.cursos import router

client = TestClient(app=app)


#test main
def test_main():
    response = client.get("/") 
    assert response.status_code == 200


#test ruta get de todos los profesores 
def test_profesores():
    response = client.get("/Profesores/ver")
    assert response.status_code == 202
    

# test ruta get de un profesor
def test_profesor():
    response = client.get("/Profesores/busqueda_profesor?profesores=Mar")
    assert response.status_code == 202

    

#test  para la ruta de insertar profesores
def test_insertar_profesores():
    response = client.post("/Profesores/insertar", json={
    "nombre_profesor": "Luisa"
    })        

    assert response.status_code == 202


#test  para la ruta de modificar profesores
def test_modificar_profesores():
    response = client.put("/Profesores/actualizar/Luisa/MariaDB", json={
    "nombre_profesor": "Luisa",
    "id": 8
    })        

    assert response.status_code == 202

# test para la ruta de borrar profesores

def test_borrar_profesores():
    response = client.delete("/Profesores/eliminar/MariaDB")
    assert response.status_code == 202
