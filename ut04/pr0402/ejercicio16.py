def palabraMasLarga(cadena):
    mensaje = ""
    cadenaLista = max(cadena.split(" "))
    return cadenaLista
cadena = input("Introduce la cadena\n")
if len(cadena) > 0:
    print(palabraMasLarga(cadena))