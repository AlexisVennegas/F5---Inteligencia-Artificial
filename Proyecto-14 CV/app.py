import face_recognition
import cv2
import numpy as np
import os, sys
import math
import customtkinter
from PIL import Image, ImageTk
import threading
from Save_data.Save_dt import ft_save_data


font_scale = 2e-3
thickness_scale = 1e-3

def optimal_font_dims(img, font_scale , thickness_scale):
    """
    Get optimal font dimensions for the given image
    :param img: Image to get the optimal font dimensions
    :param font_scale:
    :param thickness_scale:
    :return:
    """
    h, w, _ = img.shape
    font_scale = min(w, h) * font_scale
    thickness = math.ceil(min(w, h) * thickness_scale)
    return font_scale, thickness

def face_confidence(face_distance, face_match_threshold=0.4):
    """
    Get the confidence of the face
    :param face_distance: Distance between the face and the known face
    :param face_match_threshold: Threshold to consider a face as a match
    :return: Confidence of the face
    """
    rango = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (rango * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


class FaceRecognition:
    """
    Class to recognize faces
    
    """
    face_locations = []
    face_encodings = []
    face_names = []
    faces_confidences = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True
    global font_scale
    global thickness_scale



    def __init__(self, root, cap):
        self.root = root
        self.cap = cap
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.faces_confidences = []
        self.known_face_encodings = []
        self.known_face_names = []
        self.process_current_frame = True
        self.encode_faces()

        # customtkinter
        self.root.title("Face Recognition App")
        self.root.geometry("1300x1000")
        self.root.grid_columnconfigure(0, weight=1)

        self.camera_frame = customtkinter.CTkFrame(self.root)
        self.camera_frame.grid(row=2, column=0, pady=0)
        
        self.camera_label = customtkinter.CTkLabel(self.camera_frame, text="")
        self.camera_label.pack()

        self.buttons_frame = customtkinter.CTkFrame(self.root)
        self.buttons_frame.grid(row=1, column=0, padx=20, pady=5)

        self.button1 = customtkinter.CTkButton(self.buttons_frame, text="Agregar Persona", command=self.capture_image, width=600, height=50, font=("Arial", 20))
        self.button1.grid(row=0, column=0, padx=20, pady=5, sticky="ew")

        self.run_recognition_thread = threading.Thread(target=self.run_recognition)
        self.run_recognition_thread.daemon = True
        self.run_recognition_thread.start()


    def encode_faces(self):
        """

        :return:
        """
        for image in os.listdir('faces'):
            face_image = face_recognition.load_image_file(f'faces/{image}')
            # esto sirve para codificar la imagen y poder compararla con las demas, es importante ya que si no se hace esto no se podra comparar
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)

        print(self.known_face_names)

    def capture_image(self):
        # Implement your code to capture and save an image
        ft_save_data(self.cap, self.root) # Replace with your actual implementation



    def run_recognition(self):
        if not self.cap.isOpened():
            sys.exit("No se pudo abrir la cámara")

        while True:
            ret, frame = self.cap.read()

            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # Encontrar todas las caras en el fotograma actual del video
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # Verificar si la cara es una coincidencia con las caras conocidas
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Desconocido"
                    confidence = "0%"

                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:  # Encontrar una coincidencia
                        name = self.known_face_names[best_match_index]
                        confidence = face_confidence(face_distances[best_match_index])

                        name_without_extension, _ = os.path.splitext(name)

                        self.face_names.append(name_without_extension)
                        self.faces_confidences.append(confidence)
                    else:
                        self.face_names.append(name)

            self.process_current_frame = not self.process_current_frame

            for (x, y, w, h), name in zip(self.face_locations, self.face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                x *= 4
                y *= 4
                w *= 4
                h *= 4


                # Get optimal font dimensions
                font_scale = 5e-4
                thickness_scale = 7.5e-4
                font_scale, thickness = optimal_font_dims(frame, font_scale, thickness_scale)
                
                # Change color box depending on the name
                if name == 'Desconocido' or confidence < '70.0%':
                    color_box = (0, 0, 255) # Red
                    acceso_text = "ACCESO DENEGADO"
                elif confidence >= '70.0%':
                    color_box = (72, 131, 72) # Green
                    acceso_text = "ACCESO PERMITIDO"

                # draw a rectangle around the face
                cv2.rectangle(frame, (h, x), (y, w), color_box, 2)
                # draw a filled rectanle below the face
                cv2.rectangle(frame, (h, w + 1), (y, w + 100), color_box, -1)

                font = cv2.FONT_HERSHEY_DUPLEX
                name_text = f"{name}"
                confidence_text = f"{confidence}"
                cv2.putText(frame, name_text, (h + 6, w + 20), font, font_scale, (255, 255, 255), thickness)
                if name != 'Desconocido' and confidence >= '70.0%':
                    cv2.putText(frame, confidence_text, (h + 6, w + 55), font, font_scale, (255, 255, 255), thickness)
                    cv2.putText(frame, acceso_text, (h + 6, w + 90), font, font_scale, (255, 255, 255), thickness)
                else:
                    cv2.putText(frame, acceso_text, (h + 6, w + 90), font, font_scale, (255, 255, 255), thickness)


            # cv2.imshow('Reconocimiento Facial', frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.camera_label.configure(image=photo)
            self.camera_label.image = photo

            self.root.update()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    # main para iniciar la aplicación
    root = customtkinter.CTk()
    cap = cv2.VideoCapture(0)
    cap.set(3, 1150)
    cap.set(4, 800)
    cap.set(cv2.CAP_PROP_FPS, 60)
    fr = FaceRecognition(root, cap)
    # fr.run_recognition()
    root.mainloop()