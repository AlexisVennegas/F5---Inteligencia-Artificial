from fastapi.testclient import TestClient
from main import app
import time
import warnings


# para que no muestre informacion de deprecacion
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

# from apis.cursos import router

client = TestClient(app=app)

def animated_print(text):
    print()
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()




# primer test de main
def test_main():
    response = client.get("/")
    assert response.status_code == 200
    # assert response.json() == {"message": "Bienvenido a la API de Danza Fenix"}
        # assert response.headers["content-type"] == "application/json"


# test para la ruta get de todos los cursos
def test_cursos():
    response = client.get("/Cursos/mostrar_cursos")
    assert response.status_code == 200  
    assert response.headers["content-type"] == "application/json"
    
# test para la ruta de get de un unico curso
def test_curso():
    response = client.get("/Cursos/mostrar_curso?nombre_del_curso=Bachata")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "nombre_curso": "Bachata",
        "id_grupo": "Relax",
        "updated_at": "2023-07-13T16:45:10",
        "created_at": "2023-07-13T16:45:10",
        "precio": 35,
        "id": 1
        }
    

# test para la ruta de post de insertar un 
def test_insertar_curso():
    response = client.post("/Cursos/insertar", json={
        "nombre_curso": "Reggae",
        "id_grupo": "Relax",
        "precio": 35
    })
    assert response.status_code == 202
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {'message': 'El curso ha sido creado.'}


# test para la ruta de put de modificar un curso
def test_modificar_curso():
    response = client.put("/Cursos/actualizar?nombre_del_curso=Reggae&nuevo_nombre=chaka&nuevo_precio=40&nombre_grupo=Relax")
    assert response.status_code == 202
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {'message': 'El curso ha sido modificado.'}


# test para la ruta de delete de borrar un curso
def test_borrar_curso():
    response = client.delete("/Cursos/borrar/chaka")
    assert response.status_code == 202
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {'message': 'El curso ha sido borrado.'}

