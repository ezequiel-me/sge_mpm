n = int(input("Introduce un número. Debe ser impar\n"))

nDivision= float(n % 2)

while nDivision == 0:

    n = int(input("Tu número debe ser impar, inténtalo de nuevo\n"))

    nDivision= float(n % 2)

count = 1

i = 1

while n > 0:

    numB = i-1

    opr = n - i

    if opr == numB:

        print(" " * numB + "*" * count)

        n = n - 2

        i = 1

        count = count + 2

    else:

         i = i + 1
 