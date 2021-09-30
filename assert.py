def division(n):

    divisors=[i for i in range(1,n+1) if n % i == 0]
	# for i in range(1,n+1):
	# 	if n % i == 0 :
	# 		divisors.append(i)
    return divisors


def run():
    num=input("Write down a number: ")
    # El metodo is numeric evalua si es negativo tambien
    assert num.isnumeric() ,"Debes ingresar un numero"
    assert num == 0,"Debe ser un numero mayor a 0"
    print(division(int(num)))
    




if __name__ == "__main__":
    run()
