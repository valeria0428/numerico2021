import numpy as np
import math


def SustitucionRegresiva(Ab, n):
    x = np.zeros((n), dtype=np.double)
    x[n-1] = Ab[n-1][n]/Ab[n-1][n-1]
    for i in range(n-1, 0, -1):
        sum = 0
        for p in range(i+1, n+1):
            sum = sum + Ab[i-1][p-1]*x[p-1]
        x[i-1] = (Ab[i-1][n]-sum)/Ab[i-1][i-1]
    return x


def FormaMatrizAumentada(A, b):
    n = len(A)
    Ab = np.zeros((n, n+1), dtype=np.double)
    for i in range(n):
        for k in range(n):
            Ab[i][k] = A[i][k]

    for i in range(n):
        Ab[i][n] = b[i]

    return Ab


def intercanbioFila(Ab, filaMayor, k):
    aux = np.copy(Ab[filaMayor-1])
    aux2 = np.copy(Ab[k-1])
    Ab[filaMayor-1] = aux2
    Ab[k-1] = aux
    return Ab

def intercabioColumnas(Ab,columnaMayor,k):
    aux = np.copy(Ab[:,columnaMayor-1])
    aux2 = np.copy(Ab[:,k-1])
    Ab[:,columnaMayor-1] = aux2
    Ab[:,k-1] = aux
    return Ab

def intercabioMarcas(marcas,columnaMayor,k):
    aux = marcas[columnaMayor-1]
    aux2 = marcas[k-1]
    marcas[columnaMayor-1] = aux2
    marcas[k-1] = aux
    return marcas


def pivoteoTotal(Ab, n, k, marcas):
    mayor = 0
    filaMayor = k
    columnaMayor = k
    for r in range(k, n+1):
        for s in range(k, n+1):
            if abs(Ab[r-1][s-1]) > mayor:
                mayor = abs(Ab[r-1][s-1])
                filaMayor = r
                columnaMayor = s
    if mayor == 0:
        return "el sistema no tienen solucion unica"
    else:
        if filaMayor != k:
            Ab = intercanbioFila(Ab,filaMayor,k)
        if columnaMayor != k:
            Ab = intercabioColumnas(Ab,columnaMayor,k)
            marcas = intercabioMarcas(marcas,columnaMayor,k)
        return Ab, marcas
    

def Eliminacion(A, b, n):
    marcas = []
    for m in range(1,n+1):
        marcas.append(m)

    Ab = FormaMatrizAumentada(A, b)
    
    for k in range(1, n):
        Ab, marcas = pivoteoTotal(Ab, n, k, marcas)
        for i in range(k+1, n+1):
            multiplicador = Ab[i-1][k-1]/Ab[k-1][k-1]
            for j in range(k, n+2):
                Ab[i-1][j-1] = Ab[i-1][j-1] - multiplicador * Ab[k-1][j-1]

    x = SustitucionRegresiva(Ab,n)
    response = {
        "table": Ab,
        "X": x,
        "marcas": marcas
    }
    return response