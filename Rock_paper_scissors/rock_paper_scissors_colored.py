import random  # it generates random numbers or making random choices

rock = 'Rock \U0001F44A'
paper = 'Paper \U0001F4C3'
scissors = 'Scissors \U00002702'

count_comp_wins = 0
count_mine_wins = 0
count_comp_loses = 0
count_mine_loses = 0

# i created a loop so it can be played as much as the player wants
while True:
    # giving the player to chose one of the 3 choices
    player_move = input("\033[35;40mChoose [r]ock, [p]aper, or [s]cissors: \033[0m")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit(
            "\033[31;40m \u26A0 Invalid Input, Try again..\033[0m")  # raise an exception and exit the program

    computer_random = random.randint(1, 3)  # is used to generate a random integer within a specific range
    computer_move = ""
    # assign values to the random numbers we generated
    if computer_random == 1:
        computer_move = rock
    elif computer_random == 2:
        computer_move = paper
    elif computer_random == 3:
        computer_move = scissors

    print(f"\033[35;40mThe computer chose {computer_move}.\033[0m")
    # checking the probabilities for win/lose or draw
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        count_mine_wins += 1
        count_comp_loses += 1
        print("\033[32;40mYou win \U0001F389 \033[0m")
    elif player_move == computer_move:
        print("\033[34;40m Draw!\U0001F600 \033[0m")
    else:
        count_comp_wins += 1
        count_mine_loses += 1
        print("\033[31;40m \U0001F63F You lose! \U0001F63F \033[0m")

    want_more = input("\033[1;35;40m \U0001F525 Do you want to play again? \U0001F525 [yes/no]: \033[0m")
    # if the player wants to stop the game we give him the choice to stop it and give a result from the game
    if want_more == 'no':

        if count_mine_wins > count_comp_wins:
            print('\033[1;35;40m It was a good game!!!!\U00002764 \033[0m')
            print(f"\033[32;40mYou won the computer with {count_mine_wins} wins and {count_mine_loses} loses\033[0m")
            break
        elif count_mine_wins < count_comp_wins:
            print('\033[1;35;40m It was a good game, but unfortunately you lose!!!!\U00002764 \033[0m')
            print(f"\033[31;40m The computer won with {count_comp_wins} wins and {count_comp_loses} loses \033[0m")
        break
        # the program checks the posibility of the player to chose something different from yes or no
    elif want_more != "no" and want_more != "yes":
        raise SystemExit("\033[31;40m \u26A0 Invalid Input, Try again..\033[0m")
