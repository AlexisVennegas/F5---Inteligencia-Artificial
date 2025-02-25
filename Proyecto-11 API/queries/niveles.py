from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Nivel
from fastapi.responses import JSONResponse


def qw_get_niveles():
    try:
        niveles = session.query(Nivel).all()
        if len(niveles) == 0:
            return JSONResponse(content={"message": "No se han encontrado niveles"}, status_code=404)
        else:
            return niveles
    except Exception as e:
        return JSONResponse(content={"message":f"Error al consutar niveles .{e}"}, status_code=400) 
    
def qw_post_niveles(nivel_input):
    try:
        nivel_datos = Nivel(**nivel_input)
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nivel_datos.nivel).first()
        if nivel_existe is not None:
            return JSONResponse(content={"message":"El nivel ya existe"}, status_code=400) 
        session.add(nivel_datos)
        session.flush()
        session.commit()
        return JSONResponse(content={"message": "El Nivel ha sido grabado"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message":f"Error al consutar niveles .{e}"}, status_code=400)

def qw_put_niveles(nombre_nivel, nivel_nuevo):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        nivel_existe.nivel = nivel_nuevo
        session.commit()
        return JSONResponse(content={"message": "El Nivel ha sido actualizado."}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message":f"Error al actualizar los niveles .{e}"}, status_code=400)

def qw_delete_niveles(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        session.delete(nivel_existe)
        session.commit()
        return JSONResponse(content={"message": "El Nivel ha sido apagado."}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message":f"Error al apagar los niveles .{e}"}, status_code=400)

def qw_get_nivel(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        return nivel_existe
    except Exception as e:
        return JSONResponse(content={"message":f"Error al consultar los niveles .{e}"}, status_code=400)