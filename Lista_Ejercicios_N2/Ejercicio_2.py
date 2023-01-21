#Pregunta N°2
Bibliteca= {
    'Libros': {
      'Categorias': {
        'aventuras':{
            'codigo de libro': {
                '100000': {
                    'nombre libro': ['La ciudad de las mentiras'],
                    'nombre del autor/es': ['Lian Tanner'],
                    'estado del libro': ['Disponible']
                },
                '100001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': []
                }
            }
        },
        'ciencia ficcion':{
            'codigo de libro': {
                '150000': {
                    'nombre libro': ['Cronicas Marcianas'],
                    'nombre del autor/es': ['Ray Bradbury'],
                    'estado del libro': ['Disponible']
                },
                '150001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': []
                }
            }
        },
        'cuentos de hadas':{
            'codigo de libro': {
                '200000': {
                    'nombre libro': ['Historias del Mar'],
                    'nombre del autor/es': ['Alejandra'],
                    'estado del libro': ['Disponible']
                },
                '200001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': []  
                }
            }
        },
        'ngotica':{
            'codigo de libro': {
                '250000': {
                    'nombre libro': ['Dracula'],
                    'nombre del autor/es': ['Bram Stoker'],
                    'estado del libro': ['Disponible']
                },
                '250001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': [] 
                }
            }
        },
        'npoliciaca':{
            'codigo de libro': {
                '300000': {
                    'nombre libro': ['Esperando al diluvio'],
                    'nombre del autor/es': ['Dolores Redondo'],
                    'estado del libro': ['Disponible']
                },
                '300001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': [] 
                }
            }
        },
        'romance paranormal':{
            'codigo de libro': {
                '350000': {
                    'nombre libro': ['Amante oscuro'],
                    'nombre del autor/es': ['Jessica Bird'],
                    'estado del libro': ['Disponible']
                },
                '350001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': []
                }
            }
        },
        'ndistopica':{
            'codigo de libro': {
                '40000': {
                    'nombre libro': ['1984'],
                    'nombre del autor/es': ['George Orwell'],
                    'estado del libro': ['Disponible']
                },
                '40001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': []
                }
            }
        },
        'nfantastica': {
            'codigo de libro': {
                '450000': {
                    'nombre libro': ['El nombre del viento'],
                    'nombre del autor/es': ['Patrick Rothfuss'],
                    'estado del libro': ['Disponible']
                },
                '450001': {
                    'nombre libro': [],
                    'nombre del autor/es': [],
                    'estado del libro': []
                }
            }
        }
      }
    },
    'Usuarios': {
        'Codigo_Usuario': {
            '1': {
                'nombre': ['Juan'],
                'apellido': ['Rodriguez'],
                'dni': ['72865423'],
                'posesion libro': ['no']
            }
        }
    }
    }

a=int(input('¿Quiere hacer algun cambio en el estado de un libro? Elegir[1] si : '))

if a == 1:
    Categoria=input('Ingresar la categoria del libro: ')
    Categoria = Categoria.lower()

    if Categoria in Bibliteca['Libros']['Categorias']:
        print('La categoria existe en el sistema')
        libro=input('Ingresar el codigo del libro: ')

        if libro in Bibliteca['Libros']['Categorias'][Categoria]['codigo de libro']:
            print('El codigo existe en el sistema')
            print('¿A que estado quiere cambiar el libro:')
            estado=int(input('Ingresar[1] Disponible, Ingresar[2] Prestado: '))

            if estado == 1:
                usuario=input('Ingresar el codigo del cliente: ')

                if usuario in Bibliteca['Usuarios']['Codigo_Usuario']:
                    print('Codigo de usuario valido')
                    Bibliteca['Usuarios']['Codigo_Usuario'][usuario]['posesion libro']='no'
                    Bibliteca['Libros']['Categorias'][Categoria]['codigo de libro'][libro]['estado del libro']='Disponible'
                    print(['Usuarios']['Codigo_Usuario'][usuario])
                    print(Bibliteca['Libros']['Categorias'][Categoria]['codigo de libro'][libro])
                else:
                    print('Usuario Invalido')
            elif estado == 2:
                usuario=input('Ingresar el codigo del cliente: ')

                if usuario in Bibliteca['Usuarios']['Codigo_Usuario']:
                    print('Codigo de usuario valido')
                    Bibliteca['Usuarios']['Codigo_Usuario'][usuario]['posesion libro']='si'
                    Bibliteca['Libros']['Categorias'][Categoria]['codigo de libro'][libro]['estado del libro']='Prestado'
                    
                    print(Bibliteca['Usuarios']['Codigo_Usuario'][usuario])
                    print(Bibliteca['Libros']['Categorias'][Categoria]['codigo de libro'][libro])
                else:
                    print('Usuario Invalido')
        else:
            print('El codigo no existe en el sistema')
    else:
        print('La categoria no existe en el sistema')
