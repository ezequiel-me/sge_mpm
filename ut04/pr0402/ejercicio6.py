cadena = input("Introduce la cadena:\n")
resultado = ""
for i in cadena:
    if i.islower():
        resultado =  resultado + i.upper()
    elif i.isupper():
        resultado = resultado + i.lower()
    
print(f'La cadena cambiando las letras mayúsculas por minúsculas y viceversa. Quedaría asi:\n{resultado}')