import math
import numpy as np


def f(x):
    # Función de prueba
    return np.double(math.pow(x,3)-(5.01*math.pow(x,2))-(2.5956*x)+26.5424)

def biseccion(xi, xs, tolerancia, niter):
    data_to_table = []
    mensajes = []

    fxi = f(xi)
    fxs = f(xs)

    if fxi == 0:
        mensajes.append("xi es una raiz")
    elif fxi*fxs < 0:
        xm = np.double((xi + xs)/2)
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
            xm = np.double((xi + xs) / 2)
            fxm = f(xm)
            error = abs(xm - xaux)  # Este es el error absoluto
            contador += 1
            data_to_table.append([contador, xi, xs, xm, fxm, error])
        if fxm == 0:
            mensajes.append("xm={} es una raiz".format(xm))
        elif error < tolerancia:
            mensajes.append("xm={} es aproximación a una raiz con una tolerancia {}".format(
                xm, tolerancia))
        else:
            mensajes.append("El metodo fracaso")
    else:
        mensajes.append("El intervalo es inadecuado")

    response = {
        "result": data_to_table,
        "mensajes": mensajes
    }

    return response
