from fastapi import APIRouter
from classes.queries import qw_list_roles, qw_get_rol, qw_create_rol, qw_update_rol, qw_delete_rol
from classes.validations import RolValidator

router = APIRouter()

@router.get("/listar", tags=["Roles"])
def roles_listar():
    return qw_list_roles()

@router.get("/ver/{dato}/{valor}", tags=["Roles"])
def roles_ver(dato, valor):
    """
    El dato puede ser "id", para localizar un rol por su identificador\n
    o "nombre" para localizarlo por su nombre actual.
    """
    return qw_get_rol(dato, valor)

@router.post("/insertar", tags=["Roles"])
def roles_insertar(rol: RolValidator):
    return qw_create_rol(rol.dict())

@router.put("/actualizar/{dato}/{valor}/{nuevo_nombre}", tags=["Roles"])
def roles_actualizar(dato: str, valor: str, nuevo_nombre: str):
    """
    El dato puede ser "id", para localizar un rol por su identificador\n
    o "nombre" para localizarlo por su nombre actual.
    """
    return qw_update_rol(dato, valor, nuevo_nombre)

@router.delete("/borrar/{dato}/{valor}", tags=["Roles"])
def roles_borrar(dato: str, valor: str):
    """
    El dato puede ser "id", para localizar un rol por su identificador\n
    o "nombre" para localizarlo por su nombre actual.
    """
    return qw_delete_rol(dato, valor)
