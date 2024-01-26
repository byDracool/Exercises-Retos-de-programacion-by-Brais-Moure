# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import string
import random


def password_generator(length= 8, capital=False, numbers=False, symbols=False) -> str:
    password = ""
    password_possibilities = ""

    if length < 8:
        length= 8
    elif length > 16:
        length = 16

    password_possibilities += string.ascii_lowercase

    if capital:
        password_possibilities += string.ascii_uppercase
    if numbers:
        password_possibilities += string.digits
    if symbols:
        password_possibilities += string.punctuation

    for n in range(length + 1):
        password += (random.choice(password_possibilities))

    return print("Password: {}".format(password))


password_generator()
password_generator(length=16)
password_generator(length=1)
password_generator(length=22)
password_generator(length=12, capital=True)
password_generator(length=12, capital=True, numbers=True)
password_generator(length=12, capital=True, numbers=True, symbols=True)
password_generator(length=12, capital=True, symbols=True)


