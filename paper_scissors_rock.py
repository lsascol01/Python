from random import randint
import os
def win():
    print("""
                            ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
                            ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
                            ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
                            ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                            ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                             ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
   .g8MMMbgd       db      `7MN.   `7MF'    db       .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
.dP'     `M      ;MM:       MMN.    M      ;MM:     ,MI    "Y P'   MM   `7   MM    `7  
dM'       `     ,V^MM.      M YMb   M     ,V^MM.    `MMb.          MM        MM   d    
MM             ,M  `MM      M  `MN. M    ,M  `MM      `YMMNq.      MM        MMmmMM    
MM.    `7MMF'  AbmmmqMA     M   `MM.M    AbmmmqMA   .     `MM      MM        MM   Y  , 
`Mb.     MM   A'     VML    M     YMM   A'     VML  Mb     dM      MM        MM     ,M 
  `"bmmmdPY .AMA.   .AMMA..JML.    YM .AMA.   .AMMA.P"Ybmmd"     .JMML.    .JMMmmmmMMM   
---------------------------------------------------------------------------------------""") 

def lose():
    lose = input("""
                    ⠄⢀⣀⣤⣴⣶⣶⣤⣄⡀⠄⠄⣀⣤⣤⣤⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣴⣏⣹⣿⠿⠿⠿⠿⢿⣿⣄⢿⣿⣿⣿⣿⣿⣋⣷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⢟⣩⣶⣾⣿⣿⣿⣶⣮⣭⡂⢛⣭⣭⣭⣭⣭⣍⣛⣂⡀⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⣿⣿⣿⡿⢟⣫⣭⣷⣶⣾⣭⣼⡻⢛⣛⣭⣭⣶⣶⣬⣭⣅⡀⠄⠄⠄⠄⠄⠄
                    ⣿⡿⢏⣵⣾⣿⣿⣿⡿⢉⡉⠙⢿⣇⢻⣿⣿⣿⣿⡟⠉⠉⢻⡷⠄⠄⠄⠄⠄⠄
                    ⣿⣷⣾⣍⣛⢿⣿⣿⣿⣤⣁⣤⣿⢏⠸⣿⣿⣿⣿⣷⣬⣥⣾⠁⣿⣿⣷⠄⠄⠄
                    ⣿⣿⣿⣿⣭⣕⣒⠿⠭⠭⠭⡷⢖⣫⣶⣶⣬⣭⣭⣭⣭⣥⡶⢣⣿⣿⣿⠄⠄⠄
                    ⣿⣿⣿⣿⣿⣿⣿⡿⣟⣛⣭⣾⣿⣿⣿⣝⡛⣿⢟⣛⣛⣁⣀⣸⣿⣿⣿⣀⣀⣀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                    ⣿⡿⢛⣛⣛⣛⣙⣛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣭⣭⠽⣛⢻⣿⣿⣿⠛⠛⠛
                    ⣿⢰⣿⣿⣿⣿⣟⣛⣛⣶⠶⠶⠶⣦⣭⣭⣭⣭⣶⡶⠶⣾⠟⢸⣿⣿⣿⠄⠄⠄
                    ⡻⢮⣭⣭⣭⣭⣉⣛⣛⡻⠿⠿⠷⠶⠶⠶⠶⣶⣶⣾⣿⠟⢣⣬⣛⡻⢱⣇⠄⠄
                    ⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠶⠒⠄⠄⠄⢸⣿⢟⣫⡥⡆⠄⠄
                    ⢭⣭⣝⣛⣛⣛⣛⣛⣛⣛⣿⣿⡿⢛⣋⡉⠁⠄⠄⠄⠄⠄⢸⣿⢸⣿⣧⡅⠄⠄
                    ⣶⣶⣶⣭⣭⣭⣭⣭⣭⣵⣶⣶⣶⣿⣿⣿⣦⡀⠄⠄⠄⠄⠈⠡⣿⣿⡯⠁⠄⠄
`7MMMMMMq.`7MMMMMYMM  `7MMMMMMMq.  `7MMMMMYb.`7MMF' .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
  MM   `MM. MM    `7    MM   `MM.   MM    `Yb. MM  ,MI    "Y P'   MM   `7   MM    `7  
  MM   ,M9  MM   d      MM   ,M9    MM     `Mb MM  `MMb.          MM        MM   d    
  MMmmdM9   MMmmMM      MMmmdM9     MM      MM MM    `YMMNq.      MM        MMmmMM    
  MM        MM   Y  ,   MM  YM.     MM     ,MP MM  .     `MM      MM        MM   Y  , 
  MM        MM     ,M   MM   `Mb.   MM    ,dP' MM  Mb     dM      MM        MM     ,M 
.JMML.    .JMMmmmmMMM .JMML. .JMM..JMMmmmdP' .JMML.P"Ybmmd"     .JMML.    .JMMmmmmMMM 
_____________________________________________________________________________________""")



def mensaje_ganar(ganador):
    print(f"Ronda ganada por el {ganador}")

def run():
    while True:
        wins_maquina=0
        wins_persona=0
        while wins_maquina < 3 and wins_persona < 3:
            seleccion_maquina= randint(1,3)
            seleccion_persona= int(input("Selecciona 1) Papel 2) Tijera 3) Piedra"))
            if seleccion_maquina == seleccion_persona:
                print("Empataste")
            elif seleccion_maquina == 1 and seleccion_persona == 2 :
                mensaje_ganar("persone")
                wins_persona +=1
            elif seleccion_persona == 1 and seleccion_maquina == 2 :
                mensaje_ganar("persone")
                wins_persona +=1
            elif seleccion_maquina == 3 and seleccion_persona == 2:
                mensaje_ganar("maquina")
                print(wins_maquina)
                wins_maquina +=1
                print(wins_maquina)
            elif seleccion_persona == 3 and seleccion_maquina == 2 :
                mensaje_ganar("persone")
                wins_persona +=1
            elif seleccion_maquina == 1 and seleccion_persona == 3:
                mensaje_ganar("maquina")
                wins_maquina +=1
            elif seleccion_persona == 1 and seleccion_maquina == 3 :
                mensaje_ganar("persone")
                wins_persona +=1
        if wins_maquina == 3:
            print(lose())
        elif wins_persona == 3:
            print(win())
    



if __name__ == "__main__":
    while True: 
        welcome="""
Mentira bro era una bromis

Bienvenido al juego de piedra papel y tijera

1) Para empezar a jugar contra la maquina
2) Cerrar el juego
 
    
    """
        print(lose())
        x=input(welcome)
        print(x)
        if x == "1":
            run()
        if x == "2":
            print("No seas puto")
