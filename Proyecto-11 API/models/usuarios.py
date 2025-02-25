from sqlalchemy import ForeignKey, Column, CheckConstraint, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column("id", Integer, primary_key = True, nullable = False)
    login = Column("login", String, nullable = False)
    email = Column("email", String, nullable = False)
    password = Column("password", String, nullable = False)
    rol_id = Column("rol_id", Integer, nullable = False)
    activo = Column("activo", Integer,\
                                CheckConstraint('activo IN (0, 1)',\
                                name = 'valid_activo'), default = 1)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)

    def __init__(self, login, email, password, rol_id, created_at, updated_at):
        self.login = login
        self.email = email
        self.password = password
        self.rol_id = rol_id
        self.created_at = created_at
        self.updated_at = updated_at        
    
    def __repr__(self):
        return f"Usuario {self.id} tiene el login {self.login}."
