def eliminarRepetidos(cadena):
    resultado = ""
    for i in cadena:
        if i not in resultado:
            resultado = resultado + i

    print(resultado)

cadena = input("Introduce la cadena:\n")
eliminarRepetidos(cadena)
