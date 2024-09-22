import random  # The random module is imported to generate random numbers.

# Variables are initialized: levels keeps track of the current level, random_choice stores the number to guess,
# level_won counts the levels won, and flag is used to check if the player has run out of attempts.

levels = 0
random_choice = random.randint(1, 100)
level_won = 0
flag = False
# The game consists of up to 10 levels, where a new random number is generated for each level within a range of 1 to
# 100 times the current level number, and players have a maximum of 8 attempts to guess the number.

while levels < 10:
    levels += 1
    random_choice = random.randint(1, (levels * 100))
    tries = 0
    max_tries = 8

    print(f"\033[40;36mLevel {levels}:Guess the number between 1 and {levels * 100}\033[0m")

    # The player is prompted to start the level. If they choose "no", the game thanks them and exits.

    player_choice = input(f"\033[36mDo you want to start level {levels}? "
                          f"Type [yes] for the game to start and [no] for the game to stop:\033[0m")

    if player_choice.lower() == "no":
        print(f"Thanks for playing! You played {level_won} levels.")
        break
    # The player is repeatedly asked to guess the number until they either guess correctly or exhaust their attempts.
    while True:

        player_input = input(f"\033[40;36mGuess the number:\033[0m")

        if not player_input.isdigit():  # If the input is not a digit, the player is prompted to try again.
            print("\033[41mInvalid input. Try again..\033[0m")
            continue
        player_number = int(player_input)
        tries += 1
        # The program checks if the guessed number is correct, too low, or too high and provides feedback.

        if random_choice == player_number:
            print(f"\033[36mYou guess it with {tries} tries!!!!\033[0m")
            level_won += 1
            break
        elif random_choice > player_number:
            print("Too low!")

        else:
            print("To high")

        # After 3 incorrect guesses, a hint is provided indicating whether the number is even or odd.

        if tries == 3:
            if random_choice % 2 == 0:
                print("\033[30;46mHint: The number is even.\033[0m")
            else:
                print("\033[30;46mHint: The number is odd.\033[0m")

        if tries == max_tries:
            flag = True  # If the player exhausts all attempts, flag is set to True, and the loop breaks.
            break
    if flag:  # If the player runs out of attempts, a message is displayed with the correct number, and the game ends.
        print(f"Sorry, you've used all your tries! The number was {random_choice}.")
        break
