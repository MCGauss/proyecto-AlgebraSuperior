import tkinter as tk
from tkinter import messagebox
from Methods.inputsMatriz import VentanaMatriz
from Methods.Gauss import SistemaLineal

class VentanaGauss:
    def __init__(self, root):
        self.root = root
        self.root.title("Método de Gauss - Clasificación y Solución")

        tk.Label(root, text="Tamaño del sistema (n):").pack(pady=5)
        self.n_entry = tk.Entry(root)
        self.n_entry.pack()

        tk.Button(root, text="Ingresar matriz", command=self.ingresar_matriz).pack(pady=10)

    def ingresar_matriz(self):
        try:
            n = int(self.n_entry.get())
            if n <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Ingrese un número válido")
            return

        VentanaMatriz(self.root, n, self.procesar)

    def procesar(self, A, b):
        sistema = SistemaLineal(A, b)
        resultado = sistema.resolver()

        msg = f"Clasificación del sistema:\n{resultado['clasificacion']}\n\n"

        sol = resultado["solucion"]

        # ===============================
        # CASO 1: Sistema SIN SOLUCIÓN
        # ===============================
        if sol is None:
            msg += "El sistema no tiene solución."
            messagebox.showinfo("Resultado", msg)
            return

        # ===============================
        # CASO 2: Solución única
        # ===============================
        if "unica" in sol:
            msg += f"Solución única:\n{sol['unica']}"
            messagebox.showinfo("Resultado", msg)
            return

        # ===============================
        # CASO 3: Infinitas soluciones
        # ===============================
        msg += "Solución general paramétrica:\n\n"
        msg += f"Solución particular:\n{sol['particular']}\n\n"
        msg += "Vectores paramétricos:\n"
        for v in sol["vectores_parametricos"]:
            msg += f"{v}\n"
        msg += "Expresión completa:\n"
        msg += sol["expresion_parametrica"]

        messagebox.showinfo("Resultado", msg)



if __name__ == "__main__":
    root = tk.Tk()
    VentanaGauss(root)
    root.mainloop()


# ====================================================
# FUNCIÓN ventanaGauss() 
# ====================================================
def ventanaGauss():
    root = tk.Toplevel()
    VentanaGauss(root)
    root.mainloop()






