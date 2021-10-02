
def fibonacci_sequence(lenght):
    # first_number=1
    # second_number=0

    # show=[1]
    # while len(show) <= lenght:
    #     first_number =show[-1]
    #     element=first_number+second_number
    #     show.append(element)
    #     second_number = show[-2]
    # print(show)
    # return numbers[i for i in len(lenght) 
    second=0
    for i in range(1,lenght+1):
        first= i
        second= i+i

        print(second,first)

if __name__ == "__main__":
    fibonacci_sequence(11)




    
