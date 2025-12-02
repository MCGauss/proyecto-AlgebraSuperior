import tkinter as tk
from tkinter import messagebox

class VentanaMatriz:
    def __init__(self, root, n, callback):
        self.n = n
        self.callback = callback

        self.win = tk.Toplevel(root)
        self.win.title("Ingresar Sistema")

        # =================================================
        # FRAME CENTRAL (esto permite centrar toda la matriz)
        # =================================================
        frame = tk.Frame(self.win)
        frame.pack(expand=True)   #  centra contenido horizontal y verticalmente

        # ---- Etiqueta de A ----
        tk.Label(frame, text="Matriz A").grid(row=0, column=0, columnspan=n, pady=5)

        # ---- Entradas de A ----
        self.entradas_A = []
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(frame, width=6)
                e.grid(row=i+1, column=j, padx=4, pady=4)
                fila.append(e)
            self.entradas_A.append(fila)

        # ---- Etiqueta de b ----
        tk.Label(frame, text="Vector b").grid(row=0, column=n+1, padx=10)

        # ---- Entradas de b ----
        self.entradas_b = []
        for i in range(n):
            e = tk.Entry(frame, width=6)
            e.grid(row=i+1, column=n+1, padx=10)
            self.entradas_b.append(e)

        # ---- Botón Procesar ----
        tk.Button(frame, text="Procesar", command=self.enviar).grid(
            row=n+2, column=0, columnspan=n+2, pady=12
        )

    def enviar(self):
        try:
            A = [[float(self.entradas_A[i][j].get()) for j in range(self.n)] for i in range(self.n)]
            b = [float(self.entradas_b[i].get()) for i in range(self.n)]
        except:
            messagebox.showerror("Error", "Todos los valores deben ser numéricos")
            return

        self.callback(A, b)
        self.win.destroy()

