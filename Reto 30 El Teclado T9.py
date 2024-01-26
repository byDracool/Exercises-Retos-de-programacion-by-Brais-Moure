# /*
#  * Los primeros dispositivos móviles tenían un teclado llamado T9
#  * con el que se podía escribir texto utilizando únicamente su
#  * teclado numérico (del 0 al 9).
#  *
#  * Crea una función que transforme las pulsaciones del T9 a su
#  * representación con letras.
#  * - Debes buscar cuál era su correspondencia original.
#  * - Cada bloque de pulsaciones va separado por un guión.
#  * - Si un bloque tiene más de un número, debe ser siempre el mismo.
#  * - Ejemplo:
#  *     Entrada: 6-666-88-777-33-3-33-888
#  *     Salida: MOUREDEV
#  */


def t9_to_text(message):
    input_to_list = message.split("-")
    converted_message = ""
    buttons_assignation = [
        [" "],  # 0
        [",", ".", "?", "!"],  # 1
        ["a", "b", "c"],  # 2
        ["d", "e", "f"],  # 3
        ["g", "h", "i"],  # 4
        ["j", "k", "l"],  # 5
        ["m", "n", "o"],  # 6
        ["p", "q", "r", "s"],  # 7
        ["t", "u", "v"],  # 8
        ["w", "x", "y", "z"],  # 9
        ]

    # Separamos todos los valores en bloques independientes
    for block in input_to_list:
        # Nos aseguramos que sea el mismo numero por cada bloque de numeros
        if len(set(block)) > 1 or len(set(block)) < 1:
            print("Valor incorrecto")
        else:
            digit = int(block[0][0])
            # Comprobamos que el numero de digitos iguales sea correcto
            if len(block) > len(buttons_assignation[digit]):
                print("Demasiados digitos.")
            else:
                word = buttons_assignation[digit][len(block)-1]
                converted_message += word

    return converted_message


if __name__ == "__main__":
    print(t9_to_text("6-666-88-777-33-3-33-888"))
    print(t9_to_text("6-666-88-777-33-0-3-33-888"))
    print(t9_to_text("6-676-88-777-33-3-33-888"))
    print(t9_to_text("6-6a6-88-777-33-3-33-888"))
    print(t9_to_text(""))
    print(t9_to_text("2222"))


