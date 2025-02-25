from flask import Flask, render_template
import os
import database as db

app = Flask(__name__)

# Obtén la ubicación del directorio actual
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Construye la ruta completa al directorio de las plantillas
template_dir = os.path.join(template_dir, 'src', 'templates')

# Configura la ubicación del directorio de las plantillas en la aplicación Flask
app = Flask(__name__, template_folder=template_dir)

# Ruta de la página principal
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM students")
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)
