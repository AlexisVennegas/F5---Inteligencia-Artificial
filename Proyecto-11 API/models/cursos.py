from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from models.grupos import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Curso(Base): # Tabla de cursos
    __tablename__ = "cursos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_curso = Column("nombre_curso", String, nullable = False)
    precio = Column("precio", Float(precision = 5, asdecimal = True, decimal_return_scale = 2), nullable = False)
    id_grupo = Column("id_grupo", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #grupo = relationship("Grupo")  # Establecer la relación con la clase Grupo
    #niveles = relationship("Nivel", secondary = cursos_niveles, backref = "cursos")
    #profesores = relationship("Profesor", secondary = cursos_profesores, backref = "cursos")
    #alumnos = relationship("Alumno", secondary = estudios, backref = "cursos_alumnos")
    #titulares = relationship("Profesor", secondary = estudios, backref = "alumnos_profesores")
    
    def __init__(self, nombre_curso, precio, id_grupo, created_at = datetime.now(), updated_at = datetime.now()):
        self.nombre_curso = nombre_curso
        self.precio = precio
        self.id_grupo = id_grupo
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"Curso {self.id} de {self.nombre_curso}. Pertenece al grupo {self.grupo.nombre_grupo}.El precio es {self.precio}"

