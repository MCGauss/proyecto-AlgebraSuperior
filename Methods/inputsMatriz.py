'''
    El programa presenta la codificación 
    para la validación de entradas de cualquier
    matriz cuadrada asociada a un determinado SEL.
'''
import numpy as np

#Input para num de filas y columnas
def pedirFilCol():
    while True:
        fStr = input("Número de filas de la matriz A: ")
        cStr = input("Número de columnas de la matriz A: ")
        
        #Validar si se recibe una entrada numérica
        try:
          filas = int(fStr)
          cols = int(cStr)
          
          if filas != cols: print("El método requiere de una matriz cuadrada.\n")
          elif filas < 2: print("El método sirve a partir de sistemas 2x2.\n")
          else: return filas, cols
          
        except ValueError:
          print("Error: Por favor ingrese valores válidos.\n")


#Input de los elementos de la matriz
def llenarMatriz(filas, cols):
   print("\nIngrese los valores para la matriz de coeficientes A:\n")
   matriz = []

   #Generar una lista de listas
   for i in range(filas):
       fila = []
       for j in range(cols):
           while True:
               inp = input(f"A[{i+1}][{j+1}]: ")
               try:
                   valor = float(inp)
                   fila.append(valor)
                   break
               except ValueError:
                   print("Error: La entrada debe ser un número válido.\n")
       matriz.append(fila)
   
   #Convertir a array
   A = np.array(matriz)
   return A

#Input del vector de términos independientes
def llenarVectorB(filas):
    print("\nIngrese los valores del vector de términos independientes b: ")
    b = []
    
    #Generar lista
    for i in range(filas):
        while True:
            inp = input(f"b[{i+1}]: ")
            try:
                valor = float(inp)
                b.append(valor)
                break
            except ValueError:
                print("Las entradas deben ser numéricas.\n")
             
    #Convertir a arreglo (vectorial)
    b = np.array(b)
    bCol = np.transpose([b])
    return bCol
                
def mostrarDatos(A, b):
    print("\nMatriz de coeficientes: \nA= ")
    print(A)
    print("\nVector de términos independientes: \nb= ")
    print(b)
    
def diagonalDominante(A, b):
    n = len(A)
    #Almacenar los inputs 
    A = A.copy()
    b = b.copy()

    # Buscar la fila donde el elemento[k][i] sea dominante
    for i in range(n):
        maxFila = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[maxFila][i]):
                maxFila = k
        
        # Intercambiar filas
        if maxFila != i:
            A[[i, maxFila]] = A[[maxFila, i]]
            b[[i, maxFila]] = b[[maxFila, i]]

        # Comprobar diagonal dominante: sum -> suma de elementos de estructura iterable
        sumaDiag = sum(abs(A[i,j]) for j in range(n) 
                       if j != i)
        if abs(A[i,i]) < sumaDiag:
            return None, None

    return A, b
    print("\nMatriz diagonal dominante: ")
    print(A)

            
def mainInputs():
    print("**SEL EN FORMA MATRICIAL***")
    filas, cols = pedirFilCol()
    A = llenarMatriz(filas, cols)
    bCol = llenarVectorB(filas)
    mostrarDatos(A, bCol)
    
    return A, bCol
