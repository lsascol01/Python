
def run():
    user_name1=input("Write your name: ")
    user_age1=int(input("Enter your age: "))
    user_name2=input("Write the other name:")
    user_age2=int(input("Enter your age: "))
    if user_age1 > user_age2:
        print(f"{user_name1} is older than {user_name2}")
    elif user_age1 < user_age2:
        print(f"{user_name2} is older than {user_name1}")
    else:
        print(f"{user_name1} has the same age {user_name2}")  

if __name__ == "__main__":

    run()