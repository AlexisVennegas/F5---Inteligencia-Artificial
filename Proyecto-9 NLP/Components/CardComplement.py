import streamlit as st

# Componente CardComplement
def CardComplement(text: str, accuracy: str, label: str):
    
    '''
    Componente CardComplement que se encarga de mostrar el resultado de la predicción
    primero carga los estilos y luego muestra el resultado, el resultado se muestra
    en un componente html que se encuentra en la variable html
    '''
    # redondeamos el valor de la predicción
    accuracy = round(accuracy, 2) * 100
    
    result_value = label
    if result_value == "1 star" or result_value == "2 stars" or result_value == "3 stars":
        result_value = "NEGATIVE"
    elif result_value == "4 stars" or result_value == "5 stars":
        result_value = "POSITIVE"
    else:
        result_value = "NEUTRAL"
    # Cargamos los estilos
    st.markdown(
        """
        <style>  
        .section_name {
            width: 100%;
            height: 100%;
            padding: 11px;
            border-radius: 4px;
            background: #ffffff1c;
            box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
            margin-top: 21px;
        }
        .Card-comment {
        width: 100%;
        height: 40%;
        display: flex;   
        }
        .img-content {
            width: 18%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .content_text {
            width: 82%;
        }
        .image_person {
            border-radius: 50%;
            width: 75px;
            height: 75px;
        }
        .name_username {
            flex-direction: row;
            height: auto !important;
            display: flex;
            align-items: flex-end;
        }
        .text_name_value {
            padding: 0px !important;
            margin: 0px !important;
            font-size: 20px;    
        }
        .from_text {
            background: #80808047;
            display: none;
            border-radius: 13px !important;
            padding: 0px 10px !important;
            margin: 0px !important;
            font-size: 20px;   
            color: #9fa4aa; 
        }
        .prediction_positive {
            width: 133px;
            height: 20px;
            position: absolute;
            right: 14px;
            top: 1px;
            background: #0000ff4d !important;
            border-radius: 10px 10px 0px 0px;
            display: flex;
            justify-content: center;
        }
        .prediction_negative {
            width: 133px;
            height: 20px;
            position: absolute;
            right: 14px;
            top: 1px;
            background: #ff000047 !important;
            border-radius: 10px 10px 0px 0px;
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Mostramos el resultado
    st.write(
    f"""
        <section class="section_name">
            <div class="prediction">
                <span class="{"prediction_positive" if result_value == "POSITIVE" else "prediction_negative"}">{result_value} : {accuracy} %</span>
            </div>
            <div class="Card-comment">
                <div class="img-content">
                    <img src={"https://cdn-icons-png.flaticon.com/128/303/303566.png" if result_value == "POSITIVE" else 'https://cdn-icons-png.flaticon.com/128/3670/3670220.png'} class="image_person">  
                </div>
                <div class="content_text">
                    <div class="name_username">
                        <p class="text_name_value" > @Username</p>
                        <p class="from_text">hace 2 dias</p>
                    </div>
                    <div class="text">
                        <p>{text}</p>
                    </div>
                </div>
            </div>
        </section>
    """, unsafe_allow_html=True
)

