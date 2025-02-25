from fastapi import APIRouter
from classes.queries import qw_get_alumnos, qw_get_alumno, qw_post_alumnos, qw_put_alumnos, qw_delete_alumno
from classes.validations import AlumnoValidator

router = APIRouter()

@router.get("/mostrar_alumnos", tags = ["Alumnos"])
def mostrar_alumnos():
    """<h1>Metodo para mostrar alumnos. </h1>
    <p>Este metodo devuelve todos los alumnos<p/>"""
    return qw_get_alumnos()


@router.get("/mostrar_alumno{dni_alumno}", tags = ["Alumnos"])
def mostrar_alumno(dni_alumno: str):
    """<h1>Metodo para buscar un anico alumno.</h1>
    <p> Este metodo devuelve el usuario del alumno buscando. </p>"""
    return qw_get_alumno(dni_alumno)

@router.post("/insertar", tags = ["Alumnos"])
def insertar_alumnos(alumno: AlumnoValidator):
    """<h1>Metodo para insertar alumnos. <h1/>
    <p>Este metodo permite insertar alumnos<p/> """
    return qw_post_alumnos(alumno.dict())

@router.put("/actualizar/{dni_alumno}", tags = ["Alumnos"])
def actualizar_alumnos(dni_alumno:str,alumno: AlumnoValidator):
    """<h1>Metodo para actualiza alumnos<h1/>
    <p>Este metodo permite modificar los datos del alumno<p/>"""
    return qw_put_alumnos(dni_alumno, alumno.dict())

@router.delete("/eliminar/{dni_eliminar_alumno}", tags = ["Alumnos"])
def eliminar_alumno(dni_eliminar_alumno:str):
    """Metodo para eliminar alumnos.<h1/>
    <p> Este metodo permite eliminar alumnos<p/>"""
    return qw_delete_alumno(dni_eliminar_alumno)


