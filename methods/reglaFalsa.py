import math
import numpy as np
from tabulate import tabulate


def f(x):
    return np.double(math.cos(7*x-8)*math.exp(-math.pow(x, 2)+4)+math.log(math.pow(x, 4) + 3)
                     - x - 15)

def reglaFalsa(xi, xs, tolerancia, niter):
    data_to_table = []
    message = []

    fxi = f(xi)
    fxs = f(xs)

    if fxi == 0:
        message.append("xi es una raiz")
    elif fxi*fxs < 0:
        xm = np.double(xi - (f(xi) * (xs - xi)) / (f(xs) - f(xi)))
        fxm = f(xm)
        contador = 1
        error = tolerancia + 1

        data_to_table.append([contador, xi, xs, xm, fxm, error])

        while error > tolerancia and fxm != 0 and contador < niter:
            if fxi*fxm < 0:
                xs = xm
                fxs = fxm
            else:
                xi = xm
                fxi = fxm
            xaux = xm
            xm = np.double(xi - (f(xi) * (xs - xi)) / (f(xs) - f(xi)))
            fxm = f(xm)
            error = abs(xm - xaux)  # Este es el error absoluto
            contador += 1
            data_to_table.append([contador, xi, xs, xm, fxm, error])
        if fxm == 0:
            message.append("xm={} es una raiz".format(xm))
        elif error < tolerancia:
            message.append("xm={} es aproximación a una raiz con una tolerancia {}".format(
                xm, tolerancia))
        else:
            message.append("El metodo fracaso")
    else:
        message.append("El intervalo es inadecuado")
    print(tabulate(data_to_table, headers=[
          "N", "Xi", "Xs", "Xm", "f(Xm)", "error"]))

    response = {
        "result": data_to_table,
        "message": message
    }

    return response
