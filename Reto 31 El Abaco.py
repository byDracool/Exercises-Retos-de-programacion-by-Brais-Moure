# /*
#  * Crea una función que sea capaz de leer el número representado por el ábaco.
#  * - El ábaco se representa por un array con 7 elementos.
#  * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
#  *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
#  * - El primer elemento del array representa los millones, y el último las unidades.
#  * - El número en cada elemento se representa por las cuentas que están a
#  *   la izquierda del alambre.
#  *
#  * Ejemplo de array y resultado:
#  * ["O---OOOOOOOO",
#  *  "OOO---OOOOOO",
#  *  "---OOOOOOOOO",
#  *  "OO---OOOOOOO",
#  *  "OOOOOOO---OO",
#  *  "OOOOOOOOO---",
#  *  "---OOOOOOOOO"]
#  *
#  *  Resultado: 1.302.790
#  */

def convert_to_number(array):
    result = []
    for i in array:
        if i[0] == "-":
            result.append("0")
        else:
            result.append(str(len(i.split("-")[0])))
    return print(f"{result[0]}.{(''.join(result[1:4]))}.{(''.join(result[4:7]))}")


if __name__ == '__main__':
    combination = ["O---OOOOOOOO",
                        "OOO---OOOOOO",
                        "---OOOOOOOOO",
                        "OO---OOOOOOO",
                        "OOOOOOO---OO",
                        "OOOOOOOOO---",
                        "---OOOOOOOOO"]
    convert_to_number(combination)
