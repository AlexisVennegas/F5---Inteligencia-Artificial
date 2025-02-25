import streamlit as st
from Components.CardComplement import CardComplement
from Scrapper.Predict_comments import *
import streamlit as st
import pandas as pd
import pymysql
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from Components.Information import title_markdown

def predict_page(value_contents):
    '''
    Función que se encarga de mostrar el resultado de la predicción
    atravez de un componente CardComplement que se encuentra en Components/CardComplement.py
    primero se muestra un spinner mientras se realiza la predicción, luego se muestra el resultado
    '''
    result = None
    if value_contents:
        # Muestra un spinner mientras se realiza la predicción
        with st.spinner("Prediciendo..."):
            # st.success('Done!')
            result_english = translate_to_english(value_contents)
            result = predict_comments(value_contents)
            #result = make_mood_prediction(result_english)
            # result = predict_comments_v2(value_contents)
            if result:
                CardComplement(result_english, result[0]["score"], result[0]["label"])
            else:
                st.write("Inserta un comentario...")
    else:
        st.write("Inserta un comentario...")

def get_data_by_video_id(conn, youtube_id):
    try:
        cursor = conn.cursor()
        query = """
        SELECT Texto, IsToxic
        FROM bawhvsumyg8pry69xiue
        WHERE youtube_id = %s
        """
        cursor.execute(query, (youtube_id,))
        data = cursor.fetchall()
        return data
    except pymysql.Error as e:
        st.error(f"Error al obtener los datos: {e}")
    finally:
        cursor.close()

def process_to_pd(comments_df):
    text = comments_df['Texto'].values 
    # title_markdown("Relevant Columns")
    wordcloud = WordCloud(background_color="white").generate(str(text))
    plt.figure(figsize=(20,20))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    # 
    st.sidebar.pyplot()

def grafic_circle(total_negative, total_positive):
   
    # Crear un DataFrame para la gráfica de pastel
    pie_data = pd.DataFrame({'Positive': [total_positive, total_negative]}, index=['Positivos', 'Negativos'])

    # Crear la gráfica de pastel
    fig, ax = plt.subplots()
    pie_data.plot.pie(y='Positive', autopct='%1.1f%%', startangle=90, legend=False, ax=ax)
    ax.axis('equal')  # Para que la gráfica sea un círculo

    # Mostrar la gráfica en Streamlit
    st.sidebar.pyplot(fig)


def testing_words(item, df):
    st.sidebar.write(df.duplicated().sum(), "duplicados")
    st.sidebar.write(df.shape, "filas y columnas")
    st.sidebar.write(df.head(), "primeros 5 comentarios")
    st.sidebar.write(df.tail(), "ultimos 5 comentarios")
    st.sidebar.write(df.info(), "información del dataframe")
    st.sidebar.write(df.describe(), "descripción del dataframe")
    st.sidebar.write(df.isnull().sum(), "valores nulos")
    st.sidebar.write(df['IsToxic'].value_counts(), "valores nulos")
    st.sidebar.write(df['Texto'].value_counts(), "valores nulos")
    st.sidebar.write(df['Texto'].nunique(), "valores nulos")

def display_data_by_video_id(conn, youtube_id, total_positive, total_negative, item):
    data = None
    data = get_data_by_video_id(conn, youtube_id)

    if data:
        data_df = pd.DataFrame(data, columns=['Texto', 'IsToxic'])
        process_to_pd(data_df)
        grafic_circle(total_negative, total_positive)
        testing_words(item, data_df)
    else:
        st.warning(f"No hay datos disponibles para el video con ID {youtube_id}.")


