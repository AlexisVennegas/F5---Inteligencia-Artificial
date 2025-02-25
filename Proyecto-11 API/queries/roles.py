from sqlalchemy import func
from datetime import datetime

from classes.models import Rol, Usuario
from classes.logger import Logger
from connection.connection import *

############## ROLES #################
# Crear un nuevo rol
def qw_create_rol(rol_input):
    if str(rol_input["nombre_rol"]).strip() == "":
        return "El nombre de rol no puede estar vacío."
    try:
        rol = Rol(**rol_input)
        session.add(rol)
        session.flush()
        session.commit()
        out = "El rol ha sido grabado."
        Logger.info(f"Se ha grabado el rol {rol.nombre_rol}", "./logs/logs_roles.txt")
    except Exception as e:
        if str(type(e)) == "<class 'sqlalchemy.exc.IntegrityError'>":
            out = "El rol ya existe previamente."
            Logger.error(f"El rol {rol.nombre_rol} se ha intentado grabar, pero ya existía", "./logs/logs_roles.txt")
        else:
            out = f"No se ha podido grabar el rol.{e}"
        session.rollback()
    return out

# Localizar un rol por su id
def qw_get_rol(dato, valor):
    if str(valor).strip() == "":
        return "El valor no puede ser una cadena vacía."
    if dato == "id":
        if not valor.isdigit():
            return "El id debe ser numérico."
        id = int(valor)
        rol = session.query(Rol).get(id)
        if rol is None:
            Logger.error(f"Se ha intentado mostrar el rol {valor}, pero no existe.", "./logs/logs_roles.txt")
            return "Error: El rol especificado no existe."
    elif dato == "nombre":
        rol = session.query(Rol).filter(Rol.nombre_rol == valor).first() # Obtener el rol correspondiente    
        if rol is None:
            Logger.error(f"Se ha intentado mostrar el rol {valor}, pero no existe.", "./logs/logs_roles.txt")
            return "Error: El rol especificado no existe."
    else:
        return "El tipo de dato especificado no existe."
    Logger.info(f"Se ha mostrado el rol {valor}.", "./logs/logs_roles.txt")
    return rol

# Listar todos los roles.
def qw_list_roles():
    roles = session.query(Rol).all()
    if len(roles) == 0:
        Logger.error("Se han intentado mostrar los roles, pero no hay ninguno.", "./logs/logs_roles.txt")
        return "No se han encontrado roles."
    for rol in roles:
        num_usuarios = session.query(func.count(Usuario.id)).filter(Usuario.rol_id == rol.id).scalar()
        rol.num_usuarios = num_usuarios
    Logger.info("Se han listado los roles.", "./logs/logs_roles.txt")
    return roles

# Actualizar un rol por id o por su nombre actual.
def qw_update_rol(dato, valor, nuevo_nombre):
    if dato == "id":
        if not valor.isdigit():
            return "El id debe ser numérico."
        id = int(valor)
        rol = session.query(Rol).get(id)
        if rol is None:
            return "Error: El rol especificado no existe."
    elif dato == "nombre":
        rol = session.query(Rol).filter(Rol.nombre_rol == valor).first() # Obtener el rol correspondiente    
        if rol is None:
            return "Error: El rol especificado no existe."
        id = rol.id
    else:
        Logger.error("Se ha producido un error en la actualización de roles.", "./logs/logs_roles.txt")
        return "El tipo de dato especificado no existe."
    # Actualizar el nombre del rol
    rol.nombre_rol = nuevo_nombre
    rol.updated_at = datetime.now()
    session.flush()
    session.commit() # Guardar los cambios en la base de datos
    Logger.info(f"Se ha actualizado el rol {valor}.", "./logs/logs_roles.txt")
    return "El rol ha sido actualizado."

# Borrar un rol por su id o por su nombre si ningún usuario lo tiene asignado
def qw_delete_rol(dato, valor):
    if dato == "id":
        if not valor.isdigit():
            return "El id debe ser numérico."
        id = int(valor)
        rol = session.query(Rol).get(id)
        if rol is None:
            return "Error: El rol especificado no existe."
    elif dato == "nombre":
        rol = session.query(Rol).filter(Rol.nombre_rol == valor).first() # Obtener el rol correspondiente    
        if rol is None:
            return "Error: El rol especificado no existe."
        id = rol.id
    else:
        Logger.error(f"No existe el rol {valor}.", "./logs/logs_roles.txt")
        return "El tipo de dato especificado no existe."
    # Verificar si existen usuarios con el rol especificado
    usuarios_con_rol = session.query(func.count(Usuario.id)).filter(Usuario.rol_id == id).scalar()
    if usuarios_con_rol > 0:
        Logger.error(f"Se ha intentado borrar el rol {valor}, pero tiene usuarios asociados.", "./logs/logs_roles.txt")
        return "Error: No se puede borrar el rol porque existen usuarios relacionados."
    # Si no hay usuarios relacionados, proceder a borrar el rol
    session.delete(rol)
    session.flush()
    session.commit()
    Logger.info(f"Se ha elimado el rol {valor}.", "./logs/logs_roles.txt")
    return "El rol ha sido eliminado."

