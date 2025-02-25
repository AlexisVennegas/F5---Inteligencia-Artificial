# -*- coding: utf-8 -*-

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import json
import streamlit as st
import time

# CONTAINER Y TITULO
st = st.container()
st.write("""
    <div class="scale-in-center" style="margin: 20px 0px;display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;">
        <p style="font-size: 45px; text-align: center; margin:5px; padding:0px;">Proceso Exploratorio de Datos (EDA)</p>
    </div>""", unsafe_allow_html=True)


# cargamos el dataset
df = pd.read_csv("../Data/airline_passenger_satisfaction.csv")

# mostramos el dataset con head en streamlit
st.text("Primeros 5 datos del dataset")
st.write(df.head())

st.text("Columnas del dataset")
with st.expander("See explanation"):
    st.write("""
    <div style="box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px; margin:10px 0px;">
        <ul>
            <li>Genero: Genero de los pasajeros (Mujer, Hombre)</li>
            <li>Tipo de cliente: el tipo de cliente (cliente leal, cliente desleal)</li>
            <li>Edad: La edad real de los pasajeros.</li>
            <li>Tipo de Viaje: Proposito del vuelo de los pasajeros (Viaje Personal, Viaje de Negocios)</li>
            <li>Clase: Clase de viaje en el avion de los pasajeros (Business, Eco, Eco Plus)</li>
            <li>Distancia de vuelo: la distancia de vuelo de este viaje.</li>
            <li>Servicio wifi a bordo: Nivel de satisfaccion del servicio wifi a bordo (0:No aplicable;1-5)</li>
            <li>Hora de salida/llegada conveniente: Nivel de satisfaccion de la hora de salida/llegada conveniente</li>
            <li>Facilidad de reserva en línea: nivel de satisfaccion de la reserva en línea</li>
            <li>Ubicacion de la puerta: Nivel de satisfaccion de la ubicacion de la puerta</li>
            <li>Comida y bebida: Nivel de satisfaccion de Comida y bebida</li>
            <li>Embarque online: Nivel de satisfaccion del embarque online</li>
            <li>Confort del asiento: Nivel de satisfaccion del confort del asiento</li>
            <li>Entretenimiento a bordo: Nivel de satisfaccion del entretenimiento a bordo</li>
            <li>Servicio a bordo: Nivel de satisfaccion del servicio a bordo</li>
            <li>Servicio de habitaciones para piernas: Nivel de satisfaccion del servicio de habitaciones para piernas</li>
            <li>Manejo de equipaje: Nivel de satisfaccion en el manejo de equipaje</li>
            <li>Servicio de Check-in: Nivel de satisfaccion del servicio de Check-in</li>
            <li>Servicio a bordo: Nivel de satisfaccion del servicio a bordo</li>
            <li>Limpieza: Nivel de satisfaccion de la Limpieza</li>
            <li>Retraso de salida en minutos: Minutos de retraso a la salida</li>
            <li>Retraso de llegada en minutos: Minutos de retraso cuando llega</li>
            <li>Satisfaccion: Nivel de satisfaccion de la aerolinea (Satisfaccion, neutral o insatisfaccion)</li>
        </ul>
    </div>""", unsafe_allow_html=True)

# mostramos el dataset con describe en streamlit
st.text("Descripcion del dataset")
st.write(df.describe().style.background_gradient(cmap='Blues'))

# mostramos el dataset con info en streamlit
st.text("Cantidad de datos nulos en el dataset")
st.write(df.isna().sum())