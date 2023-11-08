import numpy as np

def levenshtein_matriz(x, y, threshold=None):
    # esta versión no utiliza threshold, se pone porque se puede
    # invocar con él, en cuyo caso se ignora
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
    # a partir de la versión levenshtein_matriz
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    for i in range(1, lenX + 1): # rellena la primera fila
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1): # para todas las filas
        D[0][j] = D[0][j - 1] + 1 # rellena el primer elemento
        for i in range(1, lenX + 1): #para las columnas
            D[i][j] = min(
                D[i - 1][j] + 1, #ins
                D[i][j - 1] + 1, # bor
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]), #sust
            )
    posX,posY = D.shape[0] -1, D.shape[1]-1 #para empezar por el final
    secuencia = []
    while posX > 0 and posY > 0: #recorrer matriz
        # se miran los casos
        ins= D[posX, posY -1]
        borr=D[posX -1, posY]
        sust=D[posX -1, posY -1]
        #para elegir la operacion optima
        opMenosCoste = min(ins,borr,sust)
        if(ins == opMenosCoste):
            secuencia.append(('', y[posY - 1]))
            posY -= 1
        elif(borr == opMenosCoste):
            secuencia.append((x[posX - 1], ''))
            posX -= 1
        elif(sust == opMenosCoste): 
            secuencia.append((x[posX - 1], y[posY - 1]))
            posX -= 1
            posY -= 1
    #si se llega a una pared de la matriz
    while posX > 0:
        secuencia.append((x[posX - 1], ''))
        posY -= 1
    while posY > 0:  
        secuencia.append(('', y[posY - 1]))
        posY -= 1   
    #invertir lista y devolver las operaciones
    secuencia = secuencia[::-1]
    return D[lenX,lenY], secuencia

def levenshtein_reduccion(x, y, threshold=None):
    # completar versión con reducción coste espacial
    return 0 # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein(x, y, threshold):
    # completar versión reducción coste espacial y parada por threshold
    return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def levenshtein_cota_optimista(x, y, threshold):
    return 0 # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted_matriz(x, y, threshold=None):
    # completar versión Damerau-Levenstein restringida con matriz
    lenX, lenY = len(x), len(y)
    # COMPLETAR
    return D[lenX, lenY]

def damerau_restricted_edicion(x, y, threshold=None):
    # partiendo de damerau_restricted_matriz añadir recuperar
    # secuencia de operaciones de edición
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted(x, y, threshold=None):
    # versión con reducción coste espacial y parada por threshold
     return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_intermediate_matriz(x, y, threshold=None):
    #longitud cadenas x e y
    lenX, lenY = len(x), len(y)
    #matriz de 0 para resultado intermedios
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    for i in range(1, lenX + 1): # Rellena la primera fila
        #insercion (x - cadena vacia)
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1): # Para cada columna
        #insercion (y - cadena vacia)
        D[0][j] = D[0][j - 1] + 1 # Rellenas su vertical
        for i in range(1, lenX + 1): # Para cada fila
            D[i][j] = min(
                D[i - 1][j] + 1, #ins
                D[i][j - 1] + 1, #bor
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]), #sust
            )
            if (i > 1 and j > 1)\
                and (x[i - 2] == y[j - 1] and x[i - 1] == y[j - 2]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 2][j - 2] + 1
                )

            #Casos de transposicion nuevos
            # acb -> ba
            if (i > 2 and j > 1)\
                and (x[i - 3] == y[j - 1] and x[i - 1] == y[j - 2]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 3][j - 2] + 2
                )

            # ab -> bca
            if (i > 1 and j > 2)\
                and (x[i - 2] == y[j - 1] and x[i - 1] == y[j - 3]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 2][j - 3] + 2
                )
                
    return D[lenX, lenY]


def damerau_intermediate_edicion(x, y, threshold=None):
    # partiendo de matrix_intermediate_damerau añadir recuperar
    # secuencia de operaciones de edición
    # completar versión Damerau-Levenstein intermedia con matriz
    
    #longitud cadenas x e y
    lenX, lenY = len(x), len(y)
    #matriz de 0 para resultado intermedios
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    for i in range(1, lenX + 1): # Rellena la primera fila
        #insercion (x - cadena vacia)
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1): # Para cada columna
        #insercion (y - cadena vacia)
        D[0][j] = D[0][j - 1] + 1 # Rellenas su vertical
        for i in range(1, lenX + 1): # Para cada fila
            D[i][j] = min(
                D[i - 1][j] + 1, #ins
                D[i][j - 1] + 1, #ins
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]), #sust
            )
            if (i > 1 and j > 1)\
                and (x[i - 2] == y[j - 1] and x[i - 1] == y[j - 2]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 2][j - 2] + 1
                )

            #Casos de transposicion nuevos
            # acb -> ba
            if (i > 2 and j > 1)\
                and (x[i - 3] == y[j - 1] and x[i - 1] == y[j - 2]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 3][j - 2] + 2
                )

            # ab -> bca
            if (i > 1 and j > 2)\
                and (x[i - 2] == y[j - 1] and x[i - 1] == y[j - 3]):
                D[i][j] = min(
                    D[i][j],
                    D[i - 2][j - 3] + 2
                )
    #ultimas posiciones matriz           
    posX, posY = D.shape[0] - 1, D.shape[1] - 1
    secuencia = []
    while posX > 0 and posY > 0: #mientras haya elementos en la cadena
        ins = D[posX, posY - 1]
        borr = D[posX - 1, posY]
        sust = D[posX - 1, posY - 1]
        #ab -> ba
        if (posX > 1 and posY > 1)\
                and (x[posX - 2] == y[posY - 1] and x[posX - 1] == y[posY - 2]):
            int = D[posX - 2, posY - 2]
        else:
            int = float('inf')
        # acb->ba
        if (posX > 2 and posY > 1)\
                and (x[posX - 3] == y[posY - 1] and x[posX - 1] == y[posY - 2]):
            int3_2 = D[posX - 3][posY - 2]
        else:
            int3_2 = float('inf')
        #ab->bca
        if (posX > 1 and posY > 2)\
                and (x[posX - 2] == y[posY - 1] and x[posX - 1] == y[posY - 3]):
            int2_3 = D[posX - 2][posY - 3]
        else:
            int2_3 = float('inf')

        opMinCoste = min (ins,borr,sust,int,int3_2, int2_3)
        if(ins == opMinCoste):
            secuencia.append(('', y[posY - 1]))
            posY -= 1
        elif(borr == opMinCoste):
            secuencia.append((x[posX - 1], ''))
            posX -= 1
        elif(sust == opMinCoste): 
            secuencia.append((x[posX - 1], y[posY - 1]))
            posX -= 1
            posY -= 1
        if(int == opMinCoste):
            secuencia.append(('', y[posY - 1]))
            posX -= 2
            posY -= 2
        elif(int3_2 == opMinCoste):
            secuencia.append((x[posX - 1], ''))
            posX -= 3
            posY -= 2
        elif(int2_3 == opMinCoste): 
            secuencia.append((x[posX - 1], y[posY - 1]))
            posX -= 2
            posY -= 3
    #paredes    
    while posY > 0:
        secuencia.append(('', y[posY - 1]))
        posY -= 1
    while posX > 0:
        secuencia.append((x[posX - 1], ''))
        posX -= 1
    secuencia = secuencia[::-1]
    return D[lenX, lenY], secuencia
    
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

