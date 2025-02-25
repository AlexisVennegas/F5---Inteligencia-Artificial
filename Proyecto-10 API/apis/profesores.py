from fastapi import APIRouter
from classes.queries import qw_get_profesores, qw_post_profesores, qw_put_profesores, qw_delete_profesores, qw_list_profesores
from classes.validations import ProfesorValidator


router = APIRouter()

@router.get("/ver", tags = ["Profesores"])
def mostrar_profesores ():
    ''' <h1> Método para buscar a todos los profesores</h1>'''
    ''' <p>Este método devuelve a todos los profesores con su ID</p>'''
    return qw_get_profesores()

@router.post("/insertar", tags = ["Profesores"])
def insertar_profesor(profesor: ProfesorValidator):
    ''' <h1>Método para insertar a un profesor</h1>'''
    ''' <p>Este método inserta un profesor</p>'''
    return qw_post_profesores(profesor.dict())

@router.get("/busqueda_profesor", tags=["Profesores"])
def busqueda_profesor (profesores: str):
    ''' <h1>Método para buscar un solo profesor/a</h1>'''
    ''' <p>Este método buscar un solo profesor/a</p>'''
    return qw_list_profesores(profesores)

@router.post("/insertar", tags = ["Profesores"])
def insertar_profesor(profesor: ProfesorValidator):
    ''' <h1>Método para insertar a un profesor</h1>'''
    ''' <p>Este método inserta un profesor</p>'''
    return qw_post_profesores(profesor.dict())

@router.put("/actualizar/{profesor}/{nuevo_profesor}", tags = ["Profesores"])
def actualizar_profesor(profesor: str, nuevo_profesor: str):
    ''' <h1>Método para actualizar a un/a profesor/a</h1>'''
    ''' <p>Este método actualizar un profesor</p>'''
    return qw_put_profesores(profesor, nuevo_profesor)

@router.delete("/eliminar/{profesor}", tags = ["Profesores"])
def eliminar_profesor(profesor: str):
    ''' <h1>Método para elimiar a un/a profesor/a</h1>'''
    ''' <p>Este método eliminar un profesor</p>'''
    return qw_delete_profesores(profesor)