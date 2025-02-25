from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.core.paginator import Paginator
from django.shortcuts import render
from facebook_scraper import get_posts
import json
import os 

# VISTA QUE DEVUELVE UN JSON CON TODAS LAS NOTICIAS
def notice():
    # ABRO EL ARCHIVO JSON
    try:
        with open("{% static 'data.json' %}", "r") as file:
            data = json.load(file)
            file.close()
        # DEVUELVO EL JSON
    except Exception as e:
        # SI HAY UN ERROR DEVUELVO -1
        return -1
    return data

# VISTA QUE DEVUELVE UN JSON CON TODAS LAS NOTICIAS DE FACEBOOK
def data_facebook():
    posts_list = []
    for post in get_posts('groups/159206940894760', page=9):
        posts_list.append(post)
    return posts_list

# VISTA RAIZ DE LA APLICACION WEB
def home(request):
    # CARGO LOS TEMPLATES
    page_404 = loader.get_template('404.html')
    page = loader.get_template('index.html')

    # EN LA VARIABLE DATA ALMACENO TODAS LAS NOTICAS EN UN JSON QUE DEVUELVE NOTICE()
    data_json_path = "{% static 'data.json'  %}"

    # Verificar si el archivo data.json está vacío o no existe
    if not os.path.exists(data_json_path) or os.stat(data_json_path).st_size == 0:
        # Obtener datos de Facebook
        data = data_facebook()
        if data != -1:
            # Convertir objetos datetime a cadenas antes de guardarlos en el archivo
            for post in data:
                if 'time' in post and isinstance(post['time'], datetime):
                    post['time'] = post['time'].isoformat()
                    # eliminamos los 30 primeros caracteres de links
                    post['links'] = post['links'][30:]

            # Escribir los datos en el archivo data.json
            with open(data_json_path, "w") as file:
                json.dump(data, file)
    else:
        # Abrir el archivo data.json y cargar los datos
        with open(data_json_path, "r") as file:
            data = json.load(file)
    # Configura el número de noticias que deseas mostrar por página
    noticias_por_pagina = 5

    # Obtén el número de página de la solicitud GET
    pagina = request.GET.get('page', 1)

    # Crea un objeto Paginator
    paginator = Paginator(data, noticias_por_pagina)


    # SI DATA ES IGUAL A -1 ES PORQUE HUBO UN ERROR AL ABRIR EL ARCHIVO JSON
    if data == -1:
        doc_404 = page_404.render()
        return HttpResponse(doc_404)
   
    # RENDERIZO EL TEMPLATE CON LOS DATOS DE DATA
    try:
        # Obtiene las noticias para la página actual
        noticias_pagina = paginator.page(pagina)
    except Exception as e:
        # Si la página está fuera del rango, muestra la última página
        noticias_pagina = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'noticias_pagina': noticias_pagina})