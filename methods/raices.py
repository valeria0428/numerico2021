import numpy as np
import math


def f(x):
    return np.double(math.pow(x, 4)-18*math.pow(x, 2)+81)


def df(x):
    return np.double(4*math.pow(x, 3)-36*x)


def ddf(x):
    return np.double(12*math.pow(x, 2)-36)

def raizMultiples(x0, tolerancia, niter):
    data_to_table = []
    message = []

    fx = f(x0)
    dfx = df(x0)
    ddfx = ddf(x0)

    contador = 0
    data_to_table.append([contador, x0, fx, dfx, ddfx])
    error = tolerancia + 1
    den = math.pow(dfx, 2) - (fx*ddfx)

    while error > tolerancia and fx != 0 and den != 0 and contador < niter:
        x1 = x0 - ((fx*dfx)/den)
        error = abs((x1-x0))
        fx = f(x1)
        dfx = df(x1)
        ddfx = ddf(x1)
        den = math.pow(dfx, 2) - (fx*ddfx)
        contador = contador + 1
        x0 = x1
        data_to_table.append([contador, x0, fx, dfx, ddfx, error])

    if fx == 0:
        message.append("{} es raiz".format(x1))
    elif error < tolerancia:
        message.append(
            "{} es aproximacion a una raiz con una tolerancia = {}".format(x0, tolerancia))
    elif den == 0:
        message.append("denominador se hace cero")
    else:
        message.append("fracaso en {} iteraciones".format(niter))

    
    response = {
        "result": data_to_table,
        "messages": message
    }

    return response
