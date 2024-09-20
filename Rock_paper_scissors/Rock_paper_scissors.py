import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

count_comp_wins = 0
count_mine_wins = 0
count_comp_loses = 0
count_mine_loses = 0

while True:
    player_move = input("Choose [r]ock, [p]aper, or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print(colored("Invalid Input, Try again.."))
        continue

    computer_random = random.randint(1, 3)
    computer_move = ""
    if computer_random == 1:
        computer_move = rock
    elif computer_random == 2:
        computer_move = paper
    elif computer_random == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
       (player_move == paper and computer_move == rock) or \
       (player_move == scissors and computer_move == paper):
        count_mine_wins += 1
        count_comp_loses += 1
        print("You win!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        count_comp_wins += 1
        count_mine_loses += 1
        print("You lose!")

    want_more = input("Do you want to play again? [yes/no]: ")

    if want_more == 'no':
        if count_mine_wins > count_comp_wins:
            print('It was a good game!')
            print(f"You won with {count_mine_wins} wins and {count_mine_loses} losses")
        elif count_mine_wins < count_comp_wins:
            print('It was a good game, but unfortunately you lost!')
            print(f"The computer won with {count_comp_wins} wins and {count_comp_loses} losses")
        break
    elif want_more != "yes":
        print("Invalid Input, Try again..")
