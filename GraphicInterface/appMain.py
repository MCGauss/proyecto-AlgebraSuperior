import sys
import os

# Rutas
ruta_actual = os.path.dirname(os.path.abspath(__file__))   # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)               # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

# Librerías
import tkinter as tk
import pygame

# Importación de pantallas
from GraphicInterface.ventanaPortada import ventanaPortada


def main():
    # Inicializar pygame para música
    pygame.mixer.init()
    ruta_musica = os.path.join(ruta_proyecto, "Assets", "Homecoming.mp3")

    if os.path.exists(ruta_musica):
        pygame.mixer.music.load(ruta_musica)
        pygame.mixer.music.play(-1)  # Repetir en bucle

    # Crear ventana principal
    root = tk.Tk()
    root.title("Proyecto Gauss - PySolve Interactive")
    root.geometry("700x500")
    root.minsize(500, 400)

    # Lanzar la portada
    ventanaPortada(root)

    root.mainloop()
