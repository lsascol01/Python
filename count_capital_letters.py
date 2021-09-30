def run():

    # result=list(filter(lambda x: x.isupper(), word))
    # result= len(result)
    # print(result)
    # word= word.lower().replace(" ", "")
    # if word == word[::-1]:
    #     print("True")
    # else:
    #     print("False")
    # y=lambda word:word.lower().replace(" ", "") == word[::-1]word.lower().replace(" ", "")
    # print(y("ana"))
    test_str = 'GeeKsFoRGEEks'
  
    # printing original string
    print("The original string is : " + str(test_str))
    
    # Uppercase check using isupper()
    res = [idx for idx in range(len(test_str)) if test_str[idx].isupper()]
    
    # printing result 
    print("Uppercase elements indices : " + str(res)) 
if __name__ == "__main__":
    run()

