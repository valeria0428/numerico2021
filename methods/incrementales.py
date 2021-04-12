import math
from tabulate import tabulate
import numpy as np


def f(x):
    return np.double(math.exp(3*x-12)+x*math.cos(3*x)-math.pow(x, 2)+4)

def incrementales(x0,delta,niter):
    data_to_table = []
    mensajes = []
    fx0 = f(x0)

    if fx0 == 0:
        mensajes.append("X0 es una raiz")
    else:
        x1 = x0 + delta
        contador = 1
        fx1 = f(x1)
        data_to_table.append([x1, fx1])
        while fx0 * fx1 > 0 and contador < niter:
            x0 = x1
            fx0 = fx1
            x1 = x0 + delta
            fx1 = f(x1)
            contador += 1
            data_to_table.append([x1, fx1])
        if fx1 == 0:
            mensajes.append("x1 es una raiz")
        elif fx0 * fx1 < 0:
            mensajes.append("Hay una raiz entre x0={} y x1={}".format(x0, x1))
        else:
            mensajes.append("Fracaso en niter iteraciones")
            
    response = {
        "result": data_to_table,
        "mensaje": mensajes
    }
    return response