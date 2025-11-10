lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

listaConjunto = list(filter(lambda dataLista2: dataLista2 in lista1, lista2))
print(listaConjunto)