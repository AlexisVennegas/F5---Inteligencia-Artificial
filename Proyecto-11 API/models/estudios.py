from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from models.grupos import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Estudios(Base): # Tabla de cursos
    __tablename__ = "estudios"
    id = Column("id", Integer, primary_key = True, nullable = False)
    dni_alumno = Column("dni_alumno", String, nullable = False)
    nombre_curso = Column("nombre_curso", String, nullable = False)
    nivel = Column("nivel", String,  nullable = False)
    profesor = Column("profesor", String, nullable = False)
    precio = Column("precio", Float,  nullable = False)
    fecha_inicio = Column("fecha_inicio", DateTime, nullable = False)
    fecha_fin = Column("fecha_final", DateTime, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    grupo = Column("grupo", String, nullable=False)
    
    #grupo = relationship("Grupo")  # Establecer la relación con la clase Grupo
    #niveles = relationship("Nivel", secondary = cursos_niveles, backref = "cursos")
    #profesores = relationship("Profesor", secondary = cursos_profesores, backref = "cursos")
    #alumnos = relationship("Alumno", secondary = estudios, backref = "cursos_alumnos")
    #titulares = relationship("Profesor", secondary = estudios, backref = "alumnos_profesores")
    
    def __init__( self, dni_alumno, nombre_curso, nivel, profesor):
        self.dni_alumno = dni_alumno
        self.nombre_curso = nombre_curso
        self.nivel = nivel
        self.profesor = profesor
        
