cadena = input("Introduce la palabra a comprobar\n")
cadenaInvertida = cadena[::-1]
resultado = "no es"
resultado = "es" if cadena == cadenaInvertida else "no es"
print(f'La palabra {cadena} {resultado} un palíndromo')