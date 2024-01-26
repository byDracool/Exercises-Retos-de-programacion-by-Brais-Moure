# /*
#  * Crea un programa que analice texto y obtenga:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto (cada vez que aparecen un punto).
#  * - Encuentre la palabra más larga.
#  *
#  * Todo_ esto utilizando un único bucle.
#  */

def text_analicer(text):
    text_splitted = text.split()

    # Número total de palabras
    words_counter = len(text.split())
    print(f"Número total de palabras: {words_counter}")

    # Número de oraciones del texto (cada vez que aparecen un punto)
    dot_counter = 0
    for char in text_splitted:
        if "." in char:
            dot_counter += 1

    print(f"Número de oraciones del texto: {dot_counter}")

    # Encuentre la palabra más larga

    longest_word = ""

    for word in text_splitted:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"Palabra más larga: '{longest_word}'")

    # Longitud media de las palabras
    shortest_word = ""

    for word in text_splitted:
        if len(word) > 0 and len(word) < len(shortest_word):
            shortest_word = word

    medium_lenght = (len(longest_word) + len(shortest_word)) / 2
    print(f"Longitud media de las palabras: {medium_lenght}")

text = """
Nos encontramos en un
periodo de guerra civil. Las
naves espaciales rebeldes,
atacando desde una base
oculta, han logrado su 
primera victoria contra
el malvado Imperio
Galáctico.

Durante la batalla, los 
espías rebeldes han
conseguido apoderarse de 
los planos secretos del
arma total y definitiva del
Imperio, la ESTRELLA
DE LA MUERTE,
una estación espacial
acorazada, llevando en sí
potencia suficiente para
destruir a un planeta
entero.

Perseguida por los 
siniestros agentes del 
Imperio, la Princesa Leia 
vuela hacia su patria, a
bordo de su nave espacial,
llevando consigo los
planos robados, que
pueden salvar a su pueblo
y devolver la libertad a la
galaxia....
"""
text_analicer(text)

