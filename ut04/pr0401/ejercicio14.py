palabraNormal = input("introduce la palabra a analizar.\n")
array = []
for i in palabraNormal:
    array.append(i)

array.reverse()
palabra = ""
for j in array:
    palabra = palabra + j

if palabraNormal == palabra:
    estado = ""
else:
    estado = " no"
print(f'La palabra {palabraNormal}{estado} es un palíndromo')