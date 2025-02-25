import streamlit as st
from transformers import pipeline
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.nn import Softmax
import torch
from googletrans import Translator
# from Scrapper.change_model import load_model, predict_toxicity

def translate_to_english(text: str):
    try:
        translator = Translator()
        translation = translator.translate(text, dest='en')
        return translation.text
    except Exception as e:
        return text

def predict_comments(value_contents):
    if value_contents:
            classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
            # classifier = pipeline("text-classification")
            # result = classifier(value_contents)
            result = classifier(value_contents)
    return result 

def predict_comments_v2(value_contents):

        # Cargar el modelo preentrenado y el tokenizador
        model_name = "distilbert-base-multilingual-cased"
        model = DistilBertForSequenceClassification.from_pretrained(model_name)
        tokenizer = DistilBertTokenizer.from_pretrained(model_name)

        # Agregar una capa de clasificación
        model.classifier = torch.nn.Linear(in_features=768, out_features=2)

        # Definir la función de softmax
        softmax = Softmax(dim=1)

        inputs = tokenizer(value_contents, return_tensors="pt")

        # Realizar la predicción
        with torch.no_grad():
                outputs = model(**inputs)

        # Aplicar la función de softmax a las predicciones
        probs = softmax(outputs.logits)

            # Obtener la probabilidad de la clase "toxic" (clase 1)
        toxicity_probability = probs[:, 1].item()
        st.write(toxicity_probability)
        return toxicity_probability



# def make_mood_prediction(text):
#     """
#     Realizamos la predicción
#     """
#     model = load_model()
#     try:
#         #text = text.get("mood")
#         prediction = predict_toxicity(model, text)
#         st.write(prediction)
#         predict_message = "👹 Es Tóxico" if prediction == 1 else "😇 No es tóxico"
#         return {"message": f"El mensaje 👉 {text}, {predict_message}"}
#         response.status_code = status.HTTP_200_OK

#     except Exception as error:
#         return {"message": f"Hubo un problema, {error}"}
