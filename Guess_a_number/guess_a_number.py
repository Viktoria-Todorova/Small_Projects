import random
random_choice = random.randint(1,100)

while True:
    player_input = input("Guess the number between 1 and 100:")

    if not player_input.isdigit():
        print("Invalid input. Try again..")
        continue
    player_number = int(player_input)

    if random_choice == player_number:
        print("You guess it")
        break
    elif random_choice > player_number:
        print("Too low!")
    else:
        print("To high")