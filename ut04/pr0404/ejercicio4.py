asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}
bienvenida = print("BIENVENIDO AL PROGRAMA, ELIGE UNA DE LAS OPCIONES DISPONIBLES")
opcion = 4
while(opcion != 0):
    opcion = int(input("1. Listar estudiantes matriculados en una asignatura\n2. Matricular un estudiante en una asignatura\n3. Dar de baja un estudiante de una asignatura\n0. Salir del programa\n\n"))
    match opcion:
        case 1:
            nombreAsignatura = input("Introduce el nombre de la asignatura\n")
            if nombreAsignatura in asignaturas:
                print(f'Estudiantes de la asignatura {nombreAsignatura}')
                for i in asignaturas.get(nombreAsignatura):
                    print(i)
            else:
                print(f'No existe ninguna asignatura con el nombre: "{nombreAsignatura}", inténtalo de nuevo\n')
        case 2:
            nombreEstudiante = input("Introduce el nombre del estudiante\n")
            asignatura = input("Introduce el nombre de la asignatura\n")
            if nombreEstudiante in asignaturas:
                print(f'El estudiante con el nombre: {nombreEstudiante} ya está matriculado en la asignatura: {asignatura}')
            elif asignatura not in asignaturas:
                print(f'La asignatura: "{asignatura}" no se encuentra en el diccionario, inténtalo de nuevo\n')
            elif len(nombreEstudiante) > 0 and len(asignatura) > 0:
                for a,alumnos in asignaturas.items():
                    if a == asignatura:
                        alumnos.append(nombreEstudiante)
                        print("Alumno agregado correctamente")
                        break
            else:
                print(f'Error: debes proporcionar un nombre y una asignatura para realizar el proceso de matriculación\n')
            
