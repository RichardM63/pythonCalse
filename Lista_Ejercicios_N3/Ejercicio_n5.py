
def Suma(n):
    p = 0
    t=0
    while p < n :
        p = p +1
        t = t + p
    print('La suma de los numeros es de: %d' %(t))

Suma(5)

def division(n1,n2):
    print('El resultado de la division es de: ', n1/n2)
    
division(4,2)

#####################################################
import sys

print('Se esta ejecutando el archivo:', sys.argv)