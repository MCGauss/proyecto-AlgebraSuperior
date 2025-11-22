import sys
import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))          # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)                      # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

"""##################################################
"""

import tkinter as tk
from tkinter import messagebox
from Methods.Gauss import metodoGauss
import numpy as np


def ventanaGauss():
    sub = tk.Toplevel()
    sub.title("Método de Gauss")
    sub.geometry("600x600")

    # ===========================
    # SECCIÓN 1: Elegir tamaño n
    # ===========================
    tk.Label(sub, text="Método de Gauss",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Ingrese el tamaño de la matriz (nxn):",
             font=("Arial", 12)).pack()

    entrada_n = tk.Entry(sub, width=5, font=("Arial", 12))
    entrada_n.pack()

    frame_matriz = tk.Frame(sub)
    frame_vector = tk.Frame(sub)

    entradas_A = []
    entradas_b = []

    # ===========================
    # Crear matriz dinámica
    # ===========================
    def crear_matriz():
        nonlocal entradas_A, entradas_b

        # Limpiar posibles widgets anteriores
        for w in frame_matriz.winfo_children():
            w.destroy()
        for w in frame_vector.winfo_children():
            w.destroy()

        entradas_A = []
        entradas_b = []

        try:
            n = int(entrada_n.get())
            if n < 2:
                raise ValueError("n debe ser mayor o igual a 2")
        except:
            messagebox.showerror("Error", "Ingresa un valor entero válido para n.")
            return

        tk.Label(sub, text=f"Ingrese los valores de la matriz A ({n} × {n}):",
                 font=("Arial", 12)).pack(pady=5)
        frame_matriz.pack(pady=5)

        # Crear campos A
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(frame_matriz, width=6, font=("Arial", 11))
                e.grid(row=i, column=j, padx=3, pady=3)
                fila.append(e)
            entradas_A.append(fila)

        tk.Label(sub, text=f"Ingrese el vector b ({n} x 1):",
                 font=("Arial", 12)).pack(pady=5)
        frame_vector.pack()

        # Crear campos b
        for i in range(n):
            e = tk.Entry(frame_vector, width=6, font=("Arial", 11))
            e.grid(row=i, column=0, pady=3)
            entradas_b.append(e)

        btn_resolver.pack(pady=15)

    # Botón para generar matriz
    tk.Button(sub, text="Crear matriz", font=("Arial", 12),
              command=crear_matriz).pack(pady=10)

    # ===========================
    # Resolver Gauss
    # ===========================
    def resolver_gauss():
        try:
            n = int(entrada_n.get())

            # Leer matriz A
            A = np.zeros((n, n), float)
            for i in range(n):
                for j in range(n):
                    A[i][j] = float(entradas_A[i][j].get())

            # Leer vector b
            b = np.zeros(n, float)
            for i in range(n):
                b[i] = float(entradas_b[i].get())

            # Ejecutar método de Gauss
            x, Atriangular, bCol = metodoGauss(A, b)

            # Mostrar resultados
            texto = "Solución del sistema:\n"
            for i, val in enumerate(x):
                texto += f"x{i+1} = {val:.6f}\n"

            texto += "\nMatriz triangular superior A:\n"
            texto += str(Atriangular)

            texto += "\n\nVector resultante b:\n"
            texto += str(bCol)

            messagebox.showinfo("Resultados", texto)

        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema:\n{e}")

    btn_resolver = tk.Button(sub, text="Resolver sistema",
                             font=("Arial", 12),
                             command=resolver_gauss)
    btn_resolver.pack_forget()  # Oculto hasta crear la matriz