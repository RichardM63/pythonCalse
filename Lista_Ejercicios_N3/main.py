if __name__ == '__main__':
    print('Archivo Principal, continuar con el resto de ejercicios')

####################################################


import Ejercicio_n5 as lab
import os
try:
    lab.Suma(2)

    lab.division(1,6)
except Exception as e:
    print('Hay un error')
    print(e)
else:
    print(os.getcwd())
finally:
    print('proceso terminado')
