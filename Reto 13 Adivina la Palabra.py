# /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
#  *   ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */
import random


def word_generator() -> list:
    words_list = ["casa", "perro", "pantalla"]
    word_complete = random.choice(words_list)

    # La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%

    hidden_letters_word = [word for word in word_complete]
    max_hide = int(len(word_complete) * 0.6)
    letters_hidden = random.randint(1, max_hide)
    # Palabras ocultas
    remaining_letters = [random.choice(hidden_letters_word) for char in range(letters_hidden)]

    return word_complete, remaining_letters


def word_printer(word, remaining_letters):
    word_current_status = []
    for char in word:
        word_current_status.append(char) if char not in remaining_letters else word_current_status.append("_")
    print(" ".join(word_current_status))


def game(word_complete, remaining_letters, player_attemps):
    max_length = len(word_complete)
    player_input = ""

    while len(player_input) != 1 and len(player_input) != max_length:
        player_input = input("Escriba una letra que crea que esta o la palabra completa si quiere resolver: ").lower()


    if len(player_input) == 1:
        if player_input in remaining_letters:
            remaining_letters.remove(player_input)
        else:
            player_attemps -= 1
    else:
        if player_input == word_complete:
            remaining_letters = []
        else:
            player_attemps -= 1

    return word_complete, remaining_letters, player_attemps


def win_check(remaining_letters):
    if len(remaining_letters) == 0:

        return True
    else:
        return False


if __name__ == "__main__":
    player_attemps = 5
    word_complete, remaining_letters = word_generator()
    word_printer(word_complete, remaining_letters)
    print("Intenta adivinar la palabra escondida.")

    while player_attemps > 0:
        print("Te quedan {} intentos".format(player_attemps))
        word_complete, remaining_letters, player_attemps = game(word_complete, remaining_letters, player_attemps)
        winner = win_check(remaining_letters)
        if winner:
            print("Enhorabuena, has descubierto la palabra secreta. ({})".format(word_complete.upper()))
            exit()
        else:
            print("Nueva ronda")
            word_printer(word_complete, remaining_letters)
    else:
        print("Lo siento, ha perdido")


