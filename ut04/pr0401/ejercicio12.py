numero = int(input("Ingresa el numero que quieres saber si es primo o no\n"))

contador = 0
for i in range(1,numero+1):
   if numero % i != 0:
       contador = contador + 1
salida = "Tu numero: " + str(numero) + " no es primo\n"  
if contador == 2:
   salida = "Tu numero: " + str(numero) + " es primo\n"
print(salida)