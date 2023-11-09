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
        ins = D[posX, posY - 1]
        bor = D[posX - 1, posY]
        sus = D[posX - 1, posY - 1]
        
        # Lógica para elegir la operación
        opMin = min(ins, bor, sus)
        if sus == opMin:
            op = (x[posX - 1], y[posY - 1])
            decX, decY = 1, 1
        elif ins == opMin:
            op = ('', y[posY - 1])
            decX, decY = 0, 1
        elif bor == opMin:
            op = (x[posX - 1], '')
            decX, decY = 1, 0
        else:
            print("Error en edición")
            exit()
        
        # Añadimos la operación y reducimos los índices
        secuencia.append(op)
        posX -= decX
        posY -= decY
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
        ins = D[posX, posY - 1]
        bor = D[posX - 1, posY]
        sus = D[posX - 1, posY - 1]

        if (posX > 1 and posY > 1)\
                and (x[posX - 2] == y[posY - 1] and x[posX - 1] == y[posY - 2]):
            dInt = D[posX - 2, posY - 2]
        else:
            dInt = float('inf')
        if (posX > 2 and posY > 1)\
                and (x[posX - 3] == y[posY - 1] and x[posX - 1] == y[posY - 2]):
            dInt3_2 = D[posX - 3][posY - 2]
        else:
            dInt3_2 = float('inf')
        if (posX > 1 and posY > 2)\
                and (x[posX - 2] == y[posY - 1] and x[posX - 1] == y[posY - 3]):
            dInt2_3 = D[posX - 2][posY - 3]
        else:
            dInt2_3 = float('inf')

        opMin = min (ins, bor, sus, dInt, dInt3_2, dInt2_3)
        if (dInt3_2 == opMin): # acb -> ba
            op = (str(x[posX - 3:posX]), str(y[posY - 2:posY]))
            decX=3
            decY=2
        elif (dInt2_3 == opMin): # ab -> bca
            op = (str(x[posX - 2:posX]), str(y[posY - 3:posY]))
            decX=2
            decY=3
        elif (dInt == opMin): # ab -> ba
            op = (str(x[posX - 2:posX]), str(y[posY - 2:posY]))
            decX=2
            decY=2
        elif (sus == opMin): # sus
            op = (x[posX - 1], y[posY - 1])
            decX=1
            decY=1
        elif (ins == opMin): # ins
            op = ('', y[posY - 1])
            decX=0
            decY=1
        elif (bor == opMin): # bor
            op = (x[posX - 1], '')
            decX=1
            decY=0
        else:
            print("Error en edición")
            exit()
        secuencia.append(op)
        posX -= decX
        posY -= decY
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
