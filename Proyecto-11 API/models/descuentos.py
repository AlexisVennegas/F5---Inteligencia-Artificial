from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Descuento(Base):
    __tablename__ = "descuentos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    concepto = Column("concepto", String, nullable = False)
    porcentaje = Column("porcentaje", Float(precision = 5, asdecimal = True, decimal_return_scale = 2), nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #estudios = relationship("Estudio", secondary=estudios, backref="descuentos")

    def __init__(self, concepto, porcentaje, created_at = datetime.now(), updated_at = datetime.now()):
        self.concepto = concepto
        self.porcentaje = porcentaje
        self.created_at = created_at
        self.updated_at = updated_at
 