# /*
#  * Crea un generador de números pseudoaleatorios entre 0 y 100.
#  * - No puedes usar ninguna función "random" (o semejante) del
#  *   lenguaje de programación seleccionado.
#  *
#  * Es más complicado de lo que parece...
#  */

import datetime
import time


def number_generator():
    number = ""
    index = 0
    timer = str(time.monotonic())
    number += timer[-1]
    timer = str(time.perf_counter())
    number += timer[-1]
    return number


print(number_generator())


