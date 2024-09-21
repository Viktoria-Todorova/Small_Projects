from datetime import datetime

# Prompt the user to choose a data type to perform operations on

print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# A loop to allow the user to select different data types in the same session.

while True:
    # Get the user's choice and store it in a variable

    choice = input("Enter the number of your choice (1-4): ")

    # Check the user choice and perform the operations

    if choice == '1':
        sentence = "Learning Python is fun!"
        extracted_word = sentence[9:15]
        print(f'the extracted word is {extracted_word}')

        uppercase_sentence = sentence.upper()
        print(f"Converted sentence to uppercase:{uppercase_sentence}")

        new_sentence = sentence.replace("fun", "awesome")
        print(f"Replacing a word: {new_sentence}")

        # Give the user to chose a word so we can do some operations with it

        word = input("Think of a word and write here:")
        reverse_word = word[::-1]
        print(f"The length of the word is:{len(word)}")
        print(f"Reversed word:{reverse_word}")
        print(f"Is the word with lower case?:{reverse_word.islower()}")
        print(f"Is the word with upper case?:{reverse_word.isupper()}")
        print(f"Does the word start with a vowel? {word[0].lower() in 'aeiou'}")
        print(f"Does the word end with a vowel? {word[-1].lower() in 'aeiou'}")
        print(f"Is the word a palindrome? {word == reverse_word}")

        # Calculate the ASCII sum of the word
        final_sum = 0
        for letter in word:
            value_of_letter = ord(letter)
            final_sum += value_of_letter
        print(f"The sum of ASCII values of the word '{word}' is: {final_sum}")

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

        print(f"Number of vowels: {vowel_count}")
        print(f"Number of consonants: {consonant_count}")
        
        print("Lets try something else, answer only with one word:")
        
        name = input("Give me your name:")
        city = input("Give me the city you were born:")
        color = input("Give me your favorite color:")
        movie = input("Give me your favorite movie:")
        hobie = input("Give me your number one hobie:")
        
        print(
            f"You are {name} from {city}, "
            f"your favorite color is:{color}, "
            f"your favorite movie is:{movie} "
            f"and your number one hobie is {hobie}")
        
        print("Let's try some concatenating")
        word1 = input("Give me your first word of choice:")
        word2 = input("Give me your second word of choice:")

        final_word = word1 + " " + word2
        print(f"The concatenated result is: {final_word}")

    elif choice == '2':
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")

        numb1 = int(num1)
        numb2 = int(num2)

        addition = numb1 + numb2
        print(f'Addition :{addition}')
        subtraction = numb1 - numb2
        print(f'Subtraction :{subtraction}')
        multiplication = numb1 * numb2
        print(f'Multiplication :{multiplication}')

        # Handle division by zero

        if numb2 <= 0:
            print("division error")
        else:
            division = numb1 / numb2
            print(f'Division :{division}')

        raising = numb1 ** numb2
        print(f'{numb1} raised to the power of {numb2} is: {raising}')

    elif choice == '3':
        # Boolean variables
        is_python_fun = True
        is_sunny = False
        print("We have two boolean variables is_python_fun = True and is_sunny = False."
              "\n We want to check the logical operations AND,OR or NOT")

        # Logical operations
        and_result = is_python_fun and is_sunny  # Logical AND
        or_result = is_python_fun or is_sunny  # Logical OR
        not_result = not is_python_fun  # Logical NOT

        print("Logical AND to: is_python_fun AND is_sunny:", and_result)
        print("Logical OR to:is_python_fun OR is_sunny:", or_result)
        print("Logical NOT to:NOT is_python_fun:", not_result)

        # Input numbers for comparison

        first_num = int(input('Give me first number for comparison:'))
        second_num = int(input('Give me second number for comparison:'))

        # Comparison operations

        bigger_num = first_num > second_num
        smaller_num = first_num < second_num
        even_num = first_num == second_num
        not_equal = first_num != second_num

        print(f"Is {first_num} > {second_num} ?:", bigger_num)
        print(f"Is {first_num} < {second_num} ?:", smaller_num)
        print(f"Is {first_num} == {second_num} ?:", even_num)
        print(f"Is {first_num} != {second_num} ?:", not_equal)

        if second_num != 0:
            if first_num % second_num == 0:
                print(f"Is {first_num} divisible by {second_num}?: True")
            elif first_num % second_num != 0:
                print(f"Is {first_num} divisible by {second_num}?: False")
            else:
                pass

    elif choice == '4':
        print("Working with lists:")
        new_list = ["I have", 4, "bananas", True]
        print(f"I created a list: {new_list}")

        new_list[2] = "apples"
        print(f'I changed an element:{new_list}')

        print(f"The 4th element in my list is: {new_list[3]} ")
        print(f'|')
        print("Working with Tuple operations:")

        my_first_tuple = ("apple", " dragon fruit", "banana")
        print(f"My Tuple : {my_first_tuple}")
        print(f"The length of the tuple is:{len(my_first_tuple)}")

        # Try to modify one element in the tuple and handle the resulting TypeError. Once a tuple is created,
        # you cannot change its values. Tuples are unchangeable, or immutable as it also is called. But there is a
        # workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

        make_the_tuple_list = list(my_first_tuple)
        make_the_tuple_list[0] = "tomato"
        my_first_tuple = tuple(make_the_tuple_list)

        print(f"Changing an element in the tuple:{my_first_tuple}")
        print("|")
        print("Working with dictionary:")

        # creating the dictionary

        my_first_dictionary = {
            "name": "Viktoria Todorova",
            "city": "Sevlievo",
            "age": 25
        }

        print(f"I created my dictionary:{my_first_dictionary}")  # printing the created dictionary
        age_value = my_first_dictionary["age"]  # accessing the age value
        print(f"The age value is: {age_value}")
        my_first_dictionary.update(
            {"favorite color": "purple"})  # adding one more key and value to the dictionary and printing it
        print(f"Updated dictionary: {my_first_dictionary}")

        #   printing the keys and the values in the dictionary using loop

        print("The keys in my dictionary are:")
        for key in my_first_dictionary.keys():
            print(key)
        print("The values in my dictionary are:")
        for value in my_first_dictionary.values():
            print(value)

    # If the user enters an invalid choice
    else:
        raise SystemExit("Invalid Input, Try again..")

    # Give the user the choice if they want to continue checking the operations

    user_choice = input("Do you want to try the other variants[yes]/[no]?:")

    # if the user does not want it we greet them by using the current time so it's more personal and stop the loop
    if user_choice == "no":
        current_hour = datetime.now().hour
        if 18 <= current_hour < 22:
            greeting = "Good evening"
        elif 22 <= current_hour or current_hour < 6:
            greeting = "Good night"
        else:
            greeting = "Bye!"
        print(f"I hope you enjoyed the journey {greeting}!")
        break
    elif user_choice != "no" and user_choice != "yes":
        raise SystemExit("Invalid Input, Try again..")
