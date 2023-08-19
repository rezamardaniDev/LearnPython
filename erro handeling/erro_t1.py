while True:
    try:
        user_input = int(input("please enter your age: "))
        break
    except:
        print("your input is invalid try again")


print(f"your name is {user_input}")