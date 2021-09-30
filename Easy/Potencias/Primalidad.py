def es_primo(numero):
    contador = 0
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
            break
    if contador == 0 and numero != 1:
        return True
    else:
        return False


def run():
    numero = int(input("Introduce un numero para conocer si es primo: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()

# def es_primo(numero):
#     if numero == 1:
#         returnFalse
#     else:
#         contador = 0
#     for i in range(1 , numero+1):
#         if i == 1or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         returnTrue
#     else:
#         returnFalse


# def run():
#     numero = int(input("Escribe un número: "))
#     if es_primo(numero):
#         print(str(numero) + " es primo")
#     else:
#         print(str(numero) +  " NO es primo")


# if __name__ == "__main__":
#     run()