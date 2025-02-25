import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import json
import streamlit as st
import time

st.write("""
    <div class="scale-in-center" style="margin: 20px 0px;display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;">
        <p style="font-size: 45px; text-align: center; margin:5px; padding:0px;">Graficacion de los datos </p>
    </div>""", unsafe_allow_html=True)
    
# cargamos el dataset
df = pd.read_csv("../Data/airline_passenger_satisfaction.csv")


# Calcular el porcentaje de cada categoría en la columna 'satisfaction'
st.write('<span style="color: red;">Porcentaje de la columna satisfaccion</span>', unsafe_allow_html=True)  
percentage_counts = df['satisfaction'].value_counts(normalize=True) * 100
# Mostrar los porcentajes en Streamlit
st.write(percentage_counts)
# Crear un gráfico de barras
st.bar_chart(percentage_counts)
# Opcional: Personalizar el gráfico de barras
st.set_option('deprecation.showPyplotGlobalUse', False)  # Para evitar advertencias
fig, ax = plt.subplots()
with st.expander("Grafica Satisfaccion"):
    st.write("""
    El 43,33% de los pasajeros estan satisfechos con los servicios de la aerolinea.   
    El 56,67% de los pasajeros se muestran neutrales o insatisfechos con los servicios de las aerolíneas
    """)




# calculamos la edad media de los pasajeros
st.write('<span style="color: red;">Edad media de los pasajeros</span>', unsafe_allow_html=True)
porcentage_age = df['Age'].value_counts(normalize=True) * 100
# Mostrar los porcentajes en Streamlit
st.write(porcentage_age)
# Crear un gráfico de barras
st.bar_chart(porcentage_age)
# Opcional: Personalizar el gráfico de barras
st.set_option('deprecation.showPyplotGlobalUse', False)  # Para evitar advertencias
fig, ax = plt.subplots()
with st.expander("Grafica Edad"):
    st.write("""
    Mas de 2.000 pasajeros tienen edades comprendidas entre 23 y 27 anos y entre 35 y 45 anos
    """)



# graficamos el genero, tipo de cliente y tipo de viaje, y clase
st.write('<span style="color: red;">Grafica de genero, tipo de cliente y clase</span>', unsafe_allow_html=True)
fig, ax = plt.subplots()
# GRAFICA DE GENERO, TIPO DE CLIENTE, TIPO DE VIAJE Y CLASE
fig, axes = plt.subplots(2, 2, figsize=(10, 8))


# Grafico 0 de genero
df['Gender'].value_counts(normalize=True, dropna=True).plot.bar(ax=axes[0, 0], color=['slategray', 'teal'])
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=360)
axes[0, 0].set_xlabel('Genero')
axes[0, 0].set_ylabel('Ratio')


# Gráfico 1
df['Customer Type'].value_counts(normalize=True, dropna=True).plot.bar(ax=axes[0, 0], color=['slategray', 'teal'])
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=360)
axes[0, 0].set_xlabel('Customer Type')
axes[0, 0].set_ylabel('Ratio')

# Gráfico 2
df['Type of Travel'].value_counts(normalize=True, dropna=True).plot.bar(ax=axes[0, 1], color=['slategray', 'teal'])
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=360)
axes[0, 1].set_xlabel('Type of Travel')
axes[0, 1].set_ylabel('Ratio')

# Gráfico 3
df['Class'].value_counts(normalize=True, dropna=True).plot.bar(ax=axes[1, 0], color=['slategray', 'teal'])
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=360)
axes[1, 0].set_xlabel('Class')
axes[1, 0].set_ylabel('Ratio')
# Elimina el cuarto subplot
fig.delaxes(axes[1, 1])
# Mostrar el gráfico en Streamlit
st.pyplot(fig)
with st.expander("Grafica Edad"):
    st.write("""
    Hay un 51% de pasajeras femeninas.   
    El 82% de los pasajeros son clientes fieles.  
    El 69% de los pasajeros viajan por motivos de negocios.   
    El 48% de los pasajeros viaja en clase business y el 45% en clase Eco.
    """)


# distintas satisfacciones
st.write('<span style="color: red;">Grafica de distintas satisfacciones</span>', unsafe_allow_html=True)

# def plot_satisfaction_bar_chart(data, column_name, color_list):
#     st.subheader(column_name)
#     value_counts = data[column_name].value_counts(normalize=True, dropna=True)
#     fig, ax = plt.subplots(figsize=(10, 5))
#     value_counts.plot.bar(color=color_list)
#     plt.xticks(rotation=90)
#     plt.xlabel(column_name)
#     st.pyplot(fig)

# color_list = ['slategray', 'darkslategray', 'steelblue', 'teal', 'cadetblue', 'powderblue']

# plot_satisfaction_bar_chart(df, 'Inflight wifi service', color_list)
# plot_satisfaction_bar_chart(df, 'Departure/Arrival time convenient', color_list)
# plot_satisfaction_bar_chart(df, 'Ease of Online booking', color_list)
# plot_satisfaction_bar_chart(df, 'Gate location', color_list)
# plot_satisfaction_bar_chart(df, 'Food and drink', color_list)
# plot_satisfaction_bar_chart(df, 'Online boarding', color_list)
# plot_satisfaction_bar_chart(df, 'Seat comfort', color_list)
# plot_satisfaction_bar_chart(df, 'Inflight entertainment', color_list)

with st.expander("distintas satisfacciones"):
    st.write("""
Variable independiente (categorica: ordinal)  
            
Aproximadamente el 25 % de los pasajeros obtuvieron una calificacion de 3 y el 25 % de ellos obtuvieron una calificacion de 2 para el servicio wifi a bordo  
El 24% de los pasajeros calificaron con 4 la hora de salida/llegada conveniente y el 21% de los pasajeros calificaron con 5 la misma calificación.  
Aproximadamente el 23% de los pasajeros califica 3 por la facilidad de reserva en línea y el 23% de ellos califica 2  
El 27,5% de los pasajeros califica con 3 la ubicación de la puerta de embarque.  
Para servicio de alimentos y bebidas 23% de calificaciones = 4  
Para el embarque en línea aproximadamente el 30% de los pasajeros dieron 4 calificaciones  
Para la comodidad del asiento, la mayoría de los pasajeros tienen un nivel satisfactorio de 4.  
Aproximadamente el 28 % de los pasajeros otorgó 4 calificaciones al entretenimiento a bordo
    """)
