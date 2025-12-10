import random

while True:
    attempt = 1
    round_num = 1

    while round_num <= 3:
        RANDOM = random.randint(1, 100)

        try:
            user_input = int(input("Enter any number between 1 & 100: "))
        except ValueError:
            print("Please enter numbers only!")
            continue

        #  First handle INVALID inputs
        if user_input < 1 or user_input > 100:
            print("Number should be between 1 and 100!")
            continue

        #  Compare user input with random number
        if user_input == RANDOM:
            print(f" Correct! You guessed it in {attempt} attempts.")
        elif user_input > RANDOM:
            difference = user_input - RANDOM
            if difference >= 15:
                print("Too high!")
            else:
                print("Closer!")
        else:  # user_input < RANDOM
            difference = RANDOM - user_input
            if difference >= 15:
                print("Too low!")
            else:
                print("Closer!")

        attempt += 1
        round_num += 1

    # Ask user if they want to continue
    ask_user = input("Do you want to continue? [Y/N]: ").capitalize()
    if ask_user != "Y":
        print("Game ended!")
        break
