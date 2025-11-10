from functools import reduce
numeros = [1, 2, 3, 4, 5]
numerosSuma = reduce(lambda acc, numero: acc+numero, numeros, 0)
print(numerosSuma)