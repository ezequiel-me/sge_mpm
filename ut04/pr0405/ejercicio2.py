celsius = [0, 20, 37, 100]
resultadoTemperaturas = list(map(lambda temperatura: int(temperatura * 1.8 + 32), celsius))
print(resultadoTemperaturas)