# /*
#  * Crea un programa que sea capaz de generar e imprimir todas las
#  * permutaciones disponibles formadas por las letras de una palabra.
#  * - Las palabras generadas no tienen por qué existir.
#  * - Deben usarse todas las letras en cada permutación.
#  * - Ejemplo: sol, slo, ols, osl, los, lso
#  */

import itertools


def get_combinations(word):
    word = list(word)
    temp_words = itertools.permutations(word)
    possible_combinations = []
    temp_word = ""
    for comb in list(temp_words):
        #print(comb)
        for char in comb:
            #print(char)
            temp_word += char
        possible_combinations.append(temp_word)
        temp_word = ""

    return ("\n".join(possible_combinations))


if __name__ == "__main__":
    print(get_combinations("sol"))


