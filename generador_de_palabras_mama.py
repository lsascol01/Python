def words_creation(list):
    lenght= len(list)
    print(lenght)
    number_of_letters=2
    while number_of_letters <= lenght:
        for i in list:
            show=[]
            show.append(i)
            for i in list:
                show=[]
                show.append(i)
                for i in list:
                    show=[]
                    show.append(i)
            print(show)
        number_of_letters += 1




def run():
    letters=["T","B","C","A","E","O"]
    words_creation(letters)

if __name__ == "__main__":
    run()

