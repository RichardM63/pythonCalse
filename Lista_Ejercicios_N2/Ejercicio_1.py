#Pregunta N°1
print('Menú Iterativo')
print('Ingresa[1] si quieres dibujar un cuadrado en la consola')
print('Ingresa[2] si quieres realizar una lista de numeros e identificar los numeros multiplos de 2')
print('Ingresa[3] si quieres ver una lista de nombres y edades que impriman los que son mayores de edad')
a = int(input('Ingresar la opcion correspondiente: '))
while a >3 and a<1:
    print('Ingresar una opcion correcta')
    input('Ingresar la opcion correspondiente: ')

if a == 1 :
    for a in range (1,4):
        print("*****")
elif a==2:
    numeroIteracional=int(input("Ingresar numeros a iterar: "))
    numeros = list()

    for i in range(1,numeroIteracional+1):
        if i % 2 == 0:
            print('El numero %d es multiplo de 2' %(i)) 
    numeros.append(i)
    print(numeros)
elif a ==3:
    nombre= ['Julio','Daniel','Pepe','Oscar','David']
    edad= [12,25,40,17,32]
    Lista= [nombre,edad]
    print(Lista)
    p = 0
    while p <= 4:
        if edad[p] >= 18 :
            print("%s es mayor de edad teniendo %d años" %(Lista[0][p],Lista[1][p]))
        p = p + 1
    b= int(input('¿Quieres hacer tu propia lista? Ingresar[1] si deseas crear una lista '))
    if b == 1:
        nombre1= []
        edad1=[]
        c = int(input('Ingresar las capacidad de la lista: '))
        p=0
        while p < c:
            AgregarNombre=input('Ingresar el nombre: ')
            nombre1.append(AgregarNombre)
            nombre1=nombre1
            AgregarEdad=int(input('Ingresar la edad: '))
            edad1.append(AgregarEdad)
            edad1=edad1
            p = p + 1
        lista1=[nombre1,edad1]
        print(lista1.items())
        p = 0        
        while p < c:
            if edad1[p] >= 18 :
                print("%s es mayor de edad teniendo %d años" %(lista1[0][p],lista1[1][p]))
            p = p + 1
        
