from random import *
numeroGenerado = randint(0,100)
numeroInsertado = int(input("Se ha generado un numero del 0 al 100. Intenta adivinarlo. Suerte!\n"))
while numeroInsertado != numeroGenerado:
   if numeroInsertado < numeroGenerado:
       caso = "más alto"
   elif numeroInsertado > numeroGenerado:
       caso = "más bajo"
   numeroInsertado = int(input("Has fallado. El numero generado es " + caso + "\n"))
print("¡Felicidades, el número " + str(numeroInsertado) + " es el número generado!")