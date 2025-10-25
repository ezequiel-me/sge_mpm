cadena = input("Introduce la cadena:\n")

resultado = ""

for c in cadena:
    if c.isalnum() or c == ' ':
        resultado += c
print(f'La cadena sin los caracteres alfanuméricos quedaría de la siguiente forma:\n{resultado}')