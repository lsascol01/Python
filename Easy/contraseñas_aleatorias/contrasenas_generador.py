import string
import random
from typing import Match
MAYUS = list(string.ascii_uppercase)
MINUS = list(string.ascii_lowercase)
NUMS = list(string.digits)
CHARS = list(string.punctuation)


def generar_contrasena():
    caracteres = MAYUS + MINUS + NUMS + CHARS
    contrasena = []

    for i in range(15):
        caracter_random= random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es:" , contrasena)


if __name__ == "__main__":
    run()