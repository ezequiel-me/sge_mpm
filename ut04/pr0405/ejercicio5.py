from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]
numerosPares = list(filter(lambda num: num%2==0, numeros))
productoPares = reduce(lambda acumuluador, numero: numero*acumuluador, numerosPares, 1)
print(productoPares)