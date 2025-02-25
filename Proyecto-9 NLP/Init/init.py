import streamlit as st


def init() -> None:
    st.set_page_config(
    page_title="Youtube Predict",
    page_icon=":smiley:",
    layout="centered",  # Puedes ajustar esto según tus necesidades
    initial_sidebar_state="collapsed"  # Puedes ajustar esto según tus necesidades
    )


    background_image_url = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ5_WpATCBkLRcevy1ul160mBp9382fk3OwrCYwb3YUmytwc7B8"

    # Establecer el degradado de fondo
    background_gradient = "linear-gradient(to bottom, #ff00003b, #abcdefb3)"  # Cambia los colores según tus preferencias

    # Aplicar el estilo usando st.markdown
    st.markdown(
    f"""
    
    <style>
        .st-emotion-cache-fg4pbf {{
            background-image: url('{background_image_url}') !important;
            background-size: cover !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
            background: {background_gradient} !important;
        }}
        .st-emotion-cache-1v0mbdj > img {{
            margin-top: 60px !important;
            box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
            border-radius: 15px;
        }}
        .st-emotion-cache-16txtl3 {{
            text-align: center !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
    )

def init_predict_comments(link_video: str) -> None:

    if link_video is None:
        # Título de la app
        first_model = st.write("""
        <section style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
            <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid red;"> Youtube Predict Comments</h1>
        </section>""", unsafe_allow_html=True)

        # IMAGE
        st.write("""
            <div class="div_container_img" style="display: flex; justify-content: center; align-items: center; padding: 10px; border-radius: 15px">
                <img src="https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_download_software_1/H2x1_NSwitchDS_YouTube_image1280w.jpg" alt="aereolina" width="700" style="box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; margin: 10px 0px; border-radius: 6px;">
            </div>""", unsafe_allow_html=True)
    else:
         # Título de la app                               
        st.markdown("""
            <style>
            .st-emotion-cache-5rimss > div {
                display: none !important;
            }
            </style>
            """, unsafe_allow_html=True)

         # IMAGE
        st.write(f"""
            <section style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px; border-radius: 15px">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/{link_video}" frameborder="0" allowfullscreen></iframe>'
            </section>""", unsafe_allow_html=True)


def init_scrapping_css():
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

        # TITULO
    st.write("""
            <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
                <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Youtube</h1>
            </div>""", unsafe_allow_html=True)
    # IMAGE
    st.write("""
            <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
                <img src="https://media2.giphy.com/media/LP62GF82YvcuOuFJRD/giphy.gif?cid=ecf05e47hsutrc15t05in0wrr7a9veckswprb9xikrzm8a6f&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="aereolina" width="300" style="margin: 10px 0px; border-radius: 6px;">
            </div>""", unsafe_allow_html=True)


def change_video(link_video: str) -> None:
    init_predict_comments(link_video)
    # st.write(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{link_video}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)  


SIDE_INFO = "Puedes usar nuestro modelo de inteligencia artificial para detectar y combatir el discurso de odio en línea."
