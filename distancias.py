import numpy as np

def levenshtein_matriz(x, y, threshold=None):
    # esta versiÃ³n no utiliza threshold, se pone porque se puede
    # invocar con Ã©l, en cuyo caso se ignora
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    for i in range(1, lenX + 1):
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1):
        D[0][j] = D[0][j - 1] + 1
        for i in range(1, lenX + 1):
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]),
            )
    return D[lenX, lenY]

def levenshtein_edicion(x, y, threshold=None):
    """
    Cálculo distancia de levenshtein con matriz y 
    recorrido
    """
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=int)
    for i in range(1, lenX + 1): # Rellena la primera fila
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1): # Para todas las filas
        D[0][j] = D[0][j - 1] + 1 # Rellenas el primer elemento
        for i in range(1, lenX + 1): # Para el resto de columnas
            D[i][j] = min(
                D[i - 1][j] + 1, # Inserción
                D[i][j - 1] + 1, # Borrado
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]), # Sustitución
            )
    posX, posY = D.shape[0] - 1, D.shape[1] - 1  # Desde el final
    secuencia = []
    while posX > 0 and posY > 0: # Recorremos toda la matriz
        # Calculamos los diferentes casos
        insercion = D[posX, posY - 1]
        borrado = D[posX - 1, posY]
        sustitucion = D[posX - 1, posY - 1]
        
        # Lógica para elegir la operación
        opMinCoste = min(insercion, borrado, sustitucion)
        if sustitucion == opMinCoste:
            op = (x[posX - 1], y[posY - 1])
            decrementoX, decrementoY = 1, 1
        elif insercion == opMinCoste:
            op = ('', y[posY - 1])
            decrementoX, decrementoY = 0, 1
        elif borrado == opMinCoste:
            op = (x[posX - 1], '')
            decrementoX, decrementoY = 1, 0
        else:
            print("Error en edición")
            exit()
        
        # Añadimos la operación y reducimos los índices
        secuencia.append(op)
        posX -= decrementoX
        posY -= decrementoY
    # Si llegamos a una pared entonces suponemos inserciones o borrados
    while posY > 0:
        secuencia.append(('', y[posY - 1]))
        posY -= 1
    while posX > 0:
        secuencia.append((x[posX - 1], ''))
        posX -= 1
    # Devolvemos las operaciones en el orden correcto
    secuencia = secuencia[::-1]
    return D[lenX, lenY], secuencia

def levenshtein_reduccion(x, y, threshold=None):
    # completar versiÃ³n con reducciÃ³n coste espacial
    return 0 # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein(x, y, threshold):
    # completar versiÃ³n reducciÃ³n coste espacial y parada por threshold
    return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein_cota_optimista(x, y, threshold):
    return 0 # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted_matriz(x, y, threshold=None):
    # completar versiÃ³n Damerau-Levenstein restringida con matriz
    lenX, lenY = len(x), len(y)
    # COMPLETAR
    return D[lenX, lenY]

def damerau_restricted_edicion(x, y, threshold=None):
    # partiendo de damerau_restricted_matriz aÃ±adir recuperar
    # secuencia de operaciones de ediciÃ³n
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted(x, y, threshold=None):
    # versiÃ³n con reducciÃ³n coste espacial y parada por threshold
     return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_intermediate_matriz(x, y, threshold=None):
    # completar versiÃ³n Damerau-Levenstein intermedia con matriz
    return D[lenX, lenY]

def damerau_intermediate_edicion(x, y, threshold=None):
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int64)
    for i in range(1, lenX + 1): 
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1): 
        D[0][j] = D[0][j - 1] + 1
        for i in range(1, lenX + 1):
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]),
            )
            if (i > 1 and j > 1)\
                and (x[i - 2] == y[j - 1] and x[i - 1] == y[j - 2]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 2][j - 2] + 1
                )

            #acb -> ba
            if (i > 2 and j > 1)\
                and (x[i - 3] == y[j - 1] and x[i - 1] == y[j - 2]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 3][j - 2] + 2
                )

            #ab -> bca
            if (i > 1 and j > 2)\
                and (x[i - 2] == y[j - 1] and x[i - 1] == y[j - 3]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 2][j - 3] + 2
                )

    posX, posY = D.shape[0] - 1, D.shape[1] - 1
    secuencia = []
    while posX > 0 and posY > 0:
        insercion = D[posX, posY - 1]
        borrado = D[posX - 1, posY]
        sustitucion = D[posX - 1, posY - 1]

        if (posX > 1 and posY > 1)\
                and (x[posX - 2] == y[posY - 1] and x[posX - 1] == y[posY - 2]):
            intercambio2_2 = D[posX - 2, posY - 2]
        else:
            intercambio2_2 = float('inf')
        if (posX > 2 and posY > 1)\
                and (x[posX - 3] == y[posY - 1] and x[posX - 1] == y[posY - 2]):
            intercambio3_2 = D[posX - 3][posY - 2]
        else:
            intercambio3_2 = float('inf')
        if (posX > 1 and posY > 2)\
                and (x[posX - 2] == y[posY - 1] and x[posX - 1] == y[posY - 3]):
            intercambio2_3 = D[posX - 2][posY - 3]
        else:
            intercambio2_3 = float('inf')

        opMin = min (insercion, borrado, sustitucion, intercambio2_2, intercambio3_2, intercambio2_3)
        if (intercambio3_2 == opMin): # acb -> ba
            op = (str(x[posX - 3:posX]), str(y[posY - 2:posY]))
            decrementoX=3
            decrementoY=2
        elif (intercambio2_3 == opMin): # ab -> bca
            op = (str(x[posX - 2:posX]), str(y[posY - 3:posY]))
            decrementoX=2
            decrementoY=3
        elif (intercambio2_2 == opMin): # ab -> ba
            op = (str(x[posX - 2:posX]), str(y[posY - 2:posY]))
            decrementoX=2
            decrementoY=2
        elif (sustitucion == opMin): # sustitucion
            op = (x[posX - 1], y[posY - 1])
            decrementoX=1
            decrementoY=1
        elif (insercion == opMin): # insercion
            op = ('', y[posY - 1])
            decrementoX=0
            decrementoY=1
        elif (borrado == opMin): # borrado
            op = (x[posX - 1], '')
            decrementoX=1
            decrementoY=0
        else:
            print("Error en edición")
            exit()
        secuencia.append(op)
        posX -= decrementoX
        posY -= decrementoY
    while posY > 0:
        secuencia.append(('', y[posY - 1]))
        posY -= 1
    while posX > 0:
        secuencia.append((x[posX - 1], ''))
        posX -= 1
    secuencia = secuencia[::-1]
    return D[lenX, lenY], secuencia
    
def damerau_intermediate(x, y, threshold=None):
    # versiÃ³n con reducciÃ³n coste espacial y parada por threshold
    return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE
        
opcionesSpell = {
    'levenshtein_m': levenshtein_matriz,
    'levenshtein_r': levenshtein_reduccion,
    'levenshtein':   levenshtein,
    'levenshtein_o': levenshtein_cota_optimista,
    'damerau_rm':    damerau_restricted_matriz,
    'damerau_r':     damerau_restricted,
    'damerau_im':    damerau_intermediate_matriz,
    'damerau_i':     damerau_intermediate
}

opcionesEdicion = {
    'levenshtein': levenshtein_edicion,
    'damerau_r':   damerau_restricted_edicion,
    'damerau_i':   damerau_intermediate_edicion
}