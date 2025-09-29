numeroValido = 4
notFound = True
print("Introduce números hasta encontrar el válido")

while (notFound):
    numUser = int(input())
    if numUser == numeroValido:
        notFound = False
        print("Correcto, lo has encontrado el numero es ")
        print(numUser)
   
