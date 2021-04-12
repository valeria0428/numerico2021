import numpy as np
import math


def f(x):
    return np.double(math.pow(x, 3)+4*math.pow(x, 2)-10)


def secante(x0,x1,tolerancia,niter):
    data_to_table = []
    mensajes = []
    fx0 = f(x0)

    if fx0 == 0:
        mensajes.append("x0 es raiz")
    else:
        fx1 = f(x1)
        contador = 0
        data_to_table.append([contador, x0, fx0])
        contador = contador + 1
        data_to_table.append([contador, x1, fx1])
        error = tolerancia + 1
        den = fx1-fx0
        while error > tolerancia and fx1 != 0 and den != 0 and contador < niter:
            x2 = x1 - ((fx1*(x1-x0))/den)
            error = abs((x2-x1))
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f(x1)
            den = fx1 - fx0
            contador = contador + 1
            data_to_table.append([contador, x1, fx1, error])
        if fx1 == 0:
            mensajes.append("{} es raiz".format(x1))
        elif error < tolerancia:
            mensajes.append(
                "x1 es aproximacion a una raiz con una tolerancia = {}".format(tolerancia))
        elif den == 0:
            mensajes.append("hay una posible raiz multiple")
        else:
            mensajes.append("fracaso en {} iteraciones".format(niter))
    
    response = {
        "result": data_to_table,
        "mensajes": mensajes
    }
    return response