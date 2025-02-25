from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.models import Base
import json

with open("./conf/db.json", "r") as conn_data_file:
    data = json.load(conn_data_file)
# Creamos la referencia al motor de base de datos
engine = create_engine(f"{data['MOTOR']}://{data['USER']}:{data['PASSWORD']}@{data['SERVER']}/{data['DATABASE']}", echo = True)
Base.metadata.create_all(bind=engine)

# Creamos la sesión para luego poder pasar las consultas.
Session = sessionmaker(bind = engine)
session = Session()
