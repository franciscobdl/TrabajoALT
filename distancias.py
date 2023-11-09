import numpy as np

def levenshtein_matriz(x, y, threshold=None):
    # esta versión no utiliza threshold, se pone porque se puede
    # invocar con él, en cuyo caso se ignora
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=int)
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
    # a partir de la versión levenshtein_matriz
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein_reduccion(x, y, threshold=None):
    # completar versión con reducción coste espacial
    lenX, lenY = len(x), len(y)
    Vcurrent = np.zeros(lenX + 1, dtype=int)
    Vprev = np.zeros(lenX + 1, dtype=int)
    Vcurrent[0]=0

    for i in range(1, lenX + 1):
       Vcurrent[i] = Vcurrent[i - 1] + 1

    for j in range(1, lenY + 1):
        Vcurrent, Vprev = Vprev, Vcurrent
        Vcurrent[0] = Vprev[0] + 1
        for i in range(1, lenX + 1):
            Vcurrent[i] = min(Vcurrent[i - 1] + 1, Vprev[i] + 1, Vprev[i - 1] + (x[i - 1] != y[j - 1]),)
        
    return Vcurrent[lenX] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein(x, y, threshold):
    # completar versión reducción coste espacial y parada por threshold
    lenX, lenY = len(x), len(y)
    Vcurrent = np.zeros(lenX + 1, dtype=int)
    Vprev = np.zeros(lenX + 1, dtype=int)
    Vcurrent[0]=0
    next=0

    for i in range(1, lenX + 1):
       Vcurrent[i] = Vcurrent[i - 1] + 1

    for j in range(1, lenY + 1):
        Vprev,Vcurrent=Vcurrent,Vprev
        Vcurrent[0] = Vprev[0] + 1
        for i in range(1, lenX + 1):
            Vcurrent[i] = min(Vcurrent[i - 1] + 1, Vprev[i] + 1, Vprev[i - 1] + (x[i - 1] != y[j - 1]),)
            if i != lenX:
                Vnext = Vcurrent
                Vnext[i+1] = min(Vnext[i] + 1, Vcurrent[i + 1] + 1, Vcurrent[i] + (x[i] != y[j - 1]),)
                # Parada  si estamos en vector columna y este ya tiene un valor igual o superior
                # al umbral proporcionado (threshold)
            if Vcurrent[i] >= threshold + 1:
                return threshold + 1

    return min(Vcurrent[lenX],threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein_cota_optimista(x, y, threshold):
    return 0 # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted_matriz(x, y, threshold=None):
    # completar versión Damerau-Levenstein restringida con matriz
    # COMPLETAR
    #return D[lenX, lenY]
    return 0

def damerau_restricted_edicion(x, y, threshold=None):
    # partiendo de damerau_restricted_matriz añadir recuperar
    # secuencia de operaciones de edición
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted(x, y, threshold=None):
    # versión con reducción coste espacial y parada por threshold
     return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_intermediate_matriz(x, y, threshold=None):
    # completar versión Damerau-Levenstein intermedia con matriz
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=int)
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


def damerau_intermediate_edicion(x, y, threshold=None):
    # partiendo de matrix_intermediate_damerau añadir recuperar
    # secuencia de operaciones de edición
    # completar versión Damerau-Levenstein intermedia con matriz
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE
    
def damerau_intermediate(x, y, threshold=None):
    # versión con reducción coste espacial y parada por threshold
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

