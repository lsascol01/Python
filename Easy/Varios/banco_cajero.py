
# banco_cliente
# cuenta_cliente
# saldo_cliente
# banco_destino
# cuenta_destino
# hora_transferencia= [0,24]

# Trasferir 1M USD

# Condiciones obligatorias de transferencia:
# Cliente verificado (V o F)
# Destino verificado (V o F)
# Saldo mayor al monto a transferir más costo de transacción

# Parametros del costo de transaccion:

# Si el banco destino es el mismo al banco del cliente el costo de la transaccion es 0 USD
# Si el banco destino es diferente al banco del cliente el costo de la transaccion es 100 USD

# Solo se pueden hacer transferencias en hora de 9 a 12 o de 15 a 20



import random


hora=random.randint(0,24)
saldo=random.randint(0,250000)
x="1"
inicio="""
    
    Bienvenidos al ATM Bank of America 
    
    Introduzca su numero de cuenta: 
    
    """
monto_transferencia="""
    

    Ingrese el monto que quiere transferir:

    *Tome en cuenta si el destinatario es un Banco Externo, ya que tendria cargos adicionales
    
    """
banco_transferencia="""
    
    Seleccione el banco del destinatario:

    (1) Bank of America
    (2) Chase Bank
    (3) Wells Fargo
    (4) Otro
    
    """
destinatario_transferencia="""
    
    Inserte el numero de cuenta de destino
    
    """



def run ():

    def verificacion(nombre_bank):
        if nombre_bank== "2":
            nombre_bank = "Chase Bank"
        elif nombre_bank== "3":
            nombre_bank = "Wells Fargo"
        elif nombre_bank== "4":
            nombre_bank = "Banco X"
        print("Su saldo actual es de ", saldo)
        monto=int(input(monto_transferencia))   
        if saldo >= monto + 100:
            cuenta_destino=input(destinatario_transferencia)
            if cuenta_destino == x:
                print("Su transferencia desde su banco a la cuenta de ", nombre_bank , x ,"por un monto de",monto,"fue exitosa\n","Su monto actual ahora es de "  + str(int(saldo - monto)) )
        else:
            print("Insuficiencia de saldo")

    if hora >= 9 and hora <= 12 or hora >= 15 and hora <= 20:
        numero_de_cuenta=input(inicio)
        if numero_de_cuenta == "11111" :
            banco=input(banco_transferencia)
            if banco == "1" :
                print("Su saldo actual es de ", saldo)
                monto=int(input(monto_transferencia))
                cuenta_destino=input(destinatario_transferencia)
                if cuenta_destino == x:
                    print("Su transferencia desde su banco a la cuenta",x ,"por un monto de",monto,"fue exitosa\n","Su monto actual ahora es de "  + str(int(saldo - monto)))
                else:
                    print("ERROR 404")      
            elif banco != "1":
                verificacion(banco)
            else:
                print("ERROR 404")
        else:
            print("Cuenta Invalida")
    else:
        print("El horario de servicio es de 9 AM a 12 PM y de 3 PM a 8 PM " + str(hora) + "hrs")
    


if __name__ == "__main__":
    run()