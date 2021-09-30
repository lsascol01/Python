# def potenciación(repeticiones):
#     numero = int(input("Escribe un numero para saber sus potencias: "))
#     potencia = int(input("Cuantas potencias del número seleccionado quieres:"))
#     while repeticiones < potencia:
#         resultado = numero **repeticiones
#         print(resultado)
#         repeticiones +=1


# if __name__ == "__main__":
#     potenciación(0)


def run():
    LIMITE= 1000
    contador= 0
    potencia_2= 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador +=1
        potencia_2= 2**contador



if __name__ == "__main__":
    run()