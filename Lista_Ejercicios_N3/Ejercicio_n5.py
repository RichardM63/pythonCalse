
import Lista_Ejercicios_N3.Ejercicio_n1 as lab
import os
try:
    lab.Suma(5)

    lab.division(4,2)
except Exception as e:
    print('Hay un error')
    print(e)
else:
    print(os.getcwd())
finally:
    print('proceso terminado')