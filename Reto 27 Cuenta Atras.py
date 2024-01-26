# /*
#  * Crea una función que reciba dos parámetros para crear una cuenta atrás.
#  * - El primero, representa el número en el que comienza la cuenta.
#  * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#  * - Sólo se aceptan números enteros positivos.
#  * - El programa finaliza al llegar a cero.
#  * - Debes imprimir cada número de la cuenta atrás.
#  */

import time


def timer(start_number, seconds):
    if type(start_number) == int and type(seconds) == int:
        while start_number > 0:
            print(start_number)
            start_number -= 1
            time.sleep(seconds)
        else:
            print("fin del temporizador")
            exit()
    else:
        print("Los numeros introducidos son incorrectos")


timer(20, 2)


