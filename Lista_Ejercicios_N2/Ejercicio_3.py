#Pregunta N°3
print('Introduce 2 valores')
a = int(input('Ingresa el primer valor: '))
b = int(input('Ingresa el segundo valor: '))

if a > b:
    print('El numero %d es mayor que el valor %d' %(a,b))
elif a < b:
    print('El numero %d es mayor que el valor %d' %(b,a))
else:
    print('Los numeros son iguales')