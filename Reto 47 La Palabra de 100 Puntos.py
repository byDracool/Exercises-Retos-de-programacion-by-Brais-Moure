# /*
#  * La última semana de 2021 comenzamos la actividad de retos de programación,
#  * con la intención de resolver un ejercicio cada semana para mejorar
#  * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
#  *
#  * Crea un programa que calcule los puntos de una palabra.
#  * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#  *   español de 27 letras, la A vale 1 y la Z 27.
#  * - El programa muestra el valor de los puntos de cada palabra introducida.
#  * - El programa finaliza si logras introducir una palabra de 100 puntos.
#  * - Puedes usar la terminal para interactuar con el usuario y solicitarle
#  *   cada palabra.
#  */

import string

def score_calculator(word) -> int:
    word = word.upper()
    alphabet = list(string.ascii_uppercase)
    result = 0
    for letter in word:
        result += (alphabet.index(letter) + 1)
    return result

while True:
    word = input("Introduzca una palabra: ")
    result = score_calculator(word)
    print(f"Su palabra suma: {result} puntos")
    if result == 100:
        print("Has introducido una palabra de 100 puntos! El programa finalizará.")
        break


