# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  * fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */


def check_prime_fibonacci_even(number):
    result = f"{number} "

    # Prime

    if number > 1:
        for n in range (2, number):
            if number %n == 0:
                result += "no es primo"
                break
        else:
            result += "es primo"
    else:
        result += "no es primo"

    # Fibonacci
    fibonacci_list = [1, 1]
    index = 0
    while index <= number:
        fibonacci_list.append(fibonacci_list[index] + fibonacci_list[index + 1])
        index += 1
    if number in fibonacci_list:
        result += ", es fibonacci"
    else:
        result += ", no es fibonacci"

    # Par / impar
    if number %2 == 0:
        result += " y es par"
    else:
        result += " y es impar"

    return print(result)


if __name__ == "__main__":
    check_prime_fibonacci_even(2)
    check_prime_fibonacci_even(7)
    check_prime_fibonacci_even(0)
    check_prime_fibonacci_even(1)
    check_prime_fibonacci_even(-2)


