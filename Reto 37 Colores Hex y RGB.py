# /*
#  * Crea las funciones capaces de transformar colores HEX
#  * a RGB y viceversa.
#  * Ejemplos:
#  * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#  * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#  */

def rgb_to_hex(r, g, b):
    return print('#{:02x}{:02x}{:02x}'.format(r, g, b))


def hex_to_rgb(hex_value):
    h = hex_value.strip("#")
    rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return print(rgb)


if __name__ == '__main__':
    rgb_to_hex(255, 00, 255)
    hex_to_rgb("#ffffff")
