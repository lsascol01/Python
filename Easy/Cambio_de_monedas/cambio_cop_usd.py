
def exchanges(moneda,cantidad):
 result = 0
 cantidad = cantidad
 def moneda_a_dolares():
     result= str(round(cantidad/tasa,2))
 def dolares_a_moneda():
     x= str(round(cantidad*tasa,2))
    # Moneda chilena
 if moneda == 1:
        result = cantidad * 0.0013
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dolares')
    # Moneda colombiana
 elif moneda == 2:
    p=int(input("Desea cambiar de COP a USD (Opción 1) o de USD a COP (Opción 2): " ))
    tasa=3900
    if p == 1:
         result=str(round(cantidad/tasa,2))
         print(f'Los {cantidad} pesos colombianos equivalen a {result} dolares')
    if p == 2:
         result=dolares_a_moneda()
         print(f'Los {cantidad} dolares equivalen a {result} pesos colombianos')

      # Moneda Argentina
 elif moneda == 3:
     result = cantidad * 0.014
     print(f'Los {cantidad} pesos argentinos equivalen a {result} dolares')
    # Moneda mexicana
 elif moneda == 4:
        result = cantidad * 0.044
        print(f'Los {cantidad} pesos mexicanos equivalen a {result} dolares')



if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertira  dolar:
            [1] Moneda chilena 
            [2] Moneda colombiana 
            [3] Moneda argentida 
            [4] Moneda mexicana 
        Selecciona: '''))
        print('********************************')
        cantidad = int(input('Ingresa la cantidad que quieres convertir: '))
        exchanges(moneda,cantidad)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')
