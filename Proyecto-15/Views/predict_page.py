import streamlit as st
import pickle
import numpy as np
import pandas as pd
from Connection import establish_connection
from Connection import insert_data
from Connection import execute_sql_file

# Define las opciones para los selectboxes
Gender_Box = ["Male", "Female"]
Customer_Type_Box = ["Loyal Customer", "Disloyal Customer"]
Type_of_Travel_Box = ["Business travel", "Personal Travel"]
Class_Box = ["Eco", "Eco Plus", "Business"]

# Crea un diccionario para almacenar los datos capturados
data = {
    'Gender': [],
    'Customer Type': [],
    'Age': [],
    'Type of Travel': [],
    'Class': [],
    'Flight Distance': [],
    'Inflight wifi service': [],
    'Departure/Arrival time convenient': [],
    'Ease of Online booking': [],
    'Gate location': [],
    'Food and drink': [],
    'Online boarding': [],
    'Seat comfort': [],
    'Inflight entertainment': [],
    'On-board service': [],
    'Leg room service': [],
    'Baggage handling': [],
    'Checkin service': [],
    'Inflight service': [],
    'Cleanliness': [],
    'Departure Delay in Minutes': [],
    'Arrival Delay in Minutes': [],
}

# Define la función que se ejecutará al presionar el botón
def save_data(data, Gender, Customer_Type, Age, Type_of_Travel, Class,
            Flight_distance, Inflight_wifi_service, Departure_Arrival_time_convenient,
            Ease_of_Online_booking, Gate_location, Food_and_drink, Online_boarding,
            Seat_comfort, Inflight_entertainment, Onboard_service, Leg_room_service,
            Baggage_handling, Checkin_service, Inflight_service, Cleanliness,
            Departure_delay_minutes, Arrival_delay_minutes):
    data['Gender'].append(Gender)
    data['Customer Type'].append(Customer_Type)
    data['Age'].append(Age)
    data['Type of Travel'].append(Type_of_Travel)
    data['Class'].append(Class)
    data['Flight Distance'].append(Flight_distance)
    data['Inflight wifi service'].append(Inflight_wifi_service)
    data['Departure/Arrival time convenient'].append(Departure_Arrival_time_convenient)
    data['Ease of Online booking'].append(Ease_of_Online_booking)
    data['Gate location'].append(Gate_location)
    data['Food and drink'].append(Food_and_drink)
    data['Online boarding'].append(Online_boarding)
    data['Seat comfort'].append(Seat_comfort)
    data['Inflight entertainment'].append(Inflight_entertainment)
    data['On-board service'].append(Onboard_service)
    data['Leg room service'].append(Leg_room_service)
    data['Baggage handling'].append(Baggage_handling)
    data['Checkin service'].append(Checkin_service)
    data['Inflight service'].append(Inflight_service)
    data['Cleanliness'].append(Cleanliness)
    data['Departure Delay in Minutes'].append(Departure_delay_minutes)
    data['Arrival Delay in Minutes'].append(Arrival_delay_minutes)
    
    return data

def show_predict_page():
    st.title("Encuesta de satisfacción de clientes")

    # Crea los elementos del formulario
    Gender = st.selectbox("Género", Gender_Box)
    Customer_Type = st.selectbox("Tipo de cliente", Customer_Type_Box)
    Age = st.slider("Edad", 0, 100, 1)
    Type_of_Travel = st.selectbox("Tipo de Viaje", Type_of_Travel_Box)
    Class = st.selectbox("Clase", Class_Box)
    Flight_distance = st.slider("Distancia de vuelo", 0, 5000, 10)
    Inflight_wifi_service = st.slider("Servicio wifi a bordo", 0, 5, 1)
    Departure_Arrival_time_convenient = st.slider("Hora de salida/llegada conveniente", 0, 5, 1)
    Ease_of_Online_booking = st.slider("Facilidad de reserva en línea", 0, 5, 1)
    Gate_location = st.slider("Ubicación de la puerta", 0, 5, 1)
    Food_and_drink = st.slider("Comida y bebida", 0, 5, 1)
    Online_boarding = st.slider("Embarque online", 0, 5, 1)
    Seat_comfort = st.slider("Confort del asiento", 0, 5, 1)
    Inflight_entertainment = st.slider("Entretenimiento a bordo:", 0, 5, 1)
    Onboard_service = st.slider("Servicio a bordo", 0, 5, 1)
    Leg_room_service = st.slider("Servicio de habitaciones para piernas", 0, 5, 1)
    Baggage_handling = st.slider("Manejo de equipaje", 0, 5, 1)
    Checkin_service = st.slider("Servicio de Check-in", 0, 5, 1)
    Inflight_service = st.slider("Servicio a bordo", 0, 5, 1, key="inflight_service_slider")
    Cleanliness = st.slider("Limpieza", 0, 5, 1, key="Cleanliness_slider")
    Departure_delay_minutes = st.slider("Retraso de salida en minutos", 0, 1600, 1)
    Arrival_delay_minutes = st.slider("Retraso de llegada en minutos", 0, 1600, 1)

    # Crea el botón para guardar los datos
    if st.button("Nivel de satisfacción"):
        new_data = save_data(
            data,
            Gender,
            Customer_Type,
            Age,
            Type_of_Travel,
            Class,
            Flight_distance,
            Inflight_wifi_service,
            Departure_Arrival_time_convenient,
            Ease_of_Online_booking,
            Gate_location,
            Food_and_drink,
            Online_boarding,
            Seat_comfort,
            Inflight_entertainment,
            Onboard_service,
            Leg_room_service,
            Baggage_handling,
            Checkin_service,
            Inflight_service,
            Cleanliness,
            Departure_delay_minutes,
            Arrival_delay_minutes,
        )
        
        
        # Load model
        with open('../ML/model_gbc.pkl', 'rb') as file:
            model = pickle.load(file)

        # Realiza la predicción
        predict = model.predict(pd.DataFrame(new_data))
        
        # Guarda el ultimo dato ingresado
        result = predict[-1]
        
        data_form = {
            "id_passenger": 1,
            "Gender": Gender,
            "Customer_Type": Customer_Type,
            "Age": Age,
            "Type_of_Travel": Type_of_Travel,
            "Class": Class,
            "Flight_distance": Flight_distance,
            "Inflight_wifi_service": Inflight_wifi_service,
            "datc": Departure_Arrival_time_convenient,
            "Ease_of_Online_booking": Ease_of_Online_booking,
            "Gate_location": Gate_location, 
            "Food_and_drink": Food_and_drink,
            "Online_boarding": Online_boarding,
            "Departure_delay_minutes": Departure_delay_minutes,
            "Seat_comfort": Seat_comfort,
            "Inflight_entertainment": Inflight_entertainment,
            "Onboard_service": Onboard_service,
            "Leg_room_service": Leg_room_service,
            "Baggage_handling": Baggage_handling,
            "Checkin_service": Checkin_service,
            "Inflight_service": Inflight_service,
            "Cleanliness": Cleanliness,
            "Arrival_delay_minutes": Arrival_delay_minutes,
            "predict": result,
        }
        
        # limpia y vacia predict
        connection = establish_connection()
        execute_sql_file(connection, "./Credentials/airline.sql")
        insert_data(connection, data_form)
        
        predict = []
        new_data = []
        data_form = {}
        
        # Muestra el resultado
        st.success(f"El cliente está {'satisfecho 😍' if result == 1 else 'insatisfecho 🥺'}")
