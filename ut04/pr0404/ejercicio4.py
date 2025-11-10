asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}
print("****BIENVENIDO, ELIGE UNA DE LAS TRES OPCIONES DEL MENÚ****")
acabado = False
while(not acabado):
    opcionMenu = int(input("\n****MENÚ****\n"
                "1. Listar estudiantes matriculados en una asignatura.\n"
                "2. Matricular un estudiante en una asignatura.\n" 
                "3. Dar de baja un estudiante de una asignatura.\n" 
                "0. Salir\n"))
    match (opcionMenu):
        case 1:
            asignatura = input("\nEscribe el nombre de la asignatura de la cual deseas el listado de alumnos\n")
            print("\nListado de alumnos de la asignatura: "+asignatura)
            alumnosMatricula = {asignatura:asignaturas.get(i) for i in asignaturas.keys() if i == asignatura}
            print(alumnosMatricula)
        case 2:
            nombreAsignatura = input("\nEscribe el nombre de la asignatura en la que quieres matricular al alumno\n")
            nombreEstudiante = input("Escribe el nombre del estudiante\n")
            if nombreEstudiante not in nombreAsignatura:
                listaEstudiante = asignaturas.get(nombreAsignatura)
                listaEstudiante.append(nombreEstudiante)
                asignaturas.update({nombreAsignatura:listaEstudiante})
                print("\nAlumno/a matriculado/a correctamente\nLista de estudiantes actuales en la asignatura: "+nombreAsignatura)
                print(asignaturas.get(nombreAsignatura))        
        case 3:
            nombreAsignatura = input("\nEscribe el nombre de la asignatura en la que quieres dar de baja a un alumno\n")
            nombreEstudiante = input("Escribe el nombre del estudiante\n")
            if nombreEstudiante not in nombreAsignatura:
                listaEstudiante = asignaturas.get(nombreAsignatura)
                listaEstudiante.remove(nombreEstudiante)
                asignaturas.update({nombreAsignatura:listaEstudiante})
                print("\nAlumno/a dado/a de baja correctamente\nLista de estudiantes actuales en la asignatura: "+nombreAsignatura)
                print(asignaturas.get(nombreAsignatura))      
        case 0:
            acabado = True  