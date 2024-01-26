# /*
#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
#  */


def find_params(url:str) -> list:
    params = []
    url = url.split("&")
    print(url)

    for element in url:
        if "=" in element:
            element = element.split("=")
            if element[1] != "":
                params.append(element[1])

    return params


if __name__ == "__main__":
    url = "https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"
    url2 = "https://retosdeprogramacion.com?year=2023&challenge=0"
    url3 = "https://www.youtube.com/watch?&v=hUX46tEpc2A"
    print(find_params(url))
    print(find_params(url2))
    print(find_params(url3))


