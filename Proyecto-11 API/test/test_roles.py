from fastapi.testclient import TestClient
from main import app
import time
import warnings
#from deepdiff import DeepDiff


# para que no muestre informacion de deprecacion
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

client = TestClient(app = app) 

# primer test de main
def test_main():
    response = client.get("/")
    assert response.status_code == 200

# test para la ruta get de todos los roles
def test_roles():
    response = client.get("/Roles/listar")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

#test para la ruta get de un rol
def test_rol():
    response = client.get("/Roles/ver/id/18")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

# test para la inserción de un rol
def test_insertar_rol():
    response = client.post("/Roles/insertar", json={
        "nombre_rol": "Nuevo rol"
    })
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == 'El rol ya existe previamente.'

# Test para la actualización de un rol
def test_actualizar_rol():
    response = client.put("Roles/actualizar/id/18/Escritor")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    # assert response.json() == 'El rol ha sido actualizado.'

# Test para la eliminación de un rol
def test_eliminar_rol():
    response = client.delete("Roles/borrar/id/18")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    # assert response.json() == 'Error: No se puede borrar el rol porque existen usuarios relacionados.'


