def filtrarEmple(empleados, canti):
    diccionario = {nombreEmpleado: cantidadSalario for nombreEmpleado, cantidadSalario in empleados.items() if cantidadSalario > canti}
    return diccionario


empleados = {
    "Luis": 125,
    "Carlos": 280,
    "Diego": 256,
    "Daniel": 265,
    "Ruben": 245,
    "Adrian":250
}

cantidad = 250
empleadosTrue = filtrarEmple(empleados, cantidad)

print(f'Empleados con mas de 250:\n{empleadosTrue}')