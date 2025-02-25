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

# test para la ruta get de todos los grupos
def test_grupos():
    response = client.get("/Grupos/listar")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

#test para la ruta get de un grupo
def test_grupo():
    response = client.get("/Grupos/ver/id/3")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

# test para la inserción de un grupo
def test_insertar_curso():
    response = client.post("/Grupos/insertar", json={
        "nombre_grupo": "Nuevo grupo"
    })
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == 'El grupo ya existe previamente.'

# Test para la actualización de un grupo
def test_actualizar_grupo():
    response = client.put("Grupos/actualizar/id/3/Nuevo grupo de prueba")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    # assert response.json() == 'El grupo ha sido actualizado.'

# Test para la eliminación de un grupo
def test_eliminar_grupo():
    response = client.delete("Grupos/borrar/id/3")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    #assert response.json() == 'Error: No se puede borrar el grupo porque existen cursos relacionados.'



