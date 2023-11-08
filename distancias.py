import numpy as np

def levenshtein_matriz(x, y, threshold=None):
    # esta versión no utiliza threshold, se pone porque se puede
    # invocar con él, en cuyo caso se ignora
    lenX, lenY = len(x), len(y) # longitud de las cadenas
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int) # matriz de distancias
    for i in range(1, lenX + 1): # inicializar primera columna
        D[i][0] = D[i - 1][0] + 1   
    for j in range(1, lenY + 1): # inicializar primera fila
        D[0][j] = D[0][j - 1] + 1
        for i in range(1, lenX + 1): # completar el resto de la matriz
            D[i][j] = min( # mínimo de las tres operaciones
                D[i - 1][j] + 1, 
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]), # suma 0 si son iguales, 1 si son distintas
            )
    return D[lenX, lenY]

def levenshtein_edicion(x, y, threshold=None):
    # a partir de la versión levenshtein_matriz
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein_reduccion(x, y, threshold=None):
    # completar versión con reducción coste espacial
    return 0 # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein(x, y, threshold):
    # completar versión reducción coste espacial y parada por threshold
    return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein_cota_optimista(x, y, threshold):
    dic = {}
    for i in x:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for j in y:
        if j not in dic:
            dic[j] = -1
        else:
            dic[j] -= 1

    pos = 0
    neg = 0
    for v in dic.values():
        if v > 0:
            pos += v
        elif v < 0:
            neg += v
    cota = max(abs(pos), abs(neg))
    if cota < threshold: #si la cota optimista es menor que el threshold, se llama a levenshtein
        res = levenshtein(x, y, threshold)
    else: res = threshold + 1

    return res  
    
def damerau_restricted_matriz(x, y, threshold=None):
    # completar versión Damerau-Levenstein restringida con matriz
    #PRUEBA
    return 0
    # COMPLETAR

def damerau_restricted_edicion(x, y, threshold=None):
    # partiendo de damerau_restricted_matriz añadir recuperar
    # secuencia de operaciones de edición
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted(x, y, threshold=None):
    # versión con reducción coste espacial y parada por threshold
     return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_intermediate_matriz(x, y, threshold=None):
    # completar versión Damerau-Levenstein intermedia con matriz
    return 0

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

