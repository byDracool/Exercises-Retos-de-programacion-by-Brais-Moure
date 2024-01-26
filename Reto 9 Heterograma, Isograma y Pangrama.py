# /*
#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.
#  */

import string
from unidecode import unidecode


def isHeterogram(text) -> bool:
    # Ninguna letra repetida
    text = unidecode(text.lower())
    alfabet = list(string.ascii_lowercase)
    for char in text:
        if char in alfabet:
            counter = text.count(char)
            if counter > 1:
                return False
        else:
            continue
    return True


def isIsogram(text) -> bool:
    # Palabra o frase en la que cada letra aparece el mismo número de veces.
    text = unidecode(text.lower())
    counter_list = []
    alfabet = list(string.ascii_lowercase)
    for char in text:
        if char in alfabet:
            counter = text.count(char)
            counter_list.append(counter)
        else:
            continue
    for value in counter_list:
        if value == counter_list[0]:
            continue
        else:
            return False
    return True


def isPangram(text) -> bool:
    # Frase en la que aparecen todas las letras del abecedario
    text = unidecode(text.lower())
    alfabet = list(string.ascii_lowercase )
    for char in text:
        if char in alfabet:
            alfabet.remove(char)
    if len(alfabet) > 0:
        return False
    else:
        return True


print("Heterogramas:")
print(isHeterogram("yuxtaponer"))
print(isHeterogram("acondicionar"))
print('\n')

print("Isogramas:")
print(isIsogram("caca"))
print(isIsogram("kiwi"))
print('\n')

print("Pangramas:")
print(isPangram("El veloz murcielago hindu comia feliz cardillo y kiwi. La cigueña tocaba el saxofon detras del "
                "palenque de paja."))
print(isPangram("El veloz murcielago hindu comia feliz cardillo y kiwi."))
print('\n')

print(isHeterogram("hiperblanduzcos"))
print(isHeterogram("hiperblanduzcós   $## !!w"))
print(isIsogram("anna"))
print(isPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"))



