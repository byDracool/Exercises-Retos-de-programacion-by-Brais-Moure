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
import os
import random
from abc import ABC, abstractmethod


def hand_selector() -> str:
    player_hand_possibilities = ["Piedra", "Papel", "Tijera", "Lagarto", "Spoc"]
    valid_options = [1, 2, 3, 4, 5]
    player_selection = ""
    while player_selection not in valid_options:
        print()
        [print(index + 1, n) for index, n in enumerate(player_hand_possibilities)]
        player_selection  = int(input("Elija su mano [1,2,3,4,5]: "))
        player_hand = player_hand_possibilities[player_selection - 1]
        print("Ha elegido: {}".format(player_hand))

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

class Hand(ABC):

    @abstractmethod
    def name(self, Hand):
        pass

    @abstractmethod
    def play(self, Hand):
        pass

    @abstractmethod
    def play_vs_rock(self, Hand):
        pass

    @abstractmethod
    def play_vs_paper(self, Hand):
        pass

    @abstractmethod
    def play_vs_scissor(self, Hand):
        pass

    @abstractmethod
    def play_vs_lizard(self, Hand):
        pass

    @abstractmethod
    def play_vs_spoc(self, Hand):
        pass


class Jugador(ABC):

    def name(self, hand):
        return str(hand)

    def from_str_to_hand (hand):
        if hand == "Tijera":
            return Tijera()
        elif hand == "Piedra":
            return Piedra()
        elif hand == "Papel":
            return Papel()
        elif hand == "Lagarto":
            return Lagarto()
        elif hand == "Spoc":
            return Spoc()
        raise ValueError


class Tijera(Hand):

    def name(self):
        return "Tijera"

    def play(self, bot_hand: Hand):
        return bot_hand.play_vs_scissor(Hand)

    def play_vs_rock(self, bot_hand: Hand):
        return True

    def play_vs_paper(self, bot_hand: Hand):
        return False

    def play_vs_scissor(self, bot_hand: Hand):
        return "Tie"

    def play_vs_lizard(self, bot_hand: Hand):
        return False

    def play_vs_spoc(self, bot_hand: Hand):
        return True


class Piedra(Hand):

    def name(self):
        return "Piedra"

    def play(self, bot_hand: Hand):
        return bot_hand.play_vs_rock(Hand)

    def play_vs_rock(self, bot_hand: Hand):
        return "Tie"

    def play_vs_paper(self, bot_hand: Hand):
        return True

    def play_vs_scissor(self, bot_hand: Hand):
        return False

    def play_vs_lizard(self, bot_hand: Hand):
        return False

    def play_vs_spoc(self, bot_hand: Hand):
        return True


class Papel(Hand):

    def name(self):
        return "Papel"

    def play(self, bot_hand: Hand):
        return bot_hand.play_vs_paper(Hand)

    def play_vs_rock(self, bot_hand: Hand):
        return False

    def play_vs_paper(self, bot_hand: Hand):
        return "Tie"

    def play_vs_scissor(self, bot_hand: Hand):
        return True

    def play_vs_lizard(self, bot_hand: Hand):
        return True

    def play_vs_spoc(self, bot_hand: Hand):
        return False


class Lagarto(Hand):

    def name(self):
        return "Lagarto"

    def play(self, bot_hand: Hand):
        return bot_hand.play_vs_lizard(Hand)

    def play_vs_rock(self, bot_hand: Hand):
        return True

    def play_vs_paper(self, bot_hand: Hand):
        return False

    def play_vs_scissor(self, bot_hand: Hand):
        return True

    def play_vs_lizard(self, bot_hand: Hand):
        return "Tie"

    def play_vs_spoc(self, bot_hand: Hand):
        return False


class Spoc(Hand):

    def name(self):
        return "Spoc"

    def play(self, bot_hand: Hand):
        return bot_hand.play_vs_spoc(Hand)

    def play_vs_rock(self, bot_hand: Hand):
        return False

    def play_vs_paper(self, bot_hand: Hand):
        return True

    def play_vs_scissor(self, bot_hand: Hand):
        return False

    def play_vs_lizard(self, bot_hand: Hand):
        return True

    def play_vs_spoc(self, bot_hand: Hand):
        return "Tie"


if __name__ == "__main__":
    player_counter = 0
    bot_counter = 0

    while player_counter < 5 and bot_counter < 5:
        player_selection = hand_selector()
        player_hand = Jugador.from_str_to_hand(player_selection)

        bot_selection = bot_selector()
        bot_hand = Jugador.from_str_to_hand(bot_selection)

        result = player_hand.play(bot_hand)
        player_counter, bot_counter = printer(result, player_hand.name(), bot_hand.name(), player_counter, bot_counter)

    else:
        os.system("cls")
        if player_counter > bot_counter:
            counter(player_counter, bot_counter)
            print("Ha ganado!")
        else:
            counter(player_counter, bot_counter)
            print("Gano la CPU, intentelo de nuevo")