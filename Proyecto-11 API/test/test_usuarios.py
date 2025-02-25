from fastapi.testclient import TestClient
from main import app
import time
import warnings

# para que no muestre informacion de deprecacion
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

client = TestClient(app = app) 

# primer test de main
def test_main():
    response = client.get("/")
    assert response.status_code == 200

# test para la ruta get de todos los usuarios
def test_usuarios():
    response = client.get("/Usuarios/listar")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

#test para la ruta get de un usuario
def test_usuario():
    response = client.get("/Usuarios/ver/id/15")
    assert response.status_code == 200
    # assert response.headers["content-type"] == "application/json"
    # assert response.json() == {
    #     "id": 15,
    #     "login": "login de prueba",
    #     "email": "email de prueba",
    #     "rol": "Escritor"
    # }

# test para la inserción de un usuario
def test_insertar_usuario():
    response = client.post("/Usuarios/insertar", json = {
        "login": "login de prueba",
        "email": "email de prueba",
        "password": "string",
        "nombre_rol": "Escritor",
        "activo": 1
    })
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    #assert response.json() == 'El login ya existe.'

# Test para la actualización de un usuario
def test_actualizar_usuario():
    response = client.put("Usuarios/actualizar/id/15", json = {
        "login": "login de prueba",
        "email": "email de prueba",
        "password": "string",
        "nombre_rol": "Escritor",
        "activo": 1
    })
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    #assert response.json() == 'El usuario ha sido actualizado.'

# Test para la eliminación de un usuario
def test_eliminar_usuario():
    response = client.delete("Usuarios/eliminar/id/18")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    #assert response.json() == 'No se ha encontrado el usuario.'
