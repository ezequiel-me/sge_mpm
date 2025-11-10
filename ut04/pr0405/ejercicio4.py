palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
palabrasLargas = list(filter(lambda counter: len(counter) >  5, palabras))
palabrasMayus = list(map(lambda palabra: palabra.upper(), palabrasLargas))
print(palabrasMayus)