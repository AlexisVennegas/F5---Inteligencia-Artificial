from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Curso, Grupo
from classes.models import Curso
from fastapi.responses import JSONResponse
from classes.logger_cursos import Logger


############## CURSOS #################
# Crear un nuevo curso
def qw_create_curso(curso_input):
    try:
        curso_existe = session.query(Curso).filter(Curso.nombre_curso == curso_input["nombre_curso"]).first()
        if curso_existe is not None:
            Logger.error(f"El curso {curso_input['nombre_curso']} se ha intentado grabar, pero ya existía")
            return JSONResponse(content={"message": "Error: El curso especificado ya existe."}, status_code=404)
        curso = Curso(**curso_input)
        session.add(curso)
        session.flush()
        session.commit()
    except Exception as e:
        session.rollback()
        Logger.error(f"No se ha podido crear el curso {curso_input['nombre_curso']}.{e}")
        return JSONResponse(content={"message": f"No se ha podido crear el curso.{e}"}, status_code=400)
    Logger.info(f"El curso {curso_input['nombre_curso']} ha sido creado.")
    return JSONResponse(content={"message": "El curso ha sido creado."}, status_code=202)

# mostrar todos los cursos
def qw_get_cursos():
    cursos = session.query(Curso).all()
    if len(cursos) == 0:
        Logger.error("No se han encontrado cursos.")
        return "No se han encontrado cursos."
    cursos_dict = []
    for curso in cursos:
        grupo = session.query(Grupo).filter(Grupo.id == curso.id_grupo).first()
        curso_dict = {
            "id": curso.id,
            "nombre_curso": curso.nombre_curso,
            "nombre_grupo": grupo.nombre_grupo,
            "precio": curso.precio,
            "created_at": curso.created_at,
            "updated_at": curso.updated_at
        }
        cursos_dict.append(curso_dict)
    Logger.info("Se han encontrado cursos.")   
    return cursos_dict

# funcion para mostrar un solo curso
def qw_mostrar_curso(nombre_del_curso):
    curso = session.query(Curso).filter(Curso.nombre_curso == nombre_del_curso).first()
    if curso is None:
        Logger.error(f"El curso {nombre_del_curso} no existe.")
        return "Error: El curso especificado no existe."

# mostrar todos los cursos
def qw_get_cursos():
    try:
        cursos = session.query(Curso).all()
        if len(cursos) == 0:
            Logger.error("No se han encontrado cursos.")
            return JSONResponse(content={"message": "No hay cursos."}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido mostrar los cursos.{e}"}, status_code=400)
    Logger.info("Se han encontrado cursos.")
    return cursos

# funcion para mostrar un solo curso
def qw_get_curso_unique(nombre_del_curso):
    try:
        curso = session.query(Curso).filter(Curso.nombre_curso == nombre_del_curso).first()
        if curso is None:
            Logger.error(f"El curso {nombre_del_curso} no existe.")
            return JSONResponse(content={"message": "Error: El curso especificado no existe."}, status_code=404)
    except Exception as e:
        Logger.error(f"No se ha podido mostrar el curso {nombre_del_curso}.{e}")
        return JSONResponse(content={"message": f"No se ha podido mostrar el curso.{e}"}, status_code=400)
    Logger.info(f"Se ha encontrado el curso {nombre_del_curso}.")
    return curso

# funcion para modificar un curso
def qw_update_curso(nombre_del_curso, nuevo_nombre, nuevo_precio, nuevo_grupo):
    try:
        curso = session.query(Curso).filter(Curso.nombre_curso == nombre_del_curso).first()
        if curso is None:
            Logger.error(f"El curso  no existe.")
            return JSONResponse(content={"message": "Error: El curso especificado no existe."}, status_code=404)
        curso.nombre_curso = nuevo_nombre
        curso.precio = nuevo_precio
        curso.id_grupo = nuevo_grupo
        session.commit()
    except Exception as e:
        Logger.error(f"No se ha podido modificar el curso {nombre_del_curso}.{e}")   
        return JSONResponse(content={"message": f"No se ha podido modificar el curso.{e}"}, status_code=400)
    Logger.info(f"El curso {nombre_del_curso} ha sido modificado.")
    return JSONResponse(content={"message": "El curso ha sido modificado."}, status_code=202)

# funcion para borrar un curso
def qw_delete_curso(nombre_del_curso):
    try:
        curso = session.query(Curso).filter(Curso.nombre_curso == nombre_del_curso).first()
        if curso is None:
			# segundo paso en el return metemos el JSONResponse() dentro el mensaje y despues del status code
            Logger.error(f"El curso {nombre_del_curso} no existe.")
            return JSONResponse(content={"message": "Error: El curso especificado no existe."}, status_code=404)
        session.delete(curso)
        session.commit()    
    except Exception as e:
        Logger.error(f"No se ha podido borrar el curso {nombre_del_curso}.{e}")
        return JSONResponse(content={"message": f"No se ha podido borrar el curso.{e}"}, status_code=400)
    Logger.info(f"El curso {nombre_del_curso} ha sido borrado.")
    return JSONResponse(content={"message": "El curso ha sido borrado."}, status_code=202)