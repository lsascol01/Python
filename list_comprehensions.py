# def run():
#     squares=[i for i in range(1,10001) if i % 4 ==0 and i % 6 ==0 and i % 9 ==0]
#     print(squares)

# if __name__ == "__main__":
#     run()

# def run():
#     cubic={}
#     for i in range(1,101):
#         cubic[i]= i**3
#     print(cubic)
# if __name__ == "__main__":
#     run()

# def run():
#     cubic={}
#     for i in range(1,101):
#         if i % 3 !=0:
#             cubic[i]= i**3
#     print(cubic)
# if __name__ == "__main__":
#     run()

# def run():
#     cubic={i:i**3 for i in range (1,101) if i%3 !=0}
#     print(cubic)

# if __name__ == "__main__":
#     run()

def run():
    square_roots={i:i**(1/2) for i in range (1,1001)}
    print(square_roots)

if __name__ == "__main__":
    run()