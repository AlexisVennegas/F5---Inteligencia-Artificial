import json
import pymysql
import streamlit as st
from decouple import config

# Función para ejecutar un archivo SQL
def execute_sql_file(connection, filename):
    try:
        with open(filename, "r") as sql_file:
            sql_script = sql_file.read()
            # Separa las instrucciones SQL en una lista usando el punto y coma como delimitador
            sql_statements = sql_script.split(';')
            cursor = connection.cursor()

            for sql_statement in sql_statements:
                if sql_statement.strip():  # Verifica que no sea una línea vacía
                    cursor.execute(sql_statement)

            connection.commit()
    except pymysql.Error as e:
        st.error(f"Error al ejecutar el archivo SQL: {e}")
    finally:
        cursor.close()

        
# Función para establecer la conexión
def establish_connection():
    timeout = 10  # Establece un tiempo de espera de conexión
    try:
        conn = pymysql.connect(
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            db=config('DB_NAME', default='airline'),
            host=config('DB_HOST', default='localhost'),
            password=config('DB_PASSWORD', default=''),
            read_timeout=timeout,
            port=config('DB_PORT', default='3306', cast=int),
            user=config('DB_USER', default='root'),
            write_timeout=timeout,
        )
        print("Conexión establecida correctamente")
        return conn
    except pymysql.Error as e:
        st.error(f"Error al establecer la conexión: {e}")
        return None

def insert_data(conn, data):
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO data_client (id_passenger, Gender, Customer_Type, Age, Type_of_Travel, 
            Class, Flight_distance, Inflight_wifi_service, 
            datc, Ease_of_Online_booking, Gate_location, Food_and_drink,
            Online_boarding, Departure_delay_minutes, Seat_comfort, 
            Inflight_entertainment, Onboard_service, Leg_room_service, Baggage_handling, 
            Checkin_service, Inflight_service, Cleanliness, Arrival_delay_minutes) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        query_predict = """
            INSERT INTO predictions (id_passenger, predict)
            VALUES (%s, %s)
        """
        
        cursor.execute(query, (
            data["id_passenger"], data["Gender"], data["Customer_Type"], data["Age"], data["Type_of_Travel"],
            data["Class"], data["Flight_distance"], data["Inflight_wifi_service"], data["datc"],
            data["Ease_of_Online_booking"], data["Gate_location"], data["Food_and_drink"], data["Online_boarding"],
            data["Departure_delay_minutes"], data["Seat_comfort"], data["Inflight_entertainment"], data["Onboard_service"],
            data["Leg_room_service"], data["Baggage_handling"], data["Checkin_service"], data["Inflight_service"],
            data["Cleanliness"], data["Arrival_delay_minutes"]
        ))
        
        cursor.execute(query_predict, (
            data["predict"]
        ))
        
        conn.commit()
    except pymysql.Error as e:
        st.error(f"Error al insertar los datos: {e}")

