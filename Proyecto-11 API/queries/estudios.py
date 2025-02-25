from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Estudios
from classes.models import Alumno
from classes.models import Curso
from fastapi.responses import JSONResponse
from fastapi import status

def qw_create_compile(compile_input):
    try:
        information = Estudios(**compile_input)
        dni_select = information.dni_alumno
        alumno = session.query(Alumno).filter(Alumno.dni == dni_select).first()
        if alumno is None:
            return "El alumno no existe."
        session.add(information)
        session.flush()
        session.commit()
        out = "El alumno ha sido grabado."
    except Exception as e:
        return f"No se ha podido grabar el alumno.{e}"
    return out

def qw_mostrar_inscripciones():
    information = session.query(Estudios).all()
    if len(information) == 0:
        return "No se han encontrado alumnos."
    return information



# funcion para inscribir a un nuevo alumno y calcular el precio de la inscripcion
def qw_create_compile(compile_input):
    try:
        information = Estudios(**compile_input)
        dni_select = information.dni_alumno
        alumno = session.query(Alumno).filter(Alumno.dni == dni_select).first()
        if alumno is None:
            return "El alumno no existe."
        curso_actual = information.nombre_curso
        curso = session.query(Curso).filter(Curso.nombre_curso == curso_actual).first()
        grupo_select = session.query(Curso).filter(Curso.nombre_curso == information.nombre_curso).first()
        # return grupo_select.id_grupo
        if curso is None:
            return "El curso no existe."
        precio_clase = curso.precio
        information.precio = precio_clase
        information.grupo = grupo_select.id_grupo
        session.add(information)
        session.flush()
        session.commit()
        out = f"El alumno ha sido grabado. Precio de la clase: {precio_clase}"
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido grabar el alumno. {e}"}, status_code=status.HTTP_404_NOT_FOUND)
    return out

def qw_mostrar_compile():
    information = session.query(Estudios).all()
    if len(information) == 0:
        return "No se han encontrado alumnos."
    return information

# funcion para inscribir a un nuevo alumno y calcular el precio de la inscripcion
from sqlalchemy.orm import sessionmaker

def wq_get_descuentos(dni_alumno):
    Session = sessionmaker(bind=engine)
    session = Session()

    count_group_one = 0
    count_group_two = 0
    count_group_three = 0
    descuentos = ["0,5", "0,25"]

    # comprobacion de que el alumno existe
    information = session.query(Estudios).filter(Estudios.dni_alumno == dni_alumno).all()
    check_grupo = session.query(Curso).all()

    

    for info in information:
        if (info.nombre_curso == "Bachata" or info.nombre_curso == "Salsa" or info.nombre_curso == 'Kizomba' or info.nombre_curso == "Role Rotation") and (info.grupo == "Relax"):
            count_group_one += 1
        if (info.nombre_curso == "Estilo para todos" or info.nombre_curso == "Zouk") and (info.grupo == "Chicha"):
            count_group_two += 1
        if (info.nombre_curso == "Yoga" or info.nombre_curso == "Pilates") and (info.grupo == "Dem"):
            count_group_three += 1

    # return count_group_one, count_group_two, count_group_three

    # GENERA EL DESCUENTO PARA LA PRIMERA CLASE
    if count_group_one == 4:
        for info in information:
            if info.grupo == "Relax":
                info.precio = 17.50
    elif count_group_one == 3:
        for info in information:
            if info.grupo == "Relax":
                info.precio = 20.41
    elif count_group_one == 2:
        for info in information:
            if info.grupo == "Relax":
                info.precio = 26,25
    elif count_group_one == 1:
        for info in information:
            if info.grupo == "Relax":
                info.precio = 35.00

    # GENERA EL DESCUENTO PARA LA SEGUNDA CLASE
    if count_group_two == 4:
        for info in information:
            if info.grupo == "Chicha":
                info.precio = 40.00
    elif count_group_two == 3:
        for info in information:
            if info.grupo == "Chicha":
                info.precio = 23.33
    elif count_group_two == 2:
        for info in information:
            if info.grupo == "Chicha":
                info.precio = 30.00
    elif count_group_two == 1:
        for info in information:
            if info.grupo == "Chicha":
                info.precio = 40.00

    
    # GENERA EL DESCUENTO PARA LA TERCERA CLASE
    if count_group_three == 4:
        for info in information:
            if info.grupo == "Dem":
                info.precio = 40.00
    elif count_group_three == 3:
        for info in information:
            if info.grupo == "Dem":
                info.precio = 23.33
    elif count_group_three == 2:
        for info in information:
            if info.grupo == "Dem":
                info.precio = 30.00
    elif count_group_three == 1:
        for info in information:
            if info.grupo == "Dem":
                info.precio = 40.00

    # Commit the changes to the database
    session.commit()

    # si el alumno no existe, se devuelve un mensaje de error
    if information is None or len(information) == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No se han encontrado alumnos."})
    
    # se pregunta si el alumno tiene descuento familiar
    check_familiar = session.query(Alumno).filter(Alumno.dni == dni_alumno).first()
    total_precio = 0

    # se calcula el precio total de los cursos
    for info in information:
        total_precio += info.precio

    # si el alumno tiene descuento familiar, se le aplica un 10% de descuento
    if check_familiar.descuento_familiar == 1:
        descuento = total_precio * 0.1
        total_precio -= descuento

    # se devuelve el precio total
    if check_familiar:
        return f"Descuento familiar: 10%, el total a pagar es de {total_precio} euros"
    else:
        return f"El total a pagar es de {total_precio} euros"






# funcion para eliminar una inscripcion
def qw_delete_inscripcion(dni_alumno, nombre_curso, nivel):
    try:
        information = session.query(Estudios).filter(Estudios.dni_alumno == dni_alumno, Estudios.nombre_curso == nombre_curso, Estudios.nivel == nivel).first()
        session.delete(information)
        session.commit()
        out = "El alumno ha sido eliminado."
    except Exception as e:
        return f"No se ha podido eliminar el alumno.{e}"
    return out   
