# /*
#  * Crea una función que reciba una expresión matemática (String)
#  * y compruebe si es correcta. Retornará true o false.
#  * - Para que una expresión matemática sea correcta debe poseer
#  *   un número, una operación y otro número separados por espacios.
#  *   Tantos números y operaciones como queramos.
#  * - Números positivos, negativos, enteros o decimales.
#  * - Operaciones soportadas: + - * / %
#  *
#  * Ejemplos:
#  * "5 + 6 / 7 - 4" -> true
#  * "5 a 6" -> false
#  */

def value_checker(value):
    try:
        float(value)
        return True
    except:
        return False


def checkmathexp(expression: str) -> bool:
    supported_operations = ["+", "-", "*", "/", "%"]
    expression = expression.split(" ")
    if len(expression) < 3 or len(expression) % 2 == 0:
        return False
    else:
        for value in expression:
            if value_checker(value) is True or value in supported_operations:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    print(checkmathexp("5 + 6 / 7 - 4"))
    print(checkmathexp("5 a 6"))
    print(checkmathexp("hola"))
    print(checkmathexp("2.1 * -1"))
    print(checkmathexp("3 + 5"))
    print(checkmathexp("3 a 5"))
    print(checkmathexp("-3 + 5"))
    print(checkmathexp("- 3 + 5"))
    print(checkmathexp("-3 a 5"))
    print(checkmathexp("-3+5"))
    print(checkmathexp("3 + 5 - 1 / 4 % 8"))
    print(checkmathexp("-3"))


