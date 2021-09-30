def run():
    texto= input("Introduce un texto: ")
    for letra in texto:
        if letra == ("o"):
            break
        print(letra)
    # for i in range(100):
    #     print(i)
    #     if i == 20:
    #         break
#     for contador in range(2, 100):
#         if contador % 2 != 0:
#             continue
#         else:
#             print(contador)


if __name__ == "__main__":
    run()
