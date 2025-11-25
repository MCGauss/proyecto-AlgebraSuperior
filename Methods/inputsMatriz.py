import tkinter as tk
from tkinter import messagebox

class VentanaMatriz:
    def __init__(self, root, n, callback):
        self.n = n
        self.callback = callback

        self.win = tk.Toplevel(root)
        self.win.title("Ingresar matriz A y vector b")

        tk.Label(self.win, text="Matriz A").grid(row=0, column=0, columnspan=n)

        self.entradas_A = []
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(self.win, width=5)
                e.grid(row=i+1, column=j)
                fila.append(e)
            self.entradas_A.append(fila)

        tk.Label(self.win, text="Vector b").grid(row=0, column=n+1)
        self.entradas_b = []
        for i in range(n):
            e = tk.Entry(self.win, width=5)
            e.grid(row=i+1, column=n+1)
            self.entradas_b.append(e)

        tk.Button(self.win, text="Procesar", command=self.enviar).grid(
            row=n+2, column=0, columnspan=n+2, pady=10
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

