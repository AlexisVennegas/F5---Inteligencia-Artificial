from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Alumno
from fastapi.responses import JSONResponse
from classes.logger_alumnos import Logger  

def qw_get_alumnos():
    try:            
        alumnos = session.query(Alumno).all()
        if len(alumnos) == 0:
            Logger.info(f"no se han encontrado alumnos.  {alumnos}")
            return JSONResponse(content={"message": f"no se han encontrado alumnos. {e}"}, status_code=404)
        else:
            return alumnos
    except Exception as e:
        Logger.error(f"error {alumnos} al consultar alumnos.")
        return JSONResponse(content={"message": f"error al consultar alumnos. {e}"}, status_code=400)

def qw_get_alumno(dni_alumno):
    try:            
        alumno = session.query(Alumno).filter(Alumno.dni == dni_alumno).first()
        if alumno is None:
            Logger.info(f"no se han encontrado alumno.  {alumno}")
            return JSONResponse(content={"message": f"no se han encontrado alumno. {e}"}, status_code=404)
        else:
            return alumno
    except Exception as e:
        Logger.error(f"error {alumno} al consultar alumno.")
        return JSONResponse(content={"message": f"error al consultar alumnos. {e}"}, status_code=400) 
    
def qw_post_alumnos(datos_alumno):
    try:
        alumno = Alumno(**datos_alumno)
        session.add(alumno)
        session.flush()
        session.commit()
        Logger.info(f"se han grabado los datos {datos_alumno}")
        return JSONResponse({"mensaje": "Alumno creado correctamente"}, status_code=200)
    except Exception as e:
        if str(type(e)) == "<class 'sqlalchemy.exc.IntegrityError'>":
            Logger.info(f"El alumno ya existe {datos_alumno}")
            return JSONResponse({"mensaje": "El alumno ya existe"}, status_code=401) 
        else:
            Logger.error(f"Error{datos_alumno} al insertar alumnos")
            return JSONResponse(content={"message": f"error al insertar alumnos. {e}"}, status_code=400) 

def qw_put_alumnos(dni_alumno,alumno):
    try:
        alumno = Alumno(**alumno)
        data_alumno = session.query(Alumno).filter(Alumno.dni == dni_alumno).first()
        if data_alumno is None:
             Logger.info(f"se ha encontrado el alumno {dni_alumno,alumno}")
             return JSONResponse({"mensaje": "no se ha encontrado el alumno"}, status_code=404)
        data_alumno.nombre = alumno.nombre
        data_alumno.apellidos = alumno.apellidos
        data_alumno.descuento_familiar = alumno.descuento_familiar
        data_alumno.dni = alumno.dni
        data_alumno.email = alumno.email
        data_alumno.telefono = alumno.telefono
        data_alumno.nacimiento = alumno.nacimiento
        session.flush()
        session.commit()
        Logger.info(f"se han grabado los datos {dni_alumno,alumno}")
        return JSONResponse({"mensaje": "Alumno actualizado correctamente"}, status_code=200)
    except Exception as e:
        if str(type(e)) == "<class 'sqlalchemy.exc.IntegrityError'>":
            Logger.info(f"El alumno no se pudo actualizar {dni_alumno,alumno}")
            return JSONResponse({"mensaje": "El alumno no se pudo actualizar"}, status_code=400)
        else:
            Logger.error(f"error {dni_alumno,alumno} al actualizar alumno")
            return JSONResponse(content={"message": f"error al actualizar alumno. {e}"}, status_code=400) 
    
def qw_delete_alumno(dni_eliminar_alumno):
    try:
        eliminar_alumno = session.query(Alumno).filter(Alumno.dni == dni_eliminar_alumno).first()
        if eliminar_alumno is None:
            Logger.info(f"el alumno no se encontro {dni_eliminar_alumno}")
            return JSONResponse({"mensaje": "El alumno no se encontro"}, status_code=404)
        session.delete(eliminar_alumno)
        session.commit()
        Logger.info(f"Alumno eliminado correctamente {dni_eliminar_alumno}")
        return JSONResponse({"mensaje": "Alumno eliminado correctamente"}, status_code=200)
    except Exception as e:
        Logger.error(f"error {dni_eliminar_alumno} al eliminar alumno")
        return JSONResponse(content={"message": f"error al eliminar alumno. {e}"}, status_code=400)  
    