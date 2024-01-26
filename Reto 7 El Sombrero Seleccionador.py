# /*
#  * Crea un programa que simule el comportamiento del sombrero selccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts:
#  *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
#  *   y crear el algoritmo seleccionador:
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  */
# gryffindor: valor
# hufflepuff: lealtad
# ravenclaw: sabiduría
# slytherin: ambición

from collections import Counter


def selector_hat():
    answers = []
    print("Hola, soy el \"Sombrero Seleccionador\"\nTendrás que responder cinco preguntas para ayudarme a descubrir "
          "tu casa de Hogwarts.\n")

    # Tuplas (pregunta, [respuestas: (opciones, casa)]
    HatQuestion1 = ("¿Cómo te definirías?", [
                        ("1. Valiente", "gryffindor"),
                        ("2. Leal", "hufflepuff"),
                        ("3. Sabio", "ravenclaw"),
                        ("4. Ambicioso", "slytherin")]
                    )
    HatQuestion2 = ("¿Cuál es tu clase favorita?", [
                        ("1. Vuelo", "gryffindor"),
                        ("2. Pociones", "ravenclaw"),
                        ("3. Defensa contra las artes oscuras", "slytherin"),
                        ("4. Animales fantásticos", "hufflepuff")]
                    )

    HatQuestion3 = ("¿Dónde pasarías más tiempo?", [
                        ("1. Invernadero", "hufflepuff"),
                        ("2. Biblioteca", "ravenclaw"),
                        ("3. En la sala común", "slytherin"),
                        ("4. Explorando", "gryffindor")]
                    )

    HatQuestion4 = ("¿Cuál es tu color favorito?", [
                        ("1. Rojo", "gryffindor"),
                        ("2. Azul", "ravenclaw"),
                        ("3. Verde", "slytherin"),
                        ("4. Amarillo", "hufflepuff")]
                    )

    HatQuestion5 = ("¿Cuál es tu mascota?", [
                        ("1. Sapo", "ravenclaw"),
                        ("2. Lechuza", "gryffindor"),
                        ("3. Gato", "hufflepuff"),
                        ("4. Serpiente", "slytherin")]
                    )

    hat_questions = [HatQuestion1, HatQuestion2, HatQuestion3, HatQuestion4, HatQuestion5]
    valid_options = [1, 2, 3, 4]

    for question in hat_questions:
        print(question[0])
        for valid_answer in range(4):
            user_answer = 0
            print(question[1][valid_answer][0])

        while user_answer not in valid_options:
            user_answer = int(input("Responde 1, 2, 3 o 4: "))
        answers.append(question[1][user_answer -1][1])


    counter = Counter(answers)
    first = counter.most_common()

    return print(f"\n\nTu casa será: {first[0][0].upper()}")


selector_hat()

