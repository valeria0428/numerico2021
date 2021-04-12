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


def Eliminacion(A, b, n):
    Ab = FormaMatrizAumentada(A, b)
    for k in range(1, n):
        for i in range(k+1, n+1):
            multiplicador = Ab[i-1][k-1]/Ab[k-1][k-1]
            for j in range(k, n+2):
                Ab[i-1][j-1] = Ab[i-1][j-1] - multiplicador * Ab[k-1][j-1]
    x = SustitucionRegresiva(Ab, n)
    
    response = {
        "table": Ab,
        "X": x
    }
    return response
