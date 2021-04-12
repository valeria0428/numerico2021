import numpy as np
import math


def f(x):
    # return np.double(math.sin(x + 3) - math.log(x + 1) + math.pow(x, 2) - 3)
    return np.double(-math.pow(3, -math.pow(x, 2)+1)+0.06*math.pow(x, 2)+2.5)


def df(x):
    # return np.double(math.cos(x + 3) - (1 / (x + 1)) + 2 * x)
    return np.double(math.pow(3, -math.pow(x, 2)+1)-0.06*math.pow(x, 2)-2.5)

def newton(x0,tolerancia,niter):
    data_to_table = []
    mensajes = []
    fx = f(x0)
    dfx = df(x0)
    contador = 0
    error = tolerancia + 1
    data_to_table.append([contador, x0, fx, dfx, error])


    while error > tolerancia and fx != 0 and dfx != 0 and contador < niter:
        x1 = x0 - (fx / dfx)
        fx = f(x1)
        dfx = df(x1)
        error = abs(x1 - x0)
        x0 = x1
        contador += 1
        data_to_table.append([contador, x0, fx, dfx, error])

    if fx == 0:
        mensajes.append("x0={} es una raiz".format(x0))
    elif error < tolerancia:
        mensajes.append("x1={} es una proximación a una raiz con una tolerancia={}".format(
            x1, tolerancia))
    elif dfx == 0:
        mensajes.append("x1={} es una posible raiz multiple".format(x1))
    else:
        mensajes.append("Fracaso en niter={} iteraciones".format(niter))

    
    response = {
        "result": data_to_table,
        "mensajes": mensajes
    }
    return response