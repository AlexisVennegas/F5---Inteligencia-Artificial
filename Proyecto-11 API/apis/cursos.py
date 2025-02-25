from fastapi import APIRouter
from classes.queries import qw_create_curso, qw_get_cursos, qw_update_curso, qw_delete_curso, qw_get_curso_unique, qw_mostrar_curso
from classes.validations import CursoValidator

router = APIRouter()

# funcion para mostrar todos los grupos
#@router.get("/listar", tags=["cursos"])
@router.get("/mostrar_cursos", tags=["Cursos"])
def mostrar_cursos():
    """
    <h1>METODO PARA LISTAR TODOS LOS CURSOS</h1>
    <p>➡️ Este metodo devuelve todos los cursos que hay en la base de datos</p>
    """
    return qw_get_cursos()

# funcion para mostrar un solo curso 
@router.get("/mostrar_curso", tags=["Cursos"])
def mostrar_curso(nombre_del_curso: str):
    """
    <h1 style="text-align: center;" >METODO PARA MOSTRAR UN UNICO CURSO</h1>
    <p>➡️ Este metodo devuelve un curso en concreto\n
       ➡️ Se le pasa como parametro el nombre del curso que se quiere ver
    </p>
    """
    return qw_get_curso_unique(nombre_del_curso)

# funcion para insertar un nuevo curso
@router.post("/insertar", tags=["Cursos"])
def insertar_cursos(rol: CursoValidator):
    """
    <h1 style="text-align: center;" >METODO PARA INSERTAR UN NUEVO CURSO  </h1>
    <p>➡️toma como parametro un objeto de tipo CursoValidator\n
    </p>
    """
    return qw_create_curso(rol.dict())

# funcion para modificar un curso
@router.put("/actualizar", tags=["Cursos"])
def modificar_cursos(nombre_del_curso: str, nuevo_nombre: str, nuevo_precio: float, nombre_grupo: str):
    """
    <h1 style="text-align: center;" >METODO PARA ACTUALIZAR UN CURSO  </h1>
    <p>➡️ Como primer parametro el nombre del curso que se quiere actualizar\n
       ➡️ Como segundo parametro el nuevo nombre del curso\n
       ➡️ Como tercer parametro el nuevo precio del curso\n
       ➡️ Como cuarto parametro el nombre del grupo al que pertenece el curso\n
    </p>
    """
    return qw_update_curso(nombre_del_curso, nuevo_nombre, nuevo_precio, nombre_grupo)

@router.delete("/borrar/{nombre}", tags=["Cursos"])
def borrar_curso(nombre: str):
    """
    <h1 style="text-align: center;" >METODO PARA BORRAR UN CURSO  </h1>
    <p>➡️ Como primer parametro el nombre del curso que se quiere borrar\n
    </p>
    """
    return qw_delete_curso(nombre)
