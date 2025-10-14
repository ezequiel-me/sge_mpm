cadena = input("Introduce la cadena:\n")

cadena = cadena.title().replace(' ',"").replace("-","")
cadena = cadena[0].lower() + cadena[1:]

print(f'La cadena convertida a camelCase quedaría de la siguiente forma\n{cadena}')
