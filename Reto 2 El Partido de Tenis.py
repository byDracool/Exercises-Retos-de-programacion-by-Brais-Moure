# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  *
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
#  */

def tie(game_points):
    ties = ["Deuce", "Advantage", "Win"]
    winner = "Winner: "
    player1_index = 0
    player2_index = 0

    for player in game_points:
        if player == "P1":
            player1_index += 1
            player2_index -= 1 if player2_index > 0 else 0

        else:
            player2_index += 1
            player1_index -= 1 if player1_index > 0 else 0

        if player1_index == 1 and player1_index > player2_index:
            print("P1 Advantage")
        elif player2_index == 1 and player2_index > player1_index:
            print("P2 Advantage")

        elif player1_index == 2:
            winner += "P1"
            return winner
        elif player2_index == 2:
            winner += "P2"
            return winner

    endgame = (f"{ties[player1_index]} - {ties[player2_index]}")
    return endgame


def match(game_points: list):
    points = ["Love", 15, 30, 40, "Win"]


    player1_index = 0
    player2_index = 0
    player1_points = points[player1_index]
    player2_points = points[player2_index]

    for index, player in enumerate(game_points):

        # Se hara siempre
        if player == "P1":
            player1_index += 1
        else:
            player2_index += 1


        if player1_points == "Win":
            print("Ha ganado el P1")
            break
        elif player2_points == "Win":
            print("Ha ganado el P2")
            break

        elif player1_points == 40 and player2_points == 40:
            print("Deuce")
            print(tie(game_points[index:]))
            break


        player1_points = points[player1_index]
        player2_points = points[player2_index]
        print(f"{player1_points} - {player2_points}")


match(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])


