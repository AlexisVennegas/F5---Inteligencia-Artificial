from sqlalchemy import func
from datetime import datetime

from classes.models import Grupo, Curso
from classes.logger import Logger
from connection.connection import *

############## GRUPOS #################
# Crear un nuevo grupo
def qw_create_grupo(grupo_input):
    grupo = Grupo(**grupo_input)
    if grupo.nombre_grupo.strip() == "":
        Logger.error(f"Se ha intentado grabar un grupo, pero el nombre estaba vacío.", "./logs/logs_grupos.txt")
        return "El nombre del grupo no puede estar vacío."
    grupo_existe = session.query(Grupo).filter(Grupo.nombre_grupo == grupo.nombre_grupo).first() # Obtener el rol correspondiente    
    if grupo_existe is not None:
        Logger.error(f"Se ha intentado grabar el grupo {grupo.nombre_grupo}, pero ya existe previamente.", "./logs/logs_grupos.txt")
        return "El grupo ya existe previamente."
    session.add(grupo)
    session.flush()
    session.commit()
    Logger.info(f"Se ha grabado el grupo {grupo.nombre_grupo}", "./logs/logs_grupos.txt")
    return "El grupo ha sido grabado."

# Localizar un grupo por su id o nombre
def qw_get_grupo(dato, valor):
    if str(valor).strip() == "":
        Logger.error("Se ha intentado obtener un log con el valor vacío.", "./logs/logs_grupos.txt")
        return "No se puede procesar un valor vacío."
    if dato == "id":
        if not valor.isdigit():
            return "El id debe ser numérico."
        id = int(valor)
        grupo = session.query(Grupo).get(id)
        if grupo is None:
            return "Error: El grupo especificado no existe."
    elif dato == "nombre":
        grupo = session.query(Grupo).filter(Grupo.nombre_grupo == valor).first() # Obtener el grupo correspondiente    
        if grupo is None:
            Logger.error(f"El grupo {valor} no existe", "./logs/logs_grupos.txt")
            return "Error: El grupo especificado no existe."
    else:
        return "El tipo de dato especificado no existe."
    Logger.info(f"Se han obtenido los datos del grupo {valor}.", "./logs/logs_grupos.txt")
    return grupo

# Listar todos los grupos.
def qw_list_grupos():
    grupos = session.query(Grupo).all()
    if len(grupos) == 0:
        Logger.error("Se han intentado listar los grupos, pero no los hay.", "./logs/logs_grupos.txt")
        return "No se han encontrado grupos."
    for grupo in grupos:
        num_cursos = session.query(func.count(Curso.id)).filter(Curso.id_grupo == grupo.id).scalar()
        grupo.num_cursos = num_cursos
        Logger.info("Se han listado los grupos.", "./logs/logs_grupos.txt")
    return grupos

# Actualizar un grupo por id o por su nombre actual.
def qw_update_grupo(dato, valor, nuevo_nombre):
    if dato == "id":
        if not valor.isdigit():
            return "El id debe ser numérico."
        id = int(valor)
        grupo = session.query(Grupo).get(id)
        if grupo is None:
            return "Error: El grupo especificado no existe."
    elif dato == "nombre":
        grupo = session.query(Grupo).filter(Grupo.nombre_grupo == valor).first() # Obtener el rol correspondiente    
        if grupo is None:
            return "Error: El grupo especificado no existe."
        id = grupo.id
    else:
        Logger.error(f"Se ha intentado actualizar el grupo {valor}, pero no existe.", "./logs/logs_grupos.txt")
        return "El tipo de dato especificado no existe."
    # Actualizar el nombre del rol
    grupo.nombre_grupo = nuevo_nombre
    grupo.updated_at = datetime.now()
    session.flush()
    session.commit() # Guardar los cambios en la base de datos
    Logger.info(f"Se ha actualizado el grupo {valor}", "./logs/logs_grupos.txt")
    return "El grupo ha sido actualizado."

# Borrar un grupo por su id o por su nombre si ningún curso lo tiene asignado
def qw_delete_grupo(dato, valor):
    if dato == "id":
        if not valor.isdigit():
            return "El id debe ser numérico."
        id = int(valor)
        grupo = session.query(Grupo).get(id)
        if grupo is None:
            return "Error: El grupo especificado no existe."
    elif dato == "nombre":
        grupo = session.query(Grupo).filter(Grupo.nombre_grupo == valor).first() # Obtener el grupo correspondiente    
        if grupo is None:
            return "Error: El grupo especificado no existe."
        id = grupo.id
    else:
        Logger.error(f"Se ha intentado borrar el grupo {valor}, pero no existe.", "./logs/logs_grupos.txt")
        return "El tipo de dato especificado no existe."
    # Verificar si existen cursos con el grupo especificado
    cursos_con_grupo = session.query(func.count(Curso.id)).filter(Curso.id_grupo == id).scalar()
    if cursos_con_grupo > 0:
        Logger.error(f"Se ha intentado borrar el grupo {valor}, pero tiene cursos asociados.", "./logs/logs_grupos.txt")
        return "Error: No se puede borrar el grupo porque existen cursos relacionados."
    # Si no hay cursos relacionados, proceder a borrar el rol
    session.delete(grupo)
    session.flush()
    session.commit()
    Logger.info(f"Se ha eliminado el grupo {valor}.", "./logs/logs_grupos.txt")
    return "El grupo ha sido eliminado."


