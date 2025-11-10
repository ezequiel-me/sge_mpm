palabras = ["sol", "luna", "estrella", "cielo", "mar"]
palabrasClavesLongitud = {len(i) for i in palabras}
diccionario = {}
def buscarPalabras(cantidadLetras):
    palabrasEncontradas = [i for i in palabras if len(i) == cantidadLetras]
    diccionario.update({cantidadLetras : palabrasEncontradas})
    
palabrasFiltradas = list(map(buscarPalabras ,palabrasClavesLongitud))
print(diccionario)