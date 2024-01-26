# /*
#  * Crea una función que reciba dos cadenas de texto casi iguales,
#  * a excepción de uno o varios caracteres.
#  * La función debe encontrarlos y retornarlos en formato lista/array.
#  * - Ambas cadenas de texto deben ser iguales en longitud.
#  * - Las cadenas de texto son iguales elemento a elemento.
#  * - No se pueden utilizar operaciones propias del lenguaje
#  *   que lo resuelvan directamente.
#  *
#  * Ejemplos:
#  * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
#  * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
#  */

def infiltrated_characters(str1, str2):
    result = []
    str1 = list(str1)
    str2 = list(str2)

    if len(str1) == len(str2):
        for index, value in enumerate(str2):
            if value == str1[index]:
                continue
            else:
                result.append(value)
    else:
        return "Error, las cadenas no tienen la misma longitud."

    return result


print(infiltrated_characters("Me llamo mouredev", "Me llemo mouredov"))
print(infiltrated_characters("Me llamo.Brais Moure", "Me llamo brais moure"))
print(infiltrated_characters("", "a"))

