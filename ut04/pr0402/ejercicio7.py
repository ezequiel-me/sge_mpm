cadena = input("Introduce la cadena\n")
numero = int(input("Introduce el número de veces que quieres rotar la cadena\n"))
letrasCadena = ""
nuevaCadena = cadena[numero::] +  cadena[:numero:]
print(nuevaCadena)