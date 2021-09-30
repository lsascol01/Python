def run():
    def divisors(number):
        divisores=[]
        for i in range(1,number+1):
            if number % i == 0:
                divisores.append(i)
        return divisores
    num=int(input("Elija un numero"))
    print(divisors(num))
if __name__ == "__main__":
    run()