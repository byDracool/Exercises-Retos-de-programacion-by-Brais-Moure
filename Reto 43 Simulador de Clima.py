# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#  *     siguiente disminuya en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */
import random


def user_initial_data(data):
    try:
        number = int(input(f"Introduzca {data} para la prevision: "))
        return number
    except ValueError:
        print("Error: Introduce un número entero  positivo válido.")


def start_conditions(days, temperature, rain_prob):
    return print("""\nCondiciones iniciales:
    {} dias de prediccion
    Temperatura incial: {}
    Probabilidad de lluvia inicial: {}""".format(days, temperature, rain_prob))


def climate_model(days, temperature, rain_prob):
    temperatures_table = []
    rain_prob_table = []
    raining_days_counter = 0

    for i in range(1, days + 1):

        # Temperatura y % lluvia de cada dia
        print("""Dia {}:
        Temperatura: {}
        Probabilidad de lluvia: {}""".format(i, temperature, rain_prob))

        # Agregamos datos en sus listas
        temperatures_table.append(temperature)
        rain_prob_table.append(rain_prob)

        # 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
        random_possibilites = random.randint(1, 10)
        if random_possibilites == 1:
            increase_decrease_temperature = random.randint(1, 2)
            if increase_decrease_temperature == 1:
                temperature += 2
            else:
                temperature -= 2
        else:
            continue

        # Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
        if temperature > 25:
            rain_prob += 20

        # Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuya en un 20%.
        if temperature < 5:
            rain_prob -= 20

        # Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
        if rain_prob == 100 or rain_prob > 100:
            rain_prob = 100
            temperature -= 1

    # Temp maxima y minima
    print("""\nTemperatura maxima: {}
Temperatura minima: {}""".format(max(temperatures_table), min(temperatures_table)))

    # Numero de dias de lluvia
    for n in rain_prob_table:
        if n == 100:
            raining_days_counter += 1
    print("Dias de lluvia totales: {}".format(raining_days_counter))


if __name__ == "__main__":
    days = user_initial_data("el numero de dias")
    temperature = user_initial_data("la temperatura incial")
    rain_prob = user_initial_data("la probabilidad de lluvia incial")
    start_conditions(days, temperature, rain_prob)
    climate_model(days, temperature, rain_prob)
