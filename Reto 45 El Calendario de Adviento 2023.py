# /*
#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#  *   participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#  *   (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#  *   (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar
#  *   y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.
#  */
import os
import random


def menu():
    print("""Menu opciones:
    1.Anadir participante
    2.Borrar participante
    3.Mostrar participantes
    4.Lanzar sorteo
    5.Salir
    """)
    valid_options = ["1", "2", "3", "4", "5"]
    option = ""
    while option not in valid_options:
        option = input("Elija una opcion valida: ")
    else:
        return option


def options(contestants_list, option):
    if option == "1":
        name = input("Escriba el nombre del participante: ")
        if name not in contestants_list:
            contestants_list.append(name)
        else:
            print("Nombre duplicado, no se añadira al listado.")

    elif option == "2":
        name = input("Escriba el nombre del participante que desea borrar: ")
        if name in contestants_list:
            print(f"Nombre {name} borrado del listado.")
            contestants_list.remove(name)
        else:
            print("Nombre no encontrado.")

    elif option == "3":
        print("Listado de participantes: ")
        for contestant in contestants_list:
            print(contestant)

    elif option == "4":
        name = random.choice(contestants_list)
        print(f"El ganador del sorteo es \"{name}\".")
        contestants_list.remove(name)

    elif option == "5":
        print("Programa finalizado")
        exit()

    return contestants_list


if __name__ == "__main__":
    contestants = []
    while True:
        os.system("cls")
        user_option = menu()
        print(user_option)
        options(contestants, user_option)

