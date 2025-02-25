from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Nivel(Base): # Tabla de niveles
    __tablename__ = "niveles"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nivel = Column("nivel", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #cursos = relationship("Curso", secondary = cursos_niveles, backref = "niveles")

    def __init__(self, nivel, created_at = datetime.now(), updated_at = datetime.now()):
        self.nivel = nivel
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"Nivel {self.id} llamado {self.nivel}."

