# /*
#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.
#  */

def to_octal_and_hex(number):
    # Octal
    octal = ""
    result = number
    while result >= 8:
        rest = result % 8
        result = int(result / 8)
        octal += (str(rest))
    else:
        octal += (str(result))

    print(f"{number} en octal es {octal[::-1]}")

    # Hexadecimal
    hex = ""
    result = number
    special_values = ["A", "B", "C", "D", "E", "F"]

    while result >= 16:
        rest = result % 16
        result = int(result / 16)
        if rest < 10:
            hex += (str(rest))
        if rest > 10:
            letter = special_values[rest - 10]
            hex += letter
    else:
        if result > 10:
            letter = special_values[result - 10]
            hex += letter
        else:
            hex += (str(result))

    print(f"{number} en hexadecimal es {hex[::-1]}")


to_octal_and_hex(0)
to_octal_and_hex(100)
to_octal_and_hex(1000)


