import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

def newton(n, x, y):
    
    j=0
    temp=0
    tabla = np.zeros((n+1,n+1))

    for i in range(n):
        tabla[i][0] = x[i]
        tabla[i][1] = y[i]

    res = polinomio_newton(tabla,n).tolist()
    ##print (res)
    for i in range(len(res)):
        res[i].pop(0)
    res.pop()
    return np.array(res).tolist()


def polinomio_newton(tabla,n):
    data_to_table = []
    mensajes = []
    polinomio = "P(X) = " + str(tabla[0][1])
    F = Function('F')
    for j in range(2,n+1):
        for i in range(j-1,n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1])/(tabla[i][0] - tabla[i-j+1][0])
            if(i==j-1):
                polinomio += " + " + str(tabla[i][j])
                for i in range(0,i):
                    polinomio += "(x - " + str(tabla[i][0]) + ")"

    F = parse_expr(polinomio.replace("P(X) = ","").replace("(","*("))
    mensajes.append("\nPolinomio interpolante \n" + polinomio)
    data_to_table.append(tabla)
    response = {
        "result": data_to_table,
        "mensajes": mensajes
    }
    return response