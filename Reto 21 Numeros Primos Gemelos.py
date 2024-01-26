# /*
#  * Crea un programa que encuentre y muestre todos los pares de números primos
#  * gemelos en un rango concreto.
#  * El programa recibirá el rango máximo como número entero positivo.
#  *
#  * - Un par de números primos se considera gemelo si la diferencia entre
#  *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  *
#  * - Ejemplo: Rango 14
#  *   (3, 5), (5, 7), (11, 13)
#  */

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def twin_prime_numbers_finder(prime_numbers):
    twin_prime_numbers = [] # [2, 3, 5, 7, 11, 13]
    for index, n in enumerate(prime_numbers):
        try:
            if (prime_numbers[index + 1] - prime_numbers[index]) == 2:
                twin_prime_numbers.append((prime_numbers[index], prime_numbers[index + 1]))
            else:
                continue
        except:
            continue

    return twin_prime_numbers


prime_numbers = []
max_range = 14

for num in range(1, max_range + 1):
    if is_prime(num):
        prime_numbers.append(num)

print(f"prime numbers: {prime_numbers}")
print(f"twin prime numbers: {twin_prime_numbers_finder(prime_numbers)}")
twin_prime_numbers_finder(prime_numbers)


