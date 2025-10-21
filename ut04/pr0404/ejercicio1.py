diccionario = {
    "Manzana" : 0.10,
    "Mandarina": 0.20,
    "Naranja": 0.30,
    "Kiwi": 0.40,
    "Cereza": 0.50,
    "Fresa": 0.60,
    "Uva": 0.70,
    "Banana": 0.80,
    "Coco": 0.90,
    "Peras": 1.00,
}
fruta = input("Introduce el nombre de la fruta para saber su precio\n")
if fruta in diccionario:
    print(f'El precio de {fruta} son {diccionario.get(fruta)}')
else:
    print(f'No existe ninguna fruta con el nombre {fruta} en el diccionario')