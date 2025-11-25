import sys
import os

from PIL import Image, ImageTk
import tkinter as tk
from GraphicInterface.ventanaPortada import ventanaPortada

ruta_actual = os.path.dirname(os.path.abspath(__file__))   # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)               # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)


def pantallaFinal(root):

    for w in root.winfo_children():
        w.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    # ==============================
    #     CARGAR IMAGEN JPEG
    # ==============================
    ruta_imagen = os.path.join(ruta_proyecto,"Assets", "naruto1.jpeg")

    try:
        img = Image.open(ruta_imagen)

        # Opcional: reducir tamaño si la imagen es grande
        img = img.resize((450, 200))  # puedes modificarlo

        img_tk = ImageTk.PhotoImage(img)

        label_img = tk.Label(frame, image=img_tk)
        label_img.image = img_tk  # ← evita que Python libere la imagen
        label_img.pack(pady=10)

    except Exception as e:
        print("Error cargando imagen:", e)

    # ==============================
    #            TÍTULO
    # ==============================
    titulo = tk.Label(frame,
                      text="¡Gracias por usar Gauss-Solvex!",
                      font=("Georgia", 22, "bold"))
    titulo.pack(pady=15)

    creditos = tk.Label(frame,
                        text=("Este programa fue desarrollado en FES Acatlán UNAM.\n"
                              "Elaborado por:\n"
                              "Jacobo Santos Marco Antonio"),
                        font=("Arial", 14),
                        justify="center")
    creditos.pack(pady=20)

    btn_volver = tk.Button(frame, text="Regresar al inicio",
                           font=("Arial", 14),
                           width=18,
                           command=lambda: ventanaPortada(root))
    btn_volver.pack(pady=10)

    btn_salir = tk.Button(frame, text="Salir",
                          font=("Arial", 14),
                          width=18,
                          command=root.destroy)
    btn_salir.pack(pady=10)

