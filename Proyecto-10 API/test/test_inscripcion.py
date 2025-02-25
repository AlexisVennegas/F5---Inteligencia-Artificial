from fastapi.testclient import TestClient
from main import app
import time
import warnings


# para que no muestre informacion de deprecacion
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

# from apis.cursos import router

client = TestClient(app=app)

# primer test de main
def test_main():
    response = client.get("/")
    assert response.status_code == 200
    # assert response.json() == {"message": "Bienvenido a la API de Danza Fenix"}
        # assert response.headers["content-type"] == "application/json"




# test para insertar una inscripcion
def test_insertar_inscripcion():
    response = client.post("/Inscripcion/insertar", json={
    "dni_alumno": "Cata",
    "nombre_curso": "Bachata",
    "nivel": "Cero",
    "profesor": "Mar"
    }
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"    

