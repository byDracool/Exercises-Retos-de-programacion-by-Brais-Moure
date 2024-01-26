# /*
#  * Crea un programa que simule la competición de dos coches en una pista.
#  * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
#  * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
#  * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
#  * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#  *   🏁____🌲_____🚙
#  *   🏁_🌲____🌲___🚗
#  *
#  * El juego se desarrolla por turnos de forma automática, y cada segundo
#  * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
#  * uno de ellos (o los dos a la vez) llega a la meta.
#  * - Acciones:
#  *   - Avanzar entre 1 a 3 posiciones hacia la meta.
#  *   - Si al avanzar, el coche finaliza en la posición de un árbol,
#  *     se muestra 💥 y no avanza durante un turno.
#  *   - Cada turno se imprimen las pistas y sus elementos.
#  *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
#  */

import random
import os
import time


def car_track_generator(length):
    car_track = ["🏁"]
    number_of_trees = random.randint(1, 3)
    print("{} trees".format(number_of_trees))
    for n in range(length):
        car_track.append("_")
    while number_of_trees > 0:
        add_tree = random.randint(1, length)
        if car_track[add_tree] == "_":
            car_track[add_tree] = "🌲"
            number_of_trees -= 1
        else:
            continue
    return car_track


def tracks_printer(car_track, car_image, car_index):
    for n in car_track:
        if n == car_image:
            car_track.remove(n)
    car_track.insert(car_index + 1, car_image)

    return print("".join(car_track))


def cars_competition(car1_track, car1_index, car2_track, car2_index):
    car_track_list = [car1_track, car2_track]
    if car1_track[car1_index] == "💥":
        car1_track[car1_index] = "_"
    else:
        car1_index -= (random.randint(1, 3))
        if car1_index < 0:
            car1_index = 0
        else:
            car1_index = car1_index
        if car1_track[car1_index] == "🌲":
            car1_track.insert(car1_index, "💥")
            del car1_track[car1_index + 1]

    if car2_track[car2_index] == "💥":
        car2_track[car2_index] = "_"
    else:
        car2_index -= (random.randint(1, 3))
        if car2_index < 0:
            car2_index = 0
        else:
            car2_index = car2_index
        if car2_track[car2_index] == "🌲":
            car2_track.insert(car2_index, "💥")
            del car2_track[car2_index + 1]

    return car1_track, car1_index, car2_track, car2_index


def check_winner(car_index, car_image):
    if car_index > 0:
        return False
    else:
        return print(f"El coche {car_image} ha llegado a la meta!")


if __name__ == "__main__":
    length = 20
    turn = 1
    car1_track = car_track_generator(length)
    car2_track = car_track_generator(length)
    car1_image = "🚙"
    car2_image = "🚗"
    car1_index = length
    car2_index = length
    tracks_printer(car1_track, car1_image, car1_index)
    tracks_printer(car2_track, car2_image, car2_index)
    while car1_index > 0 and car2_index > 0:
        print(f"Turno {turn}:")
        car1_track, car1_index, car2_track, car2_index = cars_competition(car1_track, car1_index, car2_track, car2_index)
        tracks_printer(car1_track, car1_image, car1_index)
        tracks_printer(car2_track, car2_image, car2_index)
        turn += 1
        time.sleep(1)

    else:
        os.system("cls")
        check_winner(car1_index, car1_image)
        check_winner(car2_index, car2_image)
        print("Carrera finalizada")


