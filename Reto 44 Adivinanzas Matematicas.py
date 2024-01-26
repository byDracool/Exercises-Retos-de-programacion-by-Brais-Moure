# /*
#  * Crea un juego interactivo por terminal en el que tendrás que adivinar
#  * el resultado de diferentes operaciones matemáticas aleatorias
#  * (suma, resta, multiplicación o división de dos números enteros).
#  * - Tendrás 3 segundos para responder correctamente.
#  * - El juego finaliza si no se logra responder en ese tiempo.
#  * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
#  * - Cada 5 aciertos debes aumentar en uno el posible número de cifras
#  *   de la operación (cada vez en un operando):
#  *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#  *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#  *   - Preguntas 11 a 15: XX operación YY
#  *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#  *   ...
#  */
import os
import random
import threading


def generate_operation(answer_number):
    x = 0
    y = 0

    # Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
    if answer_number <= 5:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    # Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
    elif 5 < answer_number <= 10:
        x = random.randint(0, 99)
        y = random.randint(0, 9)

    # Preguntas 11 a 15: XX operación YY
    elif 10 < answer_number <= 15:
        x = random.randint(0, 99)
        y = random.randint(0, 99)

    # Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
    elif 15 < answer_number <= 20:
        x = random.randint(0, 999)
        y = random.randint(0, 99)

    operator = ["+", "-", "*", "/"]
    operator = random.choice(operator)

    if operator == "+":
        solution = x + y
    elif operator == "-":
        solution = x - y
    elif operator == "*":
        solution = x * y
    else:
        if y == 0:
            y += 1
        solution = x / y

    operation = str(x) + " " + str(operator) + " " + str(y) + " " + "="
    solution = str(solution)

    return solution, operation


def check_operation(solution, user_solution) -> bool:
    if solution == user_solution:
        return True
    else:
        return False


def input_with_timeout(operation):

    def on_timeout():
        print("\n¡El tiempo ha finalizado! Pulsa enter.")
        global game_on
        game_on = False

    timer = threading.Timer(5, on_timeout)
    timer.start()

    try:
        # answer = input(f"¿Cuál es el resultado de {num1} {operation} {num2}? ")
        answer = input(f"¿Cuál es el resultado de {operation} ? ")
    finally:
        timer.cancel()
    return answer


if __name__ == "__main__":
    answer_number = 0
    correct_answers = 0
    while answer_number < 21:
        os.system("cls")
        answer_number += 1
        print("\nPregunta numero: {}".format(answer_number))
        print("Contador preguntas acertadas: {}".format(correct_answers))
        solution, operation = generate_operation(answer_number)
        print("(Tienes 5 segundos para responder correctamente.)")
        user_answer = input_with_timeout(operation)

        is_correct = check_operation(solution, user_answer)
        if is_correct:
            print("Respuesta correcta!")
            correct_answers += 1
        else:
            print("Respuesta incorrecta.")

    os.system("cls")
    print("Juego finalizado.")
    print("Numero de respuestas correctas: {}".format(correct_answers))
    exit()
