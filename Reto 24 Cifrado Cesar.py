# /*
#  * Crea un programa que realize el cifrado César de un texto y lo imprima.
#  * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#  *
#  * Te recomiendo que busques información para conocer en profundidad cómo
#  * realizar el cifrado. Esto también forma parte del reto.
#  */

def cesar_encrypter(text, key):
    secret_mesage = ""

    for letter in text:
        ascii_position = ord(letter) + key
        encrypted_char = chr(ascii_position)
        secret_mesage += encrypted_char
    return secret_mesage

def cesar_decrypter(text, key):
    original_mesage = ""

    for letter in text:
        ascii_position = ord(letter) - key
        decrypted_char = chr(ascii_position)
        original_mesage += decrypted_char
    return original_mesage


text = "Hola mundo"
key = 3
secret_message = cesar_encrypter(text, key)
print("Mensaje encriptado: {}".format(secret_message))
public_message = cesar_decrypter(secret_message, key)
print("Mensaje desencriptado: {}".format(public_message))


