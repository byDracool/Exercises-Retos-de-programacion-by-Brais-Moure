# /*
#  * Crea una función que sea capaz de transformar Español al lenguaje básico
#  * del universo Star Wars: el "Aurebesh".
#  * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#  * - También tiene que ser capaz de traducir en sentido contrario.
#  *
#  * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  *
#  * ¡Que la fuerza os acompañe!
#  */

import string
import copy


def aurebesh_encoder(text, aurebesh: bool):
    text_traduction = ""
    basic_alphabet = {
            "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
            "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
            "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
            "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"}

    if aurebesh:

        for index, letter in enumerate(text):
            alphabet = list(string.ascii_lowercase)
            next_letter = None
            if letter not in alphabet:
                text_traduction += letter
            else:
                try:
                    next_letter = text[index + 1]
                    #print(next_letter)
                except:
                    text_traduction += basic_alphabet[letter]

                if next_letter:
                    if letter == "a" and next_letter == "e":
                        text_traduction += basic_alphabet["ae"]

                    elif letter == "e" and next_letter == "o":
                        text_traduction += basic_alphabet["eo"]

                    elif letter == "k" and next_letter == "h":
                        text_traduction += basic_alphabet["kh"]

                    elif letter == "n" and next_letter == "g":
                        text_traduction += basic_alphabet["ng"]

                    elif letter == "o" and next_letter == "o":
                        text_traduction += basic_alphabet["oo"]

                    elif letter == "s" and next_letter == "h":
                        text_traduction += basic_alphabet["sh"]

                    elif letter == "t" and next_letter == "h":
                        text_traduction += basic_alphabet["th"]

                    else:
                        text_traduction += basic_alphabet[letter]

    else:
        text_traduction = copy.copy(text)

        for n in basic_alphabet:
            # print(n)
            # print(basic_alphabet[n])
            if basic_alphabet[n] in text_traduction:
                text_traduction = text_traduction.replace(basic_alphabet[n], n)

    return text_traduction


"""aurebesh = aurebesh_encoder("Hola, como estas.", aurebesh = True)
print(aurebesh)
print(aurebesh_encoder(aurebesh, False))"""
aurebesh = aurebesh_encoder("The MoureDev", False)
print(aurebesh)
basic = aurebesh_encoder(aurebesh, True)
print(basic)

aurebesh = aurebesh_encoder("Qué te ha parecido el reto? A mí me ha gustado mucho! Mañana sigue practicando.", False)
print(aurebesh)
basic = aurebesh_encoder(aurebesh, True)
print(basic)

