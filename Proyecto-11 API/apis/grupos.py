from fastapi import APIRouter
from classes.queries import qw_list_grupos, qw_get_grupo, qw_create_grupo, qw_update_grupo, qw_delete_grupo
from classes.validations import GrupoValidator

router = APIRouter()

@router.get("/listar", tags=["Grupos"])
def grupos_listar():
    return qw_list_grupos()

@router.get("/ver/{dato}/{valor}", tags=["Grupos"])
def grupos_ver(dato, valor):
    """
    El dato puede ser "id", para localizar un grupo por su clave primaria\n
    o "nombre" para localizarlo por su nombre actual.
    """
    return qw_get_grupo(dato, valor)

@router.post("/insertar", tags=["Grupos"])
def grupos_insertar(grupo: GrupoValidator):
    return qw_create_grupo(grupo.dict())

@router.put("/actualizar/{dato}/{valor}/{nuevo_nombre}", tags=["Grupos"])
def grupos_actualizar(dato: str, valor: str, nuevo_nombre: str):
    """
    El dato puede ser "id", para localizar un grupo por su clave primaria\n
    o "nombre" para localizarlo por su nombre actual.
    """
    return qw_update_grupo(dato, valor, nuevo_nombre)

@router.delete("/borrar/{dato}/{valor}", tags=["Grupos"])
def grupos_borrar(dato: str, valor: str):
    """
    El dato puede ser "id", para localizar un grupo por su clave primaria\n
    o "nombre" para localizarlo por su nombre actual.
    """
    return qw_delete_grupo(dato, valor)

