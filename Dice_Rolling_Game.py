import random

def dice_rolling_game():
    count = 0
    while True:
        NUMBERS = random.randint(1,7)
        user_response = input("Should we roll the dice? (Y/N): ").capitalize()
        if user_response == "Y":
            print(f"You get {NUMBERS}")
            count+=1
        elif user_response=="N":
            break
        else:
            # raise ValueError
            print("Only enter (Y/N)")
    print(f"You played {count} times ")
    print("Game ended")

dice_rolling_game()

    
    
    
    