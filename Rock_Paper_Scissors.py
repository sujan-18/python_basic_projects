import random

def rock_paper_scissor():
    print("Let's begin the game!")

    emojies = {"rock": '🪨', "paper": '📃', "scissor": '✂️'}

    while True:
        round_num = 1
        user_count = 0
        comp_count = 0

        while round_num <= 3:
            comp_choice = random.choice(list(emojies.keys()))
            user_input = input("Enter rock/paper/scissor: ").lower()

            if user_input not in emojies:
                print("Invalid input! Try again.")
                continue

            print(f"Computer chose {emojies[comp_choice]}")

            if user_input == comp_choice:
                print("Round draw!")
            elif (user_input == "paper" and comp_choice == "rock") or \
                 (user_input == "rock" and comp_choice == "scissor") or \
                 (user_input == "scissor" and comp_choice == "paper"):
                print("User wins this round!")
                user_count += 1
            else:
                print("Computer wins this round!")
                comp_count += 1

            round_num += 1

        print("\nFinal Result:")
        if user_count > comp_count:
            print("🏆 User is the winner!")
        elif user_count < comp_count:
            print("💻 Computer is the winner!")
        else:
            print("🤝 The game is a draw!")

        ask = input("Do you want to play again? (Y/N): ").capitalize()
        if ask != "Y":
            print("Game ended. Goodbye!")
            break
