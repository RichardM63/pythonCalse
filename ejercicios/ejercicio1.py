### Mini sistema de notas

sistema={
    'NombreInstituto': 'ColegioNG',
    'Cursos': ['python','Javascrip','java','php'],
    'Profesores': ['Profesor1', 'Profesor2'],
    'Estudiantes': {
        '7753': {
            'nombre': 'Juan',
            'apellido':'rodriguez',
            'curso y notas': {
                'python': []
                }
            },
        '7754': {
            'nombre': 'Julio',
            'apellido':'rodriguez',
            'curso y notas': {
                'python':[],
                'java': []}
            },
        '7755': {
            'nombre': 'Juan',
            'apellido':'rodriguez',
            'curso y notas': {
                'php': []
                }
            }
    },
    'cursoProfesor': {
        'python': [],
        'javascrip': [],
        'java': [],
        'php': []
    }
}
'''profesoresActuales = sistema['Profesores']
profesorPorAsignar = input('Que profesor es?: ')
if profesorPorAsignar in profesoresActuales :
    print('Exisate el profesor')
    print(sistema['Cursos'])
    CursosPorAsignar = input('Cual curso desea asignar al profesor: ')
    if CursosPorAsignar in sistema['Cursos']:
        CursosActuales=sistema['cursoProfesor'][CursosPorAsignar]
        CursosActuales.append(profesorPorAsignar) 
        sistema['cursoProfesor'][CursosPorAsignar] = CursosActuales
    else:
        print('No existe el curso')
else:
    print('No exite el profesor. desea agregarlo?')
    profesoresActuales.append(profesorPorAsignar)
    sistema['Profesores'] =profesoresActuales

print(sistema)'''

CodigoDado= input('Ingrese el codigo del Estudiante: ')
if CodigoDado in sistema['Estudiantes']:
    nombre = sistema['Estudiantes'][CodigoDado]['curso y notas']
    print('El estudiante existe en el sistema')
    print('Estos cursos esta llevando el estudiante', sistema['Estudiantes'][CodigoDado]['nombre'],':')
    print(nombre.keys())
    Cursonota= input('Ingrese el nombre del curso en cuestion: ')
    Cursonota = Cursonota.lower()
    if Cursonota in nombre:
        print('El curso existe en el sistema')
        Nota=int(input('Ingrese la nota para el estudiante: '))
        if Nota >=0 and Nota <= 20:
            Resultado = sistema['Estudiantes'][CodigoDado]['curso y notas'][Cursonota]
            Resultado.append(Nota)
            sistema['Estudiantes'][CodigoDado]['curso y notas'][Cursonota]= Resultado
        else:
            print('Nota invalida')
    else:
        print('Curso invalido')
else:
    print('El estudiante no existe en el sistema') 

print(sistema['Estudiantes'][CodigoDado])  