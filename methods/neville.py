import numpy as np
import math



def Neville(x, X, Y):
    n = len(X)
    Q = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        Q[i][0] = Y[i]

    for i in range(1, n):

        for j in range(i, n):
            Q[j][i] = ((x-X[j-i])*Q[j][i-1]-(x-X[j])*Q[j-1][i-1])/(X[j]-X[j-i])
    
    response = {
        "result": Q
    }
    return response
