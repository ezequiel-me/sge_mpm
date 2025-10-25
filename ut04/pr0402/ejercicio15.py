def compararCadenas(cadenaUno, cadenaDos):
    sumaCadenaUno = 0
    sumaCadenaDos = 0
    mensaje = "El valor de la primera cadena es mayor"
    for i in cadenaUno:
        sumaCadenaUno += ord(i)
    for j in cadenaDos:
        sumaCadenaDos += ord(j)
    if(sumaCadenaDos > sumaCadenaUno):
        mensaje = "El valor de la segunda cadena es mayor"
    elif sumaCadenaDos == sumaCadenaUno:
        mensaje = "Las dos cadenas tienen el mismo valor"
    return mensaje

cadena = input("Introduce la primera cadena\n")
cadena2 = input("Introduce la segunda cadena\n")
if len(cadena) > 0 and len(cadena2) > 0:
    print(compararCadenas(cadena, cadena2))