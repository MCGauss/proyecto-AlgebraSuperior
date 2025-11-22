'''
    El presente programa contiene el método de Gauss,
    el cual se caracteriza por llevar a la matriz de
    coeficientes asociada al SEL a una forma triangular
    superior conforme a su diagonal principal.
'''
import numpy as np
from Methods.inputsMatriz import mainInputs as ingresarDatos

#Método de Gauss
def metodoGauss(A, b):
    n = len(A)
    # Convertir a float para evitar errores
    A = A.astype(float)
    b = b.astype(float)
    
    # Eliminación hacia adelante
    for k in range(n-1):
        if A[k, k] == 0:
            print(f"Cero en el pivote A[{k},{k}] — se recomienda un pivoteo parcial.")
            continue
        
        #Calcular el factor
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]

    #Convertir b a columna
    bCol = np.transpose([b])
    
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        suma = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - suma) / A[i, i]

    return x, A, bCol

def mostrarResultado(x, A, bCol):
    print("\n*****RESULTADOS*****")
    print("\nMatriz triangular superior (A):")
    print(A)
    print("\nVector modificado (b):")
    print(bCol)
    print("\nSolución del sistema (x):")
    for i, xi in enumerate(x):
        print(f"x{i+1} = {xi:.6f}")

def mainGauss():
    print("*****MÉTODO DE GAUSS*****\n")
    
    #Mandar a llamar el archivo que valida los inputs
    A, b = ingresarDatos()
    
    #Aplicar método de Gauss
    x, ATrian, bNuevo = metodoGauss(A, b)
    
    # Mostrar resultados
    mostrarResultado(x, ATrian, bNuevo)

