numMayor = 1
numMenor = 0
arrayN = [5]
for a in range(0,5):
   numero = int(input("Introduce el numero " + str(a+1) + "\n"))
   arrayN.append(numero)
arrayN.sort()
tamano = len(arrayN)
numMenor = min(arrayN)
numMayor = max(arrayN)
print("EL NUMERO MAYOR ES " + str(numMayor) + " Y EL MENOR ES " + str(numMenor))