# /*
#  * Como cada año, el día 256 se celebra el "Día de la Programación".
#  * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos
#  * 256 regalos para seguir aprendiendo programación:
#  * https://diadelaprogramacion.com
#  *
#  * Para seguir ayudando, te propongo este reto:
#  * Mostrar la sintaxis de los principales elementos de un lenguaje
#  * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
#  *
#  * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
#  * y comenta cada bloque para identificar con qué se corresponde:
#  * - Haz un "Hola, mundo!"
#  * - Crea variables de tipo String, numéricas (enteras y decimales)
#  *   y Booleanas (o cualquier tipo de dato primitivo).
#  * - Crea una constante.
#  * - Usa un if, else if y else.
#  * - Crea estructuras como un array, lista, tupla, set y diccionario.
#  * - Usa un for, foreach y un while.
#  * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
#  * - Crea una clase.
#  * - Muestra el control de excepciones.
#  *
#  * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
#  * de sintaxis básica de muchos lenguajes.
#  *
#  * ¡Muchas gracias!
#  */


#  * - Haz un "Hola, mundo!"
print("Hello world")

#  * - Crea variables de tipo String, numéricas (enteras y decimales) y Booleanas (o cualquier tipo de dato primitivo).
variable_string = "Esta es una string"
variable_numerica_entera = 25
variable_numerica_decimal = 52.2
variable_numerica_booleana = True

#  * - Crea una constante.
CONSTANTE = [1, 2, 3]

#  * - Usa un if, else if y else.
if valor == 1:
    print("1")
elif valor == 2:
    print("2")
else:
    print("No es 1 ni 2")

#  * - Crea estructuras como un array, lista, tupla, set y diccionario.
mi_array = ["uno", "dos", "tres", "cuatro"]
mi_lista = ["leche", "pan", "azucar", "agua"]
mi_tupla = (oro, plata)
mi_set = set("azul", "rojo", "amarillo")
mi_diccionario = {
    1:"valor1",
    2:"valor2",
}

#  * - Usa un for, foreach y un while.
for n in mi_lista:
    print(n)

count = 2
while count > 0:
    print("Hello")
    count -= 1

#  * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
def suma():
    resultado = 1 + 2
    return resultado

def suma_parametros(n1, n2):
    resultado = n1 + n2

#  * - Crea una clase.
class Animales:
    patas = 4
    cola = True

    def __init__(self, nombre):
        self.nombre = nombre

#  * - Muestra el control de excepciones.
try:
    resultado = resultado ** 2
except:
    print("Valor incorrecto")


