frase = input("Introduce la frase\n")
listaFrase = frase.split(" ")
diccionario = {}
for i in listaFrase:
    diccionario.update({i:frase.count(i)})
print(diccionario)