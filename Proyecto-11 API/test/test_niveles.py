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


#test ruta get de todos los niveles
def test_niveles():
    response = client.get("/Niveles/mostrar_niveles")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == [
  {
    "updated_at": "2023-07-13T17:35:05",
    "created_at": "2023-07-13T17:35:04",
    "id": 1,
    "nivel": "Cero"
  },
  {
    "updated_at": "2023-07-13T17:35:11",
    "created_at": "2023-07-13T17:35:10",
    "id": 2,
    "nivel": "Iniciación"
  },
  {
    "updated_at": "2023-07-13T17:35:15",
    "created_at": "2023-07-13T17:35:15",
    "id": 3,
    "nivel": "Medio"
  },
  {
    "updated_at": "2023-07-13T17:35:22",
    "created_at": "2023-07-13T17:35:21",
    "id": 4,
    "nivel": "Avanzado"
  }
]
    

# test ruta get de un nivel
def test_nivel():
    response = client.get("/Niveles/busqueda_nivel/Cero")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
    "updated_at": "2023-07-13T17:35:05",
    "id": 1,
    "created_at": "2023-07-13T17:35:04",
    "nivel": "Cero"
    }
    


# test para la inserción de un nivel

def test_insertar_nivel():
    response = client.post("Niveles/insertar_niveles", json={
        "nivel": "Nuevo nivel"
    })
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "El Nivel ha sido grabado"}


# Test para la actualización de un nivel

def test_actualizar_nivel():
    response = client.put("Niveles/actualizar_niveles/Nuevo%20nivel/Rapido", json={
        "nivel": "Rapido"
    })
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    # assert response.json() == {"message": "El Nivel ha sido actualizado"}

# Test para la eliminación de un nivel

def test_eliminar_nivel():
    response = client.delete("Niveles/apagar_niveles/Rapido")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    # assert response.json() == {"message": "El Nivel ha sido eliminado"}