numero = int(input("Introduce el numero\n"))
print("El programa empezará a imprmir los pares e impares entre los numeros comprendidos de 1 a " + str(numero))
for i in range(1, numero+1):
    division = float(i % 2)
    if division == 0.0:
        numerosEstado = "par"
    else:
        numerosEstado = "impar"
    print("El numero: " + str(i) + " es " + numerosEstado)