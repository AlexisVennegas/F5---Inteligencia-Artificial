from fastapi import APIRouter
from classes.queries import qw_list_usuarios, qw_show_usuario, qw_create_usuario, qw_update_usuario, qw_delete_usuario
from classes.validations import UserValidator

router = APIRouter()

@router.get("/listar", tags=["Usuarios"])
def usuarios_listar():
    return qw_list_usuarios()

@router.get("/ver/{dato}/{valor}", tags=["Usuarios"])
def usuarios_ver(dato: str, valor: str):
    """
    El dato puede ser "id", "login" o "email".\n
    Si introduce otro dato, la búsqueda no funcionará.\n
    Si selecciona "id", el valor debe ser numérico.\n
    Si selecciona "login" o "email", el valor será \n
    de texto.
    """
    return qw_show_usuario(dato, valor)

@router.post("/insertar", tags=["Usuarios"])
def usuarios_insertar(usuario: UserValidator):
    return qw_create_usuario(usuario)

@router.put("/actualizar/{dato}/{valor}", tags=["Usuarios"])
def usuarios_actualizar(dato: str, valor: str, usuario: UserValidator):
    return qw_update_usuario(dato, valor, usuario)

@router.delete("/eliminar/{dato}/{valor}", tags=["Usuarios"])
def usuarios_borrar(dato: str, valor: str):
    return qw_delete_usuario(dato, valor)
