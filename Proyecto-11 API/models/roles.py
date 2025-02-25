from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Rol(Base):
    __tablename__ = "roles"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_rol = Column("nombre_rol", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    def __init__(self, nombre_rol, created_at = datetime.now(), updated_at = datetime.now()):
        self.nombre_rol = nombre_rol
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"Rol {self.id} se llama {self.nombre_rol}."
