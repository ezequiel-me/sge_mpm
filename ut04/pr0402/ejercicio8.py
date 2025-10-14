cadenaUno = input("Introduce la primera cadena:\n")
cadenaDos = input("Introduce la segunda cadena:\n")
arrayUno = []
for i in cadenaUno:
    arrayUno.append(i)

arrayDos = []
for j in cadenaDos:
    arrayDos.append(j)

resultado = "son"
if len(i) == len(j):
    for uno in cadenaUno:
        if uno not in cadenaDos:
            resultado = "no son"
    
    for dos in cadenaDos:
        if dos not in cadenaUno:
            resultado = "no son"

print(f'Las cadenas:\n{cadenaUno}\n{cadenaDos}\n{resultado} anagramas')