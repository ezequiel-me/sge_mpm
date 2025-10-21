productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}
categoriaProductos = 0
productosTotalCategoria = {}
numeroProductos = 0
numCategorias = [i for i in productos.keys()]
print(f'Numero total de categorias:\n{len(numCategorias)}')
for j in productos:
    for b in productos.get(j):
        categoriaProductos += 1
        numeroProductos += 1
    print(f'Numero total de productos de la categoria {j}:\n{categoriaProductos}')
    categoriaProductos = 0
    
print(f'Cantidad total de productos en el diccionario:\n{numeroProductos}')