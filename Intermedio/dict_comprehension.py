def run():
    # my_dict={}
    # for i in range(1,101):
    #     my_dict[i]= i**3
    # print (my_dict)   
    # my_dict={i:round(i**0.5,4) for i in range(1,101) if i % 2 == 0}
    # print(my_dict)
    my_dict={i:round(i**3,4) for i in range(1,101)}
    print(my_dict)
if __name__ == "__main__":
    run()