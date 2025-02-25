import googleapiclient.discovery
import streamlit as st
import re
from Components.Coments import Card_New
from Components.Information import Information
from Scrapper.Predict_comments import predict_comments
from Scrapper.predict import display_data_by_video_id
from Init.init import change_video
from Scrapper.Predict_comments import translate_to_english
from SQL.Connection import *

# Clave de la API de YouTube
api_key = "AIzaSyC6QYqxFrp9v7_EbC8Bd04Cg1bOBfZvX0M"

def youtube_page(video_id: str):   
    # Lista de comentarios
    total_positive = 0
    total_negative = 0
    next_page_token = None
    
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    try:
        while True:
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                pageToken=next_page_token
            ).execute()

            link_video = results['items'][0]['snippet']['topLevelComment']['snippet']['videoId']
            # change_video(link_video)
            for item in results['items']:

                # extraemos el comentario
                comentario = item['snippet']['topLevelComment']['snippet']['textDisplay']

                # predict comments hacemos async y await
                text_english = translate_to_english(comentario)                
                result = predict_comments(text_english)
                # Card
                Card_New(item, result, text_english)

                # count positive and negative
                if result[0]['label'] == "POSITIVE":
                    total_positive += 1
                else:
                    total_negative += 1
                           
                # BBDD
                data_form = {
                    "Texto": comentario,
                    "IsToxic": result
                }
                is_toxic_label = data_form["IsToxic"][0]["label"]
                
            
                data_for_insert = {
                "Texto": data_form["Texto"],
                "IsToxic": is_toxic_label,
                "youtube_id": link_video
                }
                connection = establish_connection()
                try:
                    insert_data(connection, data_for_insert)
                except Exception as e:
                    st.write("Error al insertar los datos en la BBDD")
                    st.write("Error: ", e)
            # Comprueba si hay más páginas
            next_page_token = results.get('nextPageToken')
            # llamamos a information y lo acutalizamos con cada comentario nuevo
            if not next_page_token:
                Information(total_negative, total_positive, item, link_video)
                display_data_by_video_id(connection, link_video, total_positive, total_negative, item)
                break
    except Exception as e:
        st.write("error al cargar los comentarios")
        st.write("Error: ", e)
