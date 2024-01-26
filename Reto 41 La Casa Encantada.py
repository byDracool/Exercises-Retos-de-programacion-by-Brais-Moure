# /*
#  * Este es un reto especial por Halloween.
#  * Te encuentras explorando una mansión abandonada llena de habitaciones.
#  * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
#  * Tu misión es encontrar la habitación de los dulces.
#  *
#  * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
#  * (Tienes total libertad para ser creativo con los textos)
#  *
#  * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#  *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
#  *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
#  *   Esta podría ser una representación:
#  *   🚪⬜️⬜️⬜️
#  *   ⬜️👻⬜️⬜️
#  *   ⬜️⬜️⬜️👻
#  *   ⬜️⬜️🍭⬜️
#  * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
#  *   Si no lo aciertas no podrás desplazarte.
#  * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#  *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
#  * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
#  * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
#  *   tengas que responder dos preguntas para salir de ella.
#  */

import random
import os
from Reto_41_riddles import riddles


def house_printer(house, *args):
    for floor_index, floor in enumerate(house):
        for room_index, room in enumerate(floor):
            if room == "🎃":
                house[floor_index][room_index] = "⬜️"
    if args:
        house[player_row][player_column] = "🎃"
    for room in house:
        print(room)


def create_house():

    house = [
        ["⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️"]
    ]

    # Create start door
    door_row = random.randint(0, 3)
    door_column = random.randint(0, 3)
    house[door_row][door_column] = "🚪️️️️️"

    # Create exit
    exit_row = random.randint(0, 3)
    exit_column = random.randint(0, 3)
    house[exit_row][exit_column] = "🍭"

    # Generate ghosts
    for floor_index, floor in enumerate(house):
        for room_index, room in enumerate(floor):
            if room == "⬜️":
                random_number = random.randint(1, 10)
                if random_number == 1:
                    house[floor_index][room_index] = "👻"
            else:
                continue
    return house, door_row, door_column, exit_row, exit_column


def generate_riddle() -> tuple:
    riddle = random.choice(riddles)
    return riddle # -> Tupla de: (acertijo, solucion)


def check_answer(riddle) -> bool:
    print(riddle[0])
    player_answer = input("Solucion: ")
    player_answer.lower()
    if player_answer == riddle[1]:
        print("\nRespuesta correcta!\n")
        return True
    else:
        return False


def game(house, player_row, player_column, exit_row, exit_column):
    number_of_riddles = 0
    endgame = False
    final_riddle = False

    if house[player_row][player_column] == "👻":
        # 2 preguntas
        number_of_riddles = 2

    elif house[player_row][player_column] == house[exit_row][exit_column]: # "🍭"
        # pregunta final
        number_of_riddles = 0
        endgame = True

    else: # "⬜️"
        # 1 pregunta
        number_of_riddles = 1

    while number_of_riddles > 0:
            riddle = generate_riddle()
            validation = check_answer(riddle) # True/False
            if validation:
                number_of_riddles -= 1
                player_row, player_column = movement(house, player_row, player_column)
            else:
                print("Respuesta incorrecta.")
                continue
    return house, player_row, player_column, endgame


def movement(house, player_row, player_column):
    # norte/sur/este/oeste solo opciones disponibles
    print("Donde deseas moverte?\n"
          "Opciones disponibles: ")

    # Norte
    if  player_row > 0 and player_row <= 3:
        print("[N]orte")

    # Sur
    if player_row >= 0 and player_row < 3:
        print("[S]ur")

    # Este
    if player_column >= 0 and player_column < 3:
        print("[E]ste")

    # Oeste
    if player_column > 0 and player_column <= 3:
        print("[O]este")

    valid_movement = False

    while not valid_movement:
        select_movement = input("Direccion: ")
        select_movement.upper()

        if select_movement == "N":
            player_row -= 1
            valid_movement = True
        elif select_movement == "S":
            player_row += 1
            valid_movement = True
        elif select_movement == "E":
            player_column += 1
            valid_movement = True
        elif select_movement == "O":
            player_column -= 1
            valid_movement = True
        else:
            print("Opcion incorrecta.")

    return player_row, player_column


if __name__ == "__main__":
    print("""
    👻 BoooOOOoOoo!
    Si quieres encontrar los dulces 🍭 de la casa encantada 🏰
    tendrás que buscarlos a través de sus habitaciones.
    Pero recuerda, no podrás moverte si antes no respondes
    correctamente a su enigma.
    """)
    house, player_row, player_column, exit_row, exit_column = create_house()
    house_printer(house)
    endgame = False
    player_row, player_column = movement(house, player_row, player_column)
    house_printer(house, player_row, player_column)

    while not endgame:
        house, player_row, player_column, endgame = game(house, player_row, player_column, exit_row, exit_column)
        house_printer(house, player_row, player_column)

    else:
        os.system("cls")
        print("""
        👻 BoooOOOoOoo!
        Has encontrado los dulces 🍭 y escapado de la casa encantada 🏰
        Feliz Halloween! 🎃
            """)
        exit()



