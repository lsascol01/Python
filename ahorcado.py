import math
from random import randint


WORDS = []
with open("./data.txt", "r", encoding="utf-8") as f:
    for line in f:
        WORDS.append(line.strip())


def upper_case_and_no_accents(word):
    word = word.upper().replace("Á", "A").replace("É", "E").replace(
        "Í", "I").replace("Ó", "O").replace("Ú", "U")
    return word


def letter_by_letter():
    word_chosen =[upper_case_and_no_accents(WORDS[randint(0, len(WORDS))])]
    word_to_guess={a:b for a,b in enumerate(word_chosen[0])}
    print(word_to_guess)
    number_lifes = 8
    print(f"In order to win write a letter of the next word, you only have {number_lifes} lifes\n")
    show = {}
    while number_lifes:
        seleccion = upper_case_and_no_accents(input("Ingrese letra \n "))
        verification = {position: seleccion for position, letter in enumerate(word_chosen[0]) if seleccion == letter}
        show.update(verification)
    
        if show == word_to_guess:
            print("Ganaste\n")
            print(show.values())
            return False
        elif seleccion in show.values():
            print("\n")
        elif show != word_to_guess:
            number_lifes-=1
            if number_lifes > 0:
                print(f"Perdiste una vida te quedan {number_lifes}\n")
            elif number_lifes == 0:
                print("DEFEAT\n")
        print([letter for letter in show.values() ])



def run():
    letter_by_letter()


if __name__ == '__main__':
    while True:
        try:
            menu = """
            Welcome to the ahorcado game,
                1) to start the game
                2) to close the game

                """
            x = int(input(menu))
            if x == 1:
                run()
                decision = input("Gracias por jugar, si quieres jugar denuevo escribe 1 en lo contrario escribe 2 ")
                if decision == "1":
                    continue
                elif decision == "2":
                    print("Gracias por jugar te espero en la proxima")
                    break
            elif x == 2:
                break
            else:
                continue
        except ValueError:
            print("Seleccione una respuesta valida")
