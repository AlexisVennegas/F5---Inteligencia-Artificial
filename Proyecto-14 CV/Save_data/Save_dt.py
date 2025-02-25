import cv2
from PIL import Image, ImageTk
import os
import customtkinter as ctk
from Save_data.Save_json import main_json
import shutil

# Variable global para la referencia persistente a la imagen
imagen_tk = None

def ft_save_data(cap, app):
    _, frame = cap.read()

    # Crear una carpeta temporal
    temp_folder = "./data/temp_folder"
    os.makedirs(temp_folder, exist_ok=True)

    # Guardar la captura en la carpeta temporal
    image_path = os.path.join(temp_folder, "temp_capture.jpg")
    cv2.imwrite(image_path, frame)

    # Cargar la imagen capturada
    captured_image = Image.open(image_path)
    photo = ImageTk.PhotoImage(captured_image)

    # Mostrar la imagen en la ventana principal
    image_label = ctk.CTkLabel(app, image=photo, text="¡Foto capturada!", font=("Arial", 30))
    image_label.image = photo
    image_label.grid(row=2, column=0, padx=20, pady=0)

    # Label para el nombre de la foto
    name_label = ctk.CTkLabel(app, text="Ingresa nombre y apellido", width=600, height=50, font=("Arial", 20, "bold"))
    name_label.grid(row=3, column=0, padx=20, pady=10)

    # Entry para ingresar el nombre de la foto
    name_entry = ctk.CTkEntry(app, width=600, height=50, font=("Arial", 20), placeholder_text="Alexis Venegas...")
    name_entry.grid(row=4, column=0, padx=20, pady=10)

    def save_photo():
        # Obtener el nombre ingresado por el usuario
        photo_name = name_entry.get()

        # # Guardar la imagen con el nombre proporcionado en la carpeta temporal
        save_path_temp = os.path.join(temp_folder, f"{photo_name}.jpg")
        captured_image.save(save_path_temp)

        # Copiar la imagen a la carpeta 'faces' con extensión .jpg
        save_path_faces = os.path.join("faces", f"{photo_name}.jpg")
        shutil.copy(save_path_temp, save_path_faces)

        # Cambiar el nombre de la carpeta temporal al nombre de la imagen
        new_folder_name = os.path.join("./data", photo_name)
        os.rename(temp_folder, new_folder_name)
        
        if new_folder_name:
            try:
                main_json(photo_name, photo_name)
            except Exception as e:
                print(e)

        # Después de guardar la foto, destruir los elementos relacionados
        image_label.destroy()
        name_label.destroy()
        name_entry.destroy()
        save_button.destroy()

    # Botón para guardar la foto
    save_button = ctk.CTkButton(app, text="Guardar", command=save_photo, width=600, height=50, font=("Arial", 20))
    save_button.grid(row=5, column=0, padx=20, pady=20)