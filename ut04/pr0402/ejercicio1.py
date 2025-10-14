vocales = ['a','e','i','o','u', 'á','é','í','ó','ú']
palabra = input("Introduce la cadena de texto\n")
palabra.lower()

contadorVocales = 0
contadorConsonantes = 0
esVocal = False
for i in palabra:
    for j in vocales:
        if i == j:
            esVocal = True
            break
    if esVocal:
        contadorVocales = contadorVocales + 1
        esVocal = False
    elif i != " " and esVocal == False:
        contadorConsonantes = contadorConsonantes + 1

print(f'La cantidad de consonantes en la cadena de texto es {contadorConsonantes} y la cantidad de vocales son {contadorVocales}')