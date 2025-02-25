from sqlalchemy import ForeignKey, Table, Column, CheckConstraint, String, Integer, Float, DateTime, Boolean, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

from models.alumnos import Alumno
from models.cursos import Curso
from models.descuentos import Descuento
from models.grupos import Grupo
from models.niveles import Nivel
from models.profesores import Profesor
from models.roles import Rol
from models.usuarios import Usuario
from models.estudios import Estudios


Base = declarative_base()

'''
# DEFINIMOS LAS TABLAS "PIVOTE" PARA LAS RELACIONES MUCHOS A MUCHOS
# Definir la tabla pivote cursos_niveles
cursos_niveles = Table('cursos_niveles', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('id_curso', Integer, ForeignKey('cursos.id')),
    Column('id_nivel', Integer, ForeignKey('niveles.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
# Definir la tabla pivote cursos_profesores
cursos_profesores = Table('cursos_profesores', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('id_curso', Integer, ForeignKey('cursos.id')),
    Column('id_profesor', Integer, ForeignKey('profesores.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
# Definir la tabla pivote estudios (alumnos, cursos, profesores)
estudios = Table('estudios', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('id_alumno', Integer, ForeignKey('alumnos.id')),
    Column('id_curso', Integer, ForeignKey('cursos.id')),
    Column('id_profesor', Integer, ForeignKey('profesores.id')),
    Column('fecha_inicio', DateTime),
    Column('fecha_final', DateTime),
    Column('relacion_activa', Integer, default = 0),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
# Definir la tabla pivote entre estudios y descuentos
estudios_descuentos = Table('estudios_descuentos', Base.metadata,
    Column('id_estudio', Integer, ForeignKey('estudios.id')),
    Column('id_descuento', Integer, ForeignKey('descuentos.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
'''
   
