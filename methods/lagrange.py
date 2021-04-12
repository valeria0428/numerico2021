import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math


def lagrange(valor, x, y):
    mensajes = []
    pol = ""
    G = Function('G')
    F = Function('F')
    n = len(x)
    resultado = 0
    for k in range(n):
        mult = 1
        termino = "("
        for i in range(n):
            if i != k:
                mult *= (valor - x[i])/(x[k] - x[i])
                termino += "(x-"+str(x[i])+")"
        termino += ")/("
        for i in range(n):
            if i != k:
                termino += "(" + str(x[k]) + "-" + str(x[i]) + ")"
        termino += ")"
        termino = termino.replace(")(", ") * (")
        F = parse_expr(termino)
        mensajes.append("\n L" + str(k) + "(x) = " +
              termino.replace("((", "(").replace("))", ")") + " = " + str(expand(F)))
        toReplace = "L" + str(k) + "(x) = "
        pol += "(" + str(expand(F)) + ")*" + str(y[k])
        if k != (n-1):
            pol += " + "
        resultado += mult*y[k]
    G = str(expand(pol))
    mensajes.append("Polinomio interpolante")
    mensajes.append(G)
    mensajes.append("Resultado")
    mensajes.append("f(", valor, ") = ", resultado)
    response = {
        "mensajes": mensajes
    }
    return response
