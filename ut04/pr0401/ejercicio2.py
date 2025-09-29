numN = int(input("Introduce el primer numero\n"))
numK = int(input("Introduce el segundo numero\n"))
for a in range(1, numK+1):
    resultado = numN * a
    print(str(numN) + " * " + str(a) + " = " + str(resultado))