from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from models.grupos import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Compile(Base):
    __tablename__ = "compile"
    id = Column("id", Integer, primary_key = True, nullable = False)
    dni_usuario = Column("dni_usuario", String, nullable = False)
    # check_familiar = Column("check_familiar", Integer, nullable = False)
    cursos = Column("cursos", String, nullable = False)
    nivel = Column("nivel", String, nullable = False)
    profesor = Column("profesor", String, nullable = False)
    precio = Column("precio", Float, nullable = False)


    def __init__(self, dni_usuario, cursos, nivel, profesor):
        self.dni_usuario = dni_usuario
        # self.check_familiar = check_familiar
        self.cursos = cursos
        self.nivel = nivel
        self.profesor = profesor

    def __repr__(self):
        return f"Compile {self.id} de {self.id_usuario}. Pertenece al grupo, El precio es {self.cursos}"