from datetime import datetime

from classes.models import Usuario, Rol
from classes.logger import Logger
from classes.encryption import Encryption

from connection.connection import *


############## USUARIOS #################
# Crear un nuevo usuario
def qw_create_usuario(usuario):
    if str(usuario.login).strip() == ''\
        or str(usuario.password).strip() == ''\
        or str(usuario.email).strip() == ''\
        or str(usuario.nombre_rol).strip() == '':
            return "Algún dato obligatorio está vacío."
    rol = session.query(Rol).filter(Rol.nombre_rol == usuario.nombre_rol).first() # Buscar el rol por su nombre
    # Si no existe el rol se obtienen un mensaje de error.
    if not rol:
        return "El rol especificado no existe."
    id_de_rol = rol.id # Obtener el ID del rol
    login_existe = session.query(Usuario).filter(Usuario.login == usuario.login).first()
    if login_existe:
        Logger.error(f"Se ha intentado grabar el usuario {usuario.login}, pero ya existe.", "./logs/logs_usuarios.txt")
        return "El login ya existe."
    email_existe = session.query(Usuario).filter(Usuario.email == usuario.email).first()
    if email_existe:
        Logger.error(f"Se ha intentado grabar el email {usuario.email}, pero ya existe.", "./logs/logs_usuarios.txt")
        return "El email ya existe."
    pw = Encryption.encrypt(usuario.password)
    # Crear el nuevo objeto de Usuario con el ID del rol
    nuevo_usuario = Usuario(login = usuario.login, email = usuario.email, password = pw, rol_id = id_de_rol, created_at = datetime.now(), updated_at = datetime.now())
    session.add(nuevo_usuario) # Agregar el nuevo usuario a la sesión
    session.flush()
    session.commit() # Realizar el commit para persistir los cambios
    Logger.info(f"Se ha grabado el usuario {usuario.login}.", "./logs/logs_usuarios.txt")
    return "Usuario creado exitosamente."

# Listar todos los usuarios, indicando a cada uno el nombre de su rol
def qw_list_usuarios():
    # Obtenemos la lista de usuarios, incluyendo el nombre de su rol
    usuarios = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).all()
    if len(usuarios) == 0:
        return "No hay usuarios registrados."
    result = []
    for usuario, nombre_rol in usuarios:
        usuario_dict = {
            "id": usuario.id,
            "login": usuario.login,
            "email": usuario.email,
            "rol": nombre_rol
        }
        result.append(usuario_dict)
    Logger.info("Se han listado los usuarios.", "./logs/logs_usuarios.txt")
    return result

# Listar los datos de un usuario localizado a partir de un dato, que puede 
# ser el id, el login o el email.
def qw_show_usuario(dato, valor):
    if str(valor).strip() == "":
        return "No se puede poner un valor vacío."
    if dato == "id":
        if not valor.isdigit():
            return "El id debe ser un dato numérico."
        valor = int(valor)
        resultado = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).filter(Usuario.id == valor).first()
    elif dato == "login":
        resultado = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).filter(Usuario.login.ilike(f"%{valor}%")).first()
    elif dato == "email":
        resultado = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).filter(Usuario.email.ilike(f"%{valor}%")).first()
    else:
        return "Dato no válido."
    if not resultado:
        Logger.error("Se ha intentado ver un usuario que no existe.", "./logs/logs_usuarios.txt")
        return "No se han encontrado usuarios."
    usuario, rol = resultado
    usuario_dict = {
        "id": usuario.id,
        "login": usuario.login,
        "email": usuario.email,
        "rol": rol
    }
    Logger.info(f"Se ha visto el usuario {usuario.login}", "./logs/logs_usuarios.txt")
    return usuario_dict

# Actualizar los datos de un usuario localizado a partir de un dato, que puede 
# ser el id, el login o el email.
def qw_update_usuario(dato, valor, usuario):
    if dato == "id":
        usuario_encontrado = session.query(Usuario).filter(Usuario.id == valor).first()
    elif dato == "login":
        usuario_encontrado = session.query(Usuario).filter(Usuario.login.ilike(f"%{valor}%")).first()
    elif dato == "email":
        usuario_encontrado = session.query(Usuario).filter(Usuario.email.ilike(f"%{valor}%")).first()
    else:
        return "Dato no válido."
    if not usuario_encontrado:
        return "No se ha encontrado el usuario."
    # Verificamos si existe el rol
    rol = session.query(Rol).filter(Rol.nombre_rol == usuario.nombre_rol).first() # Buscar el rol por su nombre
    # Si no existe el rol se obtiene un mensaje de error.
    if not rol:
        Logger.error(f"Se ha intentado actualizar el usuario {valor}, pero no existe.", "./logs/logs_usuarios.txt")
        return "El rol especificado no existe."
    rol_id = rol.id # Obtener el ID del rol
    pw = Encryption.encrypt(usuario.password) # Encriptamos la contraseña
    usuario_encontrado.login = usuario.login
    usuario_encontrado.email = usuario.email
    usuario_encontrado.password = pw
    usuario_encontrado.rol_id = rol_id
    usuario_encontrado.activo = usuario.activo
    usuario_encontrado.updated_at = datetime.now()
    session.flush()
    session.commit()
    Logger.info(f"Se ha actualizado el usuario {valor}", "./logs/logs_usuarios.txt")
    return "El usuario ha sido actualizado."

# Eliminare un usuario localizado a partir de un dato, que puede 
# ser el id, el login o el email.
def qw_delete_usuario(dato, valor):
    if dato == "id":
        usuario = session.query(Usuario).filter(Usuario.id == valor).first()
    elif dato == "login":
        usuario = session.query(Usuario).filter(Usuario.login.ilike(f"%{valor}%")).first()
    elif dato == "email":
        usuario = session.query(Usuario).filter(Usuario.email.ilike(f"%{valor}%")).first()
    else:
        return "Dato no válido."
    if not usuario:
        Logger.error(f"El usuario {valor} se ha intntado eliminar, pero no existe.", "./logs/logs_usuarios.txt")
        return "No se ha encontrado el usuario."
    session.delete(usuario)
    session.flush()
    session.commit()
    Logger.info(f"Se ha eliminado el usuario {valor}.", "./logs/logs_usuarios.txt")
    return "El usuario ha sido eliminado."
