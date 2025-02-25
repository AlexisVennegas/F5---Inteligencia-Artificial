from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

from typing import Optional

class RolValidator(BaseModel):
    nombre_rol: str

class UserValidator(BaseModel):
    login: str
    email: str
    password: str
    nombre_rol: str
    activo: Optional [int] = 1
class AlumnoValidator(BaseModel):
    nombre: str
    apellidos: str
    descuento_familiar: int
    dni: str
    email: str
    telefono: str
    nacimiento: datetime
class NivelValidator(BaseModel):
    nivel: str
    
class GrupoValidator(BaseModel):
    nombre_grupo: str

class ProfesorValidator(BaseModel):
    nombre_profesor : str

class CursoValidator(BaseModel):
    nombre_curso : str
    precio : float
    id_grupo : str
    
class InscripcionValidator(BaseModel):
    dni_alumno : str
    nombre_curso : str
    nivel : str
    profesor : str