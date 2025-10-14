def contarPalabras(cadena):
    arrayCadenaSinEspacios = []

    for i in cadena:
        if i != " ":
            arrayCadenaSinEspacios.append(i)
    print(f'Número total de palabras (sin contar los espacios): {len(arrayCadenaSinEspacios)}')
    

cadena = input("Introduce la palabra para comprobar:\n")
contarPalabras(cadena)
