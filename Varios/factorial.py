from functools import reduce


def factorial(number):
    # last_factorial=1
    # for i in range(1,number+1):
    #     print(f"El factorial de {i}! es {i*last_factorial}")
    #     last_factorial=i*last_factorial

    # factorials_funtcion= reduce(lambda number1,number2: number1 * number2, range(1,number+1))
    # return(f"El factorial de {number}! es: {factorials_funtcion}")
    
    # if number == 1:
    #     return 1
    
    # return number *(factorial(number-1))

    return reduce(lambda x,y: x*y,range(1,number+1))


def run():
    number_chosen=int(input("Type a number: "))
    print(factorial(number_chosen))
    
if __name__ == "__main__":
    run()