import time
import json
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from predict_page import show_predict_page

# secciones
page = st.sidebar.selectbox("Selecciona una página", ["Visualización de Datos", "Ingresar Datos"])

# si la sección es "Visualización de Datos"
if page == "Visualización de Datos":
    # CSS
    st.markdown(
    """
    <style>
    .st-bo {
        overflow-y: hidden;
        display: flex !important;
        justify-content: space-around !important;
        margin-top: 20px !important;
    }
    .scale-in-center{-webkit-animation:scale-in-center .5s cubic-bezier(.25,.46,.45,.94) both;animation:scale-in-center .5s cubic-bezier(.25,.46,.45,.94) both}
    @-webkit-keyframes scale-in-center{0%{-webkit-transform:scale(0);transform:scale(0);opacity:1}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}@keyframes scale-in-center{0%{-webkit-transform:scale(0);transform:scale(0);opacity:1}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}

    </style>
    """,
        unsafe_allow_html=True
    )

    # Título de la app
    st.write("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
        <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Aerolínea - Satisfacción de Clientes</h1>
    </div>""", unsafe_allow_html=True)

    # IMAGE
    st.write("""
    <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
        <img src="https://i.pinimg.com/originals/b9/b8/1a/b9b81ab0e549a0ef6bbd9616e32031d5.gif" alt="aereolina" width="700" style="margin: 10px 0px; border-radius: 6px;">
    </div>""", unsafe_allow_html=True)

    # FIRST TEXT
    st.write("""
    <div style="margin: 10px 0px; display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
        <p style="font-size: 16px;">F5 Airlines lleva un tiempo recogiendo datos relativos a la satisfacción de los clientes. Esos datos han sido utilizados en general, pero con poco éxito, para ser analizados a mano en busca de los motivos y de un plan de actuación futuro para evitar este tipo de casos.</p>
    </div>""", unsafe_allow_html=True)

    # FIRST TEXT
    st.write("""
    <div style="margin: 10px 0px; display: flex; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px; flex-direction: column;">
        <p style="font-size: 16px;">Es posible resolver este problema con inteligencia artificial, el plan tiene dos fases: </p>
            <ul>
                <li>Entrenar un modelo que prediga de manera satisfactoria si un cliente dado estará satisfecho o no.</li>
                <li>Desarrollar una pequeña aplicación que recoja los datos de un cliente nuevo y realice una predicción sobre su grado de satisfacción.</li>
            </ul>
    </div>""", unsafe_allow_html=True)


    # button created
    tab1, tab2, tab3 = st.tabs(["Datos", "Graficos", "Modelo IA"])

    with tab1:
        try:
            exec(open("./EDA.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")
    with tab2:
        try:
            exec(open("./Graphics.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")
    with tab3:
        try:
            exec(open("./ML.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")


else:  
    show_predict_page()
