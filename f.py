def division(n):
	if n < 0:
		raise Exception("No se pueden seleccionar numeros negativos")
	elif n == 0:
		raise Exception("No se permite el numero cero")

	divisors=[i for i in range(1,n+1) if n % i == 0]
	# for i in range(1,n+1):
	# 	if n % i == 0 :
	# 		divisors.append(i)
	return divisors

def run():
	while True:
		try:
			selection=int(input("Write down a number: "))
			print(division(selection))
			return False
		except ValueError:
			print("Solo numeros permitidos")
		except Exception as ex:
			print(ex)



if __name__ == "__main__":
    run()
