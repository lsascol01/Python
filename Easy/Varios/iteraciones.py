def run():
    formato_hora= int(input("Desea el reloj en formato de 12 o 24 horas: \n 1) 12 horas \n 2) 24 horas \n "))
    contador_hora = 0
    contador_minuto = 0
    contador_segundo = 0
    if formato_hora == 1:
        rango= 12
    else:
        rango = 24
    while contador_hora <= rango:
        while contador_minuto < 60:
            while contador_segundo < 60:
                print(contador_hora, ":", contador_minuto, ",", contador_segundo)
                contador_segundo += 1
            contador_minuto += 1
            contador_segundo = 0
        contador_hora += 1
        contador_minuto = 0


if __name__ == "__main__":
    run()
