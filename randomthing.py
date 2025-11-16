while True:
    user_data = input("Enter a two-digit number: ")
    if user_data.isdigit():
        if len(user_data) == 2:
            number = int(user_data)
            print("Valid input!")
            break
        else:
            print("Input must be exactly two digits long.")
    else:
        print("Enter a number! Not a letter! Try again...")