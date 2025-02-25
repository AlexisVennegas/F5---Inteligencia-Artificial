from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Grupo(Base): # Tabla de grupos
    __tablename__ = "grupos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_grupo = Column("nombre_grupo", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    def __init__(self, nombre_grupo, created_at = datetime.now(), updated_at = datetime.now()):
        self.nombre_grupo = nombre_grupo
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"Grupo {self.id} llamado {self.nombre_grupo}."

