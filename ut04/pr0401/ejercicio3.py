numN = int(input("Introduce el numero\n"))
salida = True
while salida:
    if numN > 0  & numN % 2 == 0:
        numB = int(input("Tu numero es par, vuelve a introducir otro numero\n"))
    elif numN > 0 & numN  % 2 != 0 :
       salida = False 

piramide = ""
for a in range(1, numN, 2):
    piramide += "*"
    if a % 2 != 0:
        print(piramide)