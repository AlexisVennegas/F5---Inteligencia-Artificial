import streamlit as st
import time


def convert_time(time):
    # funcion que trata el time
    time = time.split("T")
    time = time[0].split("-")
    time = time[2] + "-" + time[1] + "-" + time[0]
    return time

def Card_New(item_json, result, text_english):
    

    name = item_json['snippet']['topLevelComment']['snippet']['authorDisplayName']
    text = item_json['snippet']['topLevelComment']['snippet']['textDisplay']
    image = item_json['snippet']['topLevelComment']['snippet']['authorProfileImageUrl']
    accuracy = result[0]['score']
    accuracy = round(accuracy, 2) * 100
    time = item_json['snippet']['topLevelComment']['snippet']['publishedAt']
    time = convert_time(time)
    link_video = item_json['snippet']['topLevelComment']['snippet']['videoId']
    link_canal_persona = item_json['snippet']['topLevelComment']['snippet']['authorChannelUrl']
    result_value = result[0]['label']
    if result_value == "1 star" or result_value == "2 stars" or result_value == "3 stars":
        result_value = "NEGATIVE"
    elif result_value == "4 stars" or result_value == "5 stars":
        result_value = "POSITIVE"
    else:
        result_value = "NEUTRAL"

    st.markdown(
        """
        <style>  
        .section_name {
            width: 100%;
            height: 100%;
            padding: 11px;
            border-radius: 5px;
            background: #ffffffcf !important;
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
            border-radius: 13px !important;
            padding: 0px 10px !important;
            margin: 0px !important;
            font-size: 10px;   
            color: #9fa4aa; 
        }
        .prediction_positive {
            width: 150px;
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
            width: 150px;
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

    st.write(
    f"""
        <section class="section_name">
            <div class="prediction">
                <span class="{"prediction_positive" if result_value == "POSITIVE" else "prediction_negative"}">{result_value} : {accuracy} %</span>
            </div>
            <div class="Card-comment">
                <div class="img-content">
                    <a href="{link_canal_persona}" target="_blank" style="cursor: pointer; border: none; ">
                        <img src="{image}" alt="imagen" class="image_person">
                    </a>
                </div>
                <div class="content_text">
                    <div class="name_username">
                        <a href="https://www.youtube.com/watch?v={link_video}" target="_blank" style="cursor: pointer; border: none; ">
                        <p class="text_name_value" >  {name}</p>
                        </a>
                        <p class="from_text">{time}</p>
                    </div>
                    <div class="text">
                        <p>{text_english}</p>
                    </div>
                </div>
            </div>
        </section>

    """, unsafe_allow_html=True
)
