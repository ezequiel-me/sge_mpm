
palabraNormal = input("introduce la palabra a analizar.\n")
array = []
for i in palabraNormal:
    array.append(i)

array.reverse()
palabra = ""
for j in array:
    palabra = palabra + j

print(f'La palabra {palabraNormal} dada la vuelta es {palabra}')