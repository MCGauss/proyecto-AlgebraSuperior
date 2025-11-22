import sys
import os

# Rutas
ruta_actual = os.path.dirname(os.path.abspath(__file__))   # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)               # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

import tkinter as tk
from GraphicInterface.ventanaGauss import ventanaGauss
from GraphicInterface.pantallaFinal import pantallaFinal


def ventanaIntro(root):

    for w in root.winfo_children():
        w.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    titulo = tk.Label(frame, text="Introducción",
                      font=("Georgia", 24, "bold"))
    titulo.pack(pady=15)

    texto = (
        "Este sistema permite resolver sistemas de ecuaciones lineales\n"
        "por el método de Gauss. El programa ofrece:\n\n"
        "• Ingresar un sistema de ecuaciones de forma gráfica.\n"
        "• Determinar si el sistema tiene solución única.\n"
        "• Determinar si no tiene solución.\n"
        "• Determinar si tiene soluciones infinitas y mostrar la solución general."
    )

    lbl = tk.Label(frame, text=texto,
                   font=("Arial", 14), justify="left")
    lbl.pack(pady=20)

    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=20)

    btn_continuar = tk.Button(btn_frame, text="Continuar",
                              font=("Arial", 14),
                              width=15,
                              command=lambda: ventanaGauss())
    btn_continuar.grid(row=0, column=0, padx=10)

    btn_salir = tk.Button(btn_frame, text="Salir",
                          font=("Arial", 14),
                          width=15,
                          command=lambda: pantallaFinal(root))
    btn_salir.grid(row=0, column=1, padx=10)
