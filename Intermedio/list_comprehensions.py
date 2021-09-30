def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         squares.append(i**2)
    # print(squares)
    # square=[i**2 for i in range (1,101) if i%3 != 0 ]
    # print(square)
    challenge=[i for i in range(1,100001) if i %36 == 0]
    print(challenge)
if __name__ == "__main__":
    run()
