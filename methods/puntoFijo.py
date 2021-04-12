import math
import numpy as np
from tabulate import tabulate


def f(x):
    return np.double(x*math.exp(x)-math.pow(x, 2)-5*x - 3)


def g(x):
    return np.double((x*math.exp(x)-math.pow(x, 2)-3)/5)



def punto_fijo(tolerancia, xa, niter):
    data_to_table = []
    mensajes = []

    fx = f(xa)
    contador = 0
    error = tolerancia + 1
    data_to_table.append([contador, xa, fx])

    while fx != 0 and error > tolerancia and contador < niter:
        xn = g(xa)
        fx = f(xn)
        error = abs(xn - xa)
        xa = xn
        contador += 1
        data_to_table.append([contador, xa, fx, error])
    if fx == 0:
        mensajes.append("xa={} es una raiz".format(xa))
    elif error < tolerancia:
        mensajes.append("xa={} es una aproximación con una tolerancia {:.8}".format(
            xa, tolerancia))
    else:
        mensajes.append("El metodo fracaso en el numero de iteraciones")

    response = {
        "result": data_to_table,
        "mensajes": mensajes
    }
    return response


