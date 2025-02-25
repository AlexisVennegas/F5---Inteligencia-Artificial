from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class Profesor(Base): # Tabla de profesores
    __tablename__ = "profesores"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_profesor = Column("nombre_profesor", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #cursos = relationship("Curso", secondary = cursos_profesores, backref = "profesores")
    #alumnos = relationship("Alumno", secondary = estudios, backref = "alumnos_profesores")
    #temarios = relationship("Curso", secondary = estudios, backref = "cursos_profesores")

    def __init__(self, nombre_profesor, created_at = datetime.now(), updated_at = datetime.now()):
        self.nombre_profesor = nombre_profesor
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"Profesor {self.id} se llama {self.nombre_profesor}."


