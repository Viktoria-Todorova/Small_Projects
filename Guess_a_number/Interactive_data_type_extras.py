from datetime import datetime


# Prompt the user to choose a data type to perform operations on

print("\033[96m\U0001F40D Choose a data type to perform operations on:\033[0m")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# A loop to allow the user to select different data types in the same session.

while True:
    # Get the user's choice and store it in a variable

    choice = input("'\033[96m\U0001F40D Enter the number of your choice (1-4): \033[0m")

    # Check the user choice and perform the operations

    if choice == '1':
        sentence = "Learning Python is fun!"
        extracted_word = sentence[9:15]
        print(f'\033[35mthe extracted word is \033[0m{extracted_word}')

        uppercase_sentence = sentence.upper()
        print(f"\033[35mConverted sentence to uppercase:\033[0m{uppercase_sentence}")

        new_sentence = sentence.replace("fun", "awesome")
        print(f"\033[35mReplacing a word:\033[0m {new_sentence}")

        # Give the user to chose a word so we can do some operations with it

        word = input("\033[96m\U0001F40D Think of a word and write here:\033[0m")
        reverse_word = word[::-1]
        print(f"\033[35mThe length of the word is:\033[0m{len(word)}")
        print(f"\033[35mReversed word:\033[0m{reverse_word}")
        print(f"\033[35mIs the word with lower case?:\033[0m{reverse_word.islower()}")
        print(f"\033[35mIs the word with upper case?:\033[0m{reverse_word.isupper()}")
        print(f"\033[35mDoes the word start with a vowel?\033[0m {word[0].lower() in 'aeiou'}")
        print(f"\033[35mDoes the word end with a vowel? \033[0m{word[-1].lower() in 'aeiou'}")
        print(f"\033[35mIs the word a palindrome? \033[0m{word == reverse_word}")

        # Calculate the ASCII sum of the word
        final_sum = 0
        for letter in word:
            value_of_letter = ord(letter)
            final_sum += value_of_letter
        print(f"\033[35mThe sum of ASCII values of the word '{word}' is: \033[0m{final_sum}")

        # checks if the characters in the word are unique
        if len(word) == len(set(word)):
            print(f"All characters in '{word}' are unique.")
        else:
            print(f"'{word}' contains duplicate characters.")

        # For loop to count vowels and consonants
        vowels = "aeiouAEIOU"
        vowel_count = 0
        consonant_count = 0

        for letter in word:

            if letter in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

        print(f"\033[35mNumber of vowels:\033[0m {vowel_count}")
        print(f"\033[35mNumber of consonants:\033[0m {consonant_count}")
        print("\033[96m\U0001F40D Lets try something else, answer only with one word:\033[0m")

        name = input("\033[94m\U0001F388 Give me your name:\033[0m")
        city = input("\033[94m\U0001F388 Give me the city you were born:\033[0m")
        color = input("\033[94m\U0001F388 Give me your favorite color:\033[0m")
        movie = input("\033[94m\U0001F388 Give me your favorite movie:\033[0m")
        hobie = input("\033[94m\U0001F388 Give me your number one hobie:\033[0m")

        print(
            f"'\033[4m👤 You are {name} from {city}, "
            f"your favorite color is:{color}, "
            f"your favorite movie is:{movie} "
            f"and your number one hobie is {hobie} 👤\033[0m")

        print("\U0001F40D Let's try some concatenating")
        word1 = input("\033[96mGive me your first word of choice:\033[0m")
        word2 = input("\033[96mGive me your second word of choice:\033[0m")

        final_word = word1 + " " + word2
        print(f"\033[4m🕸The concatenated result is: {final_word}\033[0m")

    elif choice == '2':
        num1 = input("\033[96m\U0001F40D Enter the first number:\033[0m")
        num2 = input("\033[96m\U0001F40D Enter the second number:\033[0m")

        numb1 = int(num1)
        numb2 = int(num2)

        addition = numb1 + numb2
        print(f'\033[35mAddition :\033[0m{addition}')
        subtraction = numb1 - numb2
        print(f'\033[35mSubtraction :\033[0m{subtraction}')
        multiplication = numb1 * numb2
        print(f'\033[35mMultiplication :\033[0m{multiplication}')

        # Handle division by zero

        if numb2 <= 0:
            print("\033[31m division error...\033[0m")
        else:
            division = numb1 / numb2
            print(f'\033[35mDivision :\033[0m{division}')

        raising = numb1 ** numb2
        print(f'\033[35m{numb1} raised to the power of {numb2} is:\033[0m {raising}')

    elif choice == '3':
        # Boolean variables
        is_python_fun = True
        is_sunny = False
        print("\033[3m\U0001F40D We have two boolean variables is_python_fun = True and is_sunny = False."
              "\n We want to check the logical operations AND,OR or NOT\033[0m")

        # Logical operations
        and_result = is_python_fun and is_sunny  # Logical AND
        or_result = is_python_fun or is_sunny  # Logical OR
        not_result = not is_python_fun  # Logical NOT

        print("\033[35mLogical AND to: is_python_fun AND is_sunny:\033[0m", and_result)
        print("\033[35mLogical OR to:is_python_fun OR is_sunny:\033[0m", or_result)
        print("\033[35mLogical NOT to:NOT is_python_fun:\033[0m", not_result)

        # Input numbers for comparison

        first_num = int(input('\033[96m\U0001F40D Give me first number for comparison:\033[0m'))
        second_num = int(input('\033[96m\U0001F40D Give me second number for comparison:\033[0m'))

        # Comparison operations

        bigger_num = first_num > second_num
        smaller_num = first_num < second_num
        even_num = first_num == second_num
        not_equal = first_num != second_num

        print(f"\033[35mIs {first_num} > {second_num} ?:\033[0m", bigger_num)
        print(f"\033[35mIs {first_num} < {second_num} ?:\033[0m", smaller_num)
        print(f"\033[35mIs {first_num} == {second_num} ?:\033[0m", even_num)
        print(f"\033[35mIs {first_num} != {second_num} ?:\033[0m", not_equal)

        if second_num != 0:
            if first_num % second_num == 0:
                print(f"\033[35mIs {first_num} divisible by {second_num}?:\033[0m True")
            elif first_num % second_num != 0:
                print(f"\033[35mIs {first_num} divisible by {second_num}?:\033[0m False")
            else:
                pass

    elif choice == '4':
        print("\033[36m🌸 Working with lists:🌸\033[0m")
        new_list = ["I have", 4, "bananas", True]
        print(f"\033[35mI created a list:\033[0m {new_list}")

        new_list[2] = "apples"
        print(f'\033[35mI changed an element:\033[0m{new_list}')

        print(f"\033[35mThe 4th element in my list is: \033[0m{new_list[3]} ")
        print(f'|')
        print("\033[36m🌸Working with Tuple operations:🌸\033[0m")

        my_first_tuple = ("apple", " dragon fruit", "banana")
        print(f"\033[35mMy Tuple :\033[0m {my_first_tuple}")
        print(f"\033[35mThe length of the tuple is:\033[0m{len(my_first_tuple)}")

        # Try to modify one element in the tuple and handle the resulting TypeError. Once a tuple is created,
        # you cannot change its values. Tuples are unchangeable, or immutable as it also is called. But there is a
        # workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

        make_the_tuple_list = list(my_first_tuple)
        make_the_tuple_list[0] = "tomato"
        my_first_tuple = tuple(make_the_tuple_list)

        print(f"\033[35mChanging an element in the tuple:\033[0m{my_first_tuple}")
        print("|")
        print("\033[36m🌸Working with dictionary:🌸\033[0m")

        # creating the dictionary

        my_first_dictionary = {
            "name": "Viktoria Todorova",
            "city": "Sevlievo",
            "age": 25
        }

        print(f"\033[35mI created my dictionary:\033[0m{my_first_dictionary}")  # printing the created dictionary
        age_value = my_first_dictionary["age"]  # accessing the age value
        print(f"\033[35mThe age value is:\033[0m {age_value}")
        my_first_dictionary.update(
            {"favorite color": "purple"})  # adding one more key and value to the dictionary and printing it
        print(f"\033[35mUpdated dictionary:\033[0m {my_first_dictionary}")

        #   printing the keys and the values in the dictionary using loop

        print("\033[35mThe keys in my dictionary are:\033[0m")
        for key in my_first_dictionary.keys():
            print(key)
        print("\033[35mThe values in my dictionary are:\033[0m")
        for value in my_first_dictionary.values():
            print(value)

    # If the user enters an invalid choice
    else:
        raise SystemExit("Invalid Input, Try again..")

    # Give the user the choice if they want to continue checking the operations

    user_choice = input("\033[30;46m\U0001F40D Do you want to try the other variants[yes]/[no]?:\033[0m")

    # if the user does not want it we greet them by using the current time so it's more personal and stop the loop
    if user_choice == "no":
        current_hour = datetime.now().hour
        if 18 <= current_hour < 22:
            greeting = "Good evening👽!"
        elif 22 <= current_hour or current_hour < 6:
            greeting = "Good night💤!"
        else:
            greeting = "Bye👋!"
        print(f"\033[36;40m I hope you enjoyed the interactive data type journey, {greeting}\033[0m")
        break
    elif user_choice != "no" and user_choice != "yes":
        raise SystemExit("Invalid Input, Try again..")
