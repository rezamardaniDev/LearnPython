while True:
    try:
        user_input = int(input("please enter your age: "))
        break
    # if user_input is valid, return user_input
    except:
        print("your input is invalid try again")
        # if user_input is invalid , ask again with error message


print(f"your name is {user_input}")