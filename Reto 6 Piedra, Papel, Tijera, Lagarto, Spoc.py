# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */

import random
import os


def hand_selector() -> str:
    player_hand_possibilities = ["Piedra", "Papel", "Tijera", "Lagarto", "Spoc"]
    valid_options = [1, 2, 3, 4, 5]
    player_selection = ""
    while player_selection not in valid_options:
        print()
        [print(index + 1, n) for index, n in enumerate(player_hand_possibilities)]
        player_selection  = int(input("Elija su mano [1,2,3,4,5]: "))
        if player_selection in valid_options:
            player_hand = player_hand_possibilities[player_selection - 1]
            print("Ha elegido: {}".format(player_hand))
        else:
            print("Opcion incorrecta, seleccione una opcion valida.")

    return player_hand


def bot_selector() -> str:
    bot_hand_possibilities = ["Piedra", "Papel", "Tijera", "Lagarto", "Spoc"]
    return random.choice(bot_hand_possibilities)


def printer(result, player_hand, bot_hand, player_counter, bot_counter):
    images = {
        "Tijera":"✂️",
        "Piedra":"🗿",
        "Papel":"📄",
        "Lagarto":"🦎",
        "Spoc": "🖖"
    }

    print(f"\t\n{player_hand} {images[player_hand]} vs {bot_hand} {images[bot_hand]}\n")

    if result == True:
        player_counter += 1
        print("GANAS")
    elif result == False:
        bot_counter += 1
        print("PIERDE")
    else:
        print("EMPATE")
        print("No se sumaran puntos")

    counter(player_counter, bot_counter)

    return player_counter, bot_counter


def counter(player_counter, bot_counter):
    print(f"""
Contador puntos:
Jugador: {player_counter}
CPU: {bot_counter}
    """)


def game(player_hand, bot_hand) -> bool:
    if player_hand == "Tijera":
        if bot_hand == "Papel" or bot_hand == "Lagarto":
            return True
        elif bot_hand == "Piedra" or bot_hand == "Spoc":
            return False
        else:
            return "Tie"

    elif player_hand == "Papel":
        if bot_hand == "Piedra" or bot_hand == "Spoc":
            return True
        elif bot_hand == "Tijera" or bot_hand == "Lagarto":
            return False
        else:
            return "Tie"

    elif player_hand == "Piedra":
        if bot_hand == "Tijera" or bot_hand == "Lagarto":
            return True
        elif bot_hand == "Papel" or bot_hand == "Spoc":
            return False
        else:
            return "Tie"

    elif player_hand == "Lagarto":
        if bot_hand == "Spoc" or bot_hand == "Papel":
            return True
        elif bot_hand == "Tijera" or bot_hand == "Piedra":
            return False
        else:
            return "Tie"

    elif player_hand == "Spoc":
        if bot_hand == "Tijera" or bot_hand == "Piedra":
            return True
        elif bot_hand == "Lagarto" or bot_hand == "Papel":
            return False
        else:
            return "Tie"

    else:
        raise ValueError


if __name__ == "__main__":
    player_counter = 0
    bot_counter = 0
    counter(player_counter, bot_counter)

    while player_counter < 5 and bot_counter < 5:
        player_hand = hand_selector()
        bot_hand = bot_selector()
        result = game(player_hand, bot_hand)
        player_counter, bot_counter = printer(result, player_hand, bot_hand, player_counter, bot_counter)
        counter(player_counter, bot_counter)

    else:
        os.system("cls")
        if player_counter > bot_counter:
            counter(player_counter, bot_counter)
            print("Ha ganado!")
        else:
            counter(player_counter, bot_counter)
            print("Gano la CPU, intentelo de nuevo")
        exit()



