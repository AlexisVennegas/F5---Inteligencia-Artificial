from fastapi.testclient import TestClient
from main import app
import warnings
import pytest

warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

client = TestClient(app=app)


#test main
def test_main():
    response = client.get("/") 
    assert response.status_code == 200



#test ruta get de todos los alumnos
def test_alumnos():
    response = client.get("/Alumnos/mostrar_alumnos")
    assert response.status_code == 200
    

#test ruta get de alumno
def test_alumno():
    response = client.get("/Alumnos/mostrar_alumnocata")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "id": 6,
        "apellidos": "Gonzalez",
        "nacimiento": "2023-07-24T18:37:34",
        "telefono": "3323211",
        "descuento_familiar": 1,
        "updated_at": "2023-07-24T20:37:28",
        "dni": "Cata",
        "nombre": "Catalina",
        "email": "cata@gmail.com",
        "created_at": "2023-07-24T20:37:28"
        }




#test  para la ruta de insertar alumnos
def test_insertar_alumnos():
    response = client.post("/Alumnos/insertar", json={
    "nombre": "Alexander",
    "apellidos": "Perry",
    "descuento_familiar": 1,
    "dni": "A12345678",
    "email": "alexander@gmail.com",
     "telefono": "11221122",
    "nacimiento": "2023-07-25T16:47:50.160Z"
    })        

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == 	{"mensaje": "Alumno creado correctamente"}




#test  para la ruta de actualizar alumnos
def test_actualizar_alumnos():
    response = client.put("/Alumnos/actualizar/A12345678", json={
    "nombre": "Pedro",
    "apellidos": "Perez",
    "descuento_familiar": 1,
    "dni": "A12345678",
    "email": "pica@gmail.com",
     "telefono": "123123",
    "nacimiento": "2023-07-25T16:47:50.160"
    })        
    assert  response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"mensaje": "Alumno actualizado correctamente"}
    

def test_borrar_alumno():
    response = client.delete("/Alumnos/eliminar/A12345678")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {'mensaje': 'Alumno eliminado correctamente'}
