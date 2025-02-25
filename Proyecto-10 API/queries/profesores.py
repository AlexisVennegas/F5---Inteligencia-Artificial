from sqlalchemy import func
from datetime import datetime
from connection.connection import * 
from classes.models import Profesor
from fastapi.responses import JSONResponse
from classes.logger_profesores import Logger


#Ejecuta la búsqueda de todos los profesores de la bbdd
def qw_get_profesores():
    try:
        profesores = session.query(Profesor).all()
        if len(profesores) == 0:
            Logger.warning(f"No se han encontrado a los profesores. {profesores}")
            return JSONResponse(content={"message": "Error: No Existe la tabla"}, status_code=404)
        
    except Exception as e:
        Logger.error(f"Error {profesores} al consultar profesores.")
        return JSONResponse(content={"message": f"No se ha encontrado la lista de profesores.{e}"}, status_code=400)
    Logger.info(f"La lista de profesores ha sido encontrada.{profesores}")
    return JSONResponse(content={"message": f"La Lista de profesores ha sido encontrada: {profesores  }" }, status_code=202)


#Ejecuta la búsqueda de UN SOLO profesor
def qw_list_profesores(nombre_profe):
    try:            
        profesores = session.query(Profesor).filter(Profesor.nombre_profesor == nombre_profe).first()
        if profesores is None:
            Logger.warning(f"El profesor/a especificado no existe {profesores}")
            return JSONResponse(content={"message": "Error: El profesor/a especificado no existe."}, status_code=404)
    except Exception as e:
        Logger.error(f"Error {profesores} al consultar el profesor.")
        return JSONResponse(content={"message": f"No se ha podido encontrar el profesor {e}"}, status_code=400)
    Logger.info(f"El profesor ha sido encontrado. {profesores}")
    return JSONResponse(content={"message": f"El Profesor ha sido encontrado {profesores}"}, status_code=202)

#Ejecuta el grabado de los profesores.
def qw_post_profesores(datos_profesor):
    try:
        profesor = Profesor(**datos_profesor)
        profesor_existe = session.query(Profesor).filter(Profesor.nombre_profesor == profesor.nombre_profesor).first()
        if profesor_existe is not None:
            Logger.warning(f"El profesor/a ya existe. {profesor}")
            return JSONResponse(content={"message": "El profesor/a ya existe."}, status_code=404)
        session.add(profesor)
        session.flush()
        session.commit()    
    except Exception as e:
        Logger.error(f"El profesor no ha podido ser grabado. {profesor}")
        return JSONResponse(content={"message": f"El profesor no ha podido ser grabado.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido grabado. El/la {profesor}")
    return JSONResponse(content={"message": "El profesor/a ha sido grabado."}, status_code=202)


#Modifica los profesores 
def qw_put_profesores(nombre_profesor, nuevo_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == nombre_profesor).first()
        if profesor is None:
            Logger.warning(f"El profesor ya existe. {profesor}")
            return JSONResponse(content={"message": f"Error: El profesor ya existe. {profesor}"}, status_code=404)
        profesor.nombre_profesor = nuevo_profesor
        session.commit()
        
    except Exception as e:
        Logger.error(f"No se ha podido añadir el profesor/a. {profesor}")
        return JSONResponse(content={"message": f"No se ha podido añadir el profesor/a.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido modificado. {profesor}")
    return JSONResponse(content={"message": f"El profesor/a ha sido modificado/a: {profesor}"}, status_code=202)




#Ejecuta la eliminación de profesores
def qw_delete_profesores(borrar_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == borrar_profesor).first()
        if profesor is None:
            Logger.warning(f"El profesor especificado no existe. {profesor}")
            return JSONResponse(content={"message": "Error: El profesor especificado no existe."}, status_code=404)
        session.delete(profesor)
        session.commit()
  
    except Exception as e:
        Logger.error(f"No se ha podido borrar el profesor/a: {profesor}")
        return JSONResponse(content={"message": f"No se ha podido borrar el profesor/a.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido borrado. {profesor}")
    return JSONResponse(content={"message": f"{profesor} ha sido borrado."}, status_code=202)
