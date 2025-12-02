import numpy as np

def limpiar_num(x):
    if abs(x) < 1e-9:
        return 0
    if abs(x - round(x)) < 1e-9:
        return int(round(x))
    return round(x, 4)

def vector_lindo(v):
    return "[" + ", ".join(str(limpiar_num(x)) for x in v) + "]"

class SistemaLineal:

    def __init__(self, A, b):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.A_aug = np.hstack((self.A, self.b.reshape(-1, 1)))


    # ================================
    # ESCALONAMIENTO (Gauss–Jordan)
    # ================================
    def gauss_jordan(self, M):
        M = M.astype(float)
        filas, cols = M.shape
        pivote_fila = 0

        for pivote_col in range(cols - 1):  # no se usa la última columna como pivote
            # buscar fila con mayor valor absoluto (evita división por 0)
            max_row = pivote_fila + np.argmax(np.abs(M[pivote_fila:, pivote_col]))

            if abs(M[max_row, pivote_col]) < 1e-9:
                continue  # columna no tiene pivote, pasa a la siguiente

            # intercambiar filas
            M[[pivote_fila, max_row]] = M[[max_row, pivote_fila]]

            # normalizar la fila del pivote
            M[pivote_fila] = M[pivote_fila] / M[pivote_fila, pivote_col]

            # eliminar otras filas
            for r in range(filas):
                if r != pivote_fila:
                    M[r] = M[r] - M[r, pivote_col] * M[pivote_fila]

            pivote_fila += 1
            if pivote_fila == filas:
                break

        return M


    # =========================
    # RANGO (contar filas no nulas)
    # =========================
    def rango(self, M):
        r = 0
        for fila in M:
            if np.any(np.abs(fila) > 1e-9):
                r += 1
        return r


    # =========================
    # CLASIFICACIÓN DEL SISTEMA
    # =========================
    def clasificar_sistema(self):
        R = self.gauss_jordan(self.A.copy())
        R_aug = self.gauss_jordan(self.A_aug.copy())

        rango_A = self.rango(R)
        rango_aug = self.rango(R_aug)

        n = self.A.shape[1]

        if rango_A < rango_aug:
            return "Sin solución"

        elif rango_A == rango_aug == n:
            return "Solución única"

        elif rango_A == rango_aug < n:
            return "Infinitas soluciones"

        else:
            return "Caso no esperado"


    # =========================
    # SOLUCIÓN PARTICULAR (si única)
    # =========================
    def resolver_unica(self):
        return np.linalg.solve(self.A, self.b).tolist()


    # =======================================================
    # ESPACIO NULO (nullspace) 
    # =======================================================
    def nullspace(self):
        R = self.gauss_jordan(self.A.copy())
        filas, cols = R.shape

        pivotes = []
        for i in range(filas):
            for j in range(cols):
                if abs(R[i, j]) > 1e-9:
                    pivotes.append(j)
                    break

        libres = [j for j in range(cols) if j not in pivotes]

        base = []
        for l in libres:
            v = np.zeros(cols)
            v[l] = 1

            fila_p = 0
            for col in pivotes:
                if abs(R[fila_p, col]) > 1e-9:
                    v[col] = -R[fila_p, l]
                    fila_p += 1
            base.append(v.tolist())

        return base
    # ======================================================
    # SOLUCIÓN GENERAL PARAMÉTRICA PARA INFINITAS SOLUCIONES
    # ======================================================
    def solucion_general_parametrica(self):
        # Obtener RREF del sistema aumentado
        R_aug = self.gauss_jordan(self.A_aug.copy())
        filas, cols = R_aug.shape
        n = cols - 1  # columnas de A

        # Identificar pivotes
        pivotes = []
        for i in range(filas):
            for j in range(n):
                if abs(R_aug[i, j]) > 1e-9:
                    pivotes.append(j)
                    break

        # Variables libres
        libres = [j for j in range(n) if j not in pivotes]

        # Solución particular (poner variable libres = 0)
        x_p = np.zeros(n)
        
        for i, col in enumerate(pivotes):
            x_p[col] = R_aug[i, -1]

        # Vectores paramétricos (uno por variable libre)
        vectores = []
        for k, libre in enumerate(libres):
            v = np.zeros(n)
            v[libre] = 1  # parámetro

            fila_p = 0
            for col in pivotes:
                if abs(R_aug[fila_p, col]) > 1e-9:
                    v[col] = -R_aug[fila_p, libre]
                    fila_p += 1

            vectores.append(v)

        return x_p.tolist(), vectores, libres



    # =========================
    # FUNCIÓN PRINCIPAL
    # =========================

    def resolver(self):
        clasificacion = self.clasificar_sistema()

        if clasificacion == "Sin solución":
            return {
                "clasificacion": clasificacion,
                "solucion": None
            }

        elif clasificacion == "Solución única":
            particular = self.resolver_unica()
            return {
                "clasificacion": clasificacion,
                "solucion": {
                    "unica": particular
                }
            }

        elif clasificacion == "Infinitas soluciones":
            x_p, vectores, libres = self.solucion_general_parametrica()

            expresion = "x = " + vector_lindo(x_p)
            for i, v in enumerate(vectores):
                expresion += f"  +  t{i+1} * {vector_lindo(v)}"

            return {
                "clasificacion": clasificacion,
                "solucion": {
                    "particular": x_p,
                    "vectores_parametricos": vectores,
                    "variables_libres": libres,
                    "expresion_parametrica": expresion
                }
            }

        else:
            return {"clasificacion": "Caso no esperado"}








    