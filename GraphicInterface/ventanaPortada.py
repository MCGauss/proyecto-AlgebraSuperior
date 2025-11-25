import sys
import os

# Rutas
ruta_actual = os.path.dirname(os.path.abspath(__file__))   # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)               # /Proyecto

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

#Librerias
import tkinter as tk

def ventanaPortada(root):

    from GraphicInterface.introduccion import ventanaIntro 

    for widget in root.winfo_children():
        widget.destroy()

        root.title("Gauss-Solvex")

    contenedor = tk.Frame(root)
    contenedor.pack(expand=True)

    tk.Label(contenedor,
             text="Universidad Nacional Autónoma de México",
             font=("Arial", 14, "bold")).pack(pady=5)

    tk.Label(contenedor,
             text="Facultad de Estudios Superiores Acatlán",
             font=("Arial", 13)).pack(pady=3)

    tk.Label(contenedor,
             text="Lic. en Matemáticas Aplicadas y Computación",
             font=("Arial", 12)).pack(pady=3)

    tk.Label(contenedor,
             text="Algebra Superior",
             font=("Arial", 12)).pack(pady=3)

    tk.Label(contenedor,
             text="Profesor: Héctor Axel Saavedra Luis",
             font=("Arial", 12)).pack(pady=10)
    
    tk.Label(contenedor,
             text="Desarrollado por:\n\n"
                  " - Jacobo Santos Marco Antonio\n",
             font=("Arial", 12),
             justify="center").pack(pady=15)
    
    tk.Label(contenedor,
             text="Gauss-Solvex",
             font=("Arial", 40, "bold")).pack(pady=15)


    tk.Button(contenedor,
              text="Continuar",
              width=20,
              height=2,
              font=("Arial", 12),
              command=lambda: ventanaIntro(root)).pack(pady=30)
