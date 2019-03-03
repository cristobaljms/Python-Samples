def monedas(valor):
    listMonedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    dictMonedas = dict({2:0, 1:0, 0.5:0, 0.2:0, 0.1:0, 0.05:0, 0.02:0, 0.01:0})

    for moneda in listMonedas:
        while (moneda <= valor):
            valor = valor - moneda
            dictMonedas[moneda] += 1

    result = list()

    for moneda in listMonedas:
        if(dictMonedas[moneda] > 0):
            result.append((dictMonedas[moneda], moneda))
    return tuple(result)

print (monedas(7.48))
