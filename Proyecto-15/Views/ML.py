import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import json
import streamlit as st
import time

df = pd.read_csv("../Data/airline_passenger_satisfaction.csv")


st.write("""
    <div class="scale-in-center" style="margin: 20px 0px;display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;">
        <p style="font-size: 45px; text-align: center; margin:5px; padding:0px;">Modelo de Manching Learning</p>
    </div>""", unsafe_allow_html=True)


st.text("Dividamos este proceso en varias partes")
st.write("""
    <div style="margin: 10px 0px; display: flex;  flex-direction: column;  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
        <p style="font-size: 16px;">Limpieza de datos (Data cleansing):</p>
        <ul>
        <li>Verificamos la cantidad de valores nulos en el DataFrame Esto permite asegurar de que no haya mas valores nulos en el conjunto de datos</li>
        <li style="font-size: 16px;">Nos damos cuenta que solo tenemos datos nulos en la columna de 'Arrival Delay in Minutes' con 310 datos nulos</li>
        <li style="font-size: 16px;">Veamos si existe relacion entre esta columa y alguna otra directamente atravez de un mapa de calor</li>
          </ul>
    </div>""", unsafe_allow_html=True)

code = ''' 
    # cargamos el dataset
    df = pd.read_csv("../Data/airline_passenger_satisfaction.csv"
    # Verificamos la cantidad de valores nulos en el DataFrames
    df.isnull().sum()'''
st.code(code, language='python')


plt.figure(figsize=(12, 6))
num = ['Age', 'Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']
sns.heatmap(df[num].corr(),
            cmap = 'crest',
            fmt = '.2f',
            linewidths = 2,
            annot = True)
st.pyplot()
st.write("""
    <div style="margin: 10px 0px; display: flex;  flex-direction: column;  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
        <ul>
            <li style="font-size: 16px;">Tenemos una relacion directa entre esta columna y la columna Departure Delay in Minutes y Flight Distance </li>
            <li>con esta informacion vamos a rellenar la columna con los datos faltantes esto atravez de la columna Departure Delay in Minutes que contiene la hora de salida </li>
            <li>usamos el metodo fullna para rellenar los datos faltantes apartir de la columna Departure Delay in Minutes</li>
        </ul>
    </div>""", unsafe_allow_html=True)

code = ''' 
    # rellenamos los datos faltantes con la columna Departure Delay in Minutes
    df['Arrival Delay in Minutes'].fillna(df['Departure Delay in Minutes'], inplace=True)
    # Verificamos la cantidad de valores nulos en el DataFrames
    df.isnull().sum()'''
st.code(code, language='python')

st.write("""
    <div style="margin: 10px 0px; display: flex;  flex-direction: column;  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
        <ul>
            <li style="font-size: 16px;">Teniendo los datos completos, pasamos a eliminar las columnas innecesarias ya sea porque no tienen relevancia o relacion</li>
            <li>En este caso eliminar las columnas "Unnamed: 0" e "id", por no aportan nada al modelo</li>
            <li>Asi tenemos los datos limpios correctamente </li>
        </ul>
    </div>""", unsafe_allow_html=True)
    
code = ''' 
    # Eliminamos las columnas innecesarias
    df.drop(['Unnamed: 0','id'],axis=1,inplace=True)
    '''
st.code(code, language='python')



st.write("""
    <div style="margin: 10px 0px; display: flex;  flex-direction: column;  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
        <p style="font-size: 16px;">Mapeo de categorías a valores numéricos/p>
        <ul>
            <li>Este proceso implica asignar valores numéricos a las categorías en una columna categórica. En este caso específico, mapeamos las categorías de satisfacción ('neutral or dissatisfied' y 'satisfied') a valores numéricos (0 y 1) en la columna 'satisfaction '.</li>
            <li>Este paso es común en la preparación de datos para el análisis y modelado de machine learning, ya que muchos algoritmos requieren que todas las entradas sean numéricas. Al convertir las categorías en valores numéricos, permites que los algoritmos utilicen esa información para hacer predicciones o análisis cuantitativos.</li>
        </ul>
    </div>""", unsafe_allow_html=True)



code = ''' 
def split_data(features, target, test_size=0.4, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=test_size, random_state=random_state
    )

    X_test, X_val, y_test, y_val = train_test_split(
        X_test, y_test, test_size=0.5, random_state=random_state
    )

    return X_train, X_test, y_train, y_test, X_val, y_val

def clean_name_model(model):
    pattern = r'(?<=[a-z])(?=[A-Z])'
    return re.sub(pattern, ' ', model)

def evaluate_model(model, X_train, y_train, X_test, y_test, X_val, y_val):
    time_start = time.time()
    model.fit(X_train, y_train)
    time_end = time.time()
    model_scores = cross_val_score(model, X_train, y_train.values.ravel(), cv=5)
    
    y_pred_test = model.predict(X_test)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    precision_test = precision_score(y_test, y_pred_test)
    recall_test = recall_score(y_test, y_pred_test)

    y_pred_val = model.predict(X_val)
    accuracy_val = accuracy_score(y_val, y_pred_val)
    precision_val = precision_score(y_val, y_pred_val)
    recall_val = recall_score(y_val, y_pred_val)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_mae_train = mae(y_train, train_predictions)
    test_mae_test = mae(y_test, test_predictions)
    overfitting_percentage = (test_mae_test - train_mae_train) / train_mae_train * 100
    
    # Calcular la curva ROC y el AUC
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    auc = roc_auc_score(y_test, y_pred_proba)

    # Calcular las matrices de confusión y limpia el nombre del modelo
    conf_mx = confusion_matrix(y_test, y_pred_test)
    name_model = clean_name_model(model.__class__.__name__)

    return {
        'Model': name_model,
        'Model Scores': model_scores,
        'Accuracy (test)': accuracy_test,
        'Accuracy (validate)': accuracy_val,
        'Precision (test)': precision_test,
        'Precision (validate)': precision_val,
        'Recall (test)': recall_test,
        'Recall (validate)': recall_val,
        'Train MAE': train_mae_train,
        'Test MAE': test_mae_test,
        'Training Time': time_end - time_start,
        'Overfitting %': overfitting_percentage,
        'Confusion Matrix': conf_mx,
        'ROC Curve': (fpr, tpr, auc),
    }

def train_and_evaluate_models(df, features, target, models):
    X_train, X_test, y_train, y_test, X_val, y_val = split_data(features, target)

    # Evaluate the models
    metrics = []
    for model in models:
        model_metrics = evaluate_model(model, X_train, y_train, X_test, y_test, X_val, y_val)
        metrics.append(model_metrics)

    return pd.DataFrame(metrics)
    '''
st.code(code, language='python')




#    <li>Eliminar valores duplicados</li>
#             <li>Eliminar columnas innecesarias</li>
#             <li>Eliminar filas innecesarias</li>
#             <li>Corregir errores de ortografía</li>
#         </ul>