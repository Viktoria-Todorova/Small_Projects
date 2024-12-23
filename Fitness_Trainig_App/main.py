from user import Person  # Importing the Person class to manage user information
from workout import Workout  # Importing the Workout class to create and manage workouts
from exercise import Exercise, exercises_dict  # Importing Exercise class and exercise dictionary
from progress import ProgressTracker  # Importing ProgressTracker class to track workout progress


# Function to Initialize Users
def initialize_users():
    users = {
        "Alice": Person("Alice", 30, 65, 165, "Lose weight"),  # Creating a user 'Alice'
        "Bob": Person("Bob", 25, 75, 180, "Build muscle"),  # Creating a user 'Bob'
        "Charlie": Person("Charlie", 35, 85, 170, "Improve endurance"),  # Creating a user 'Charlie'
        "Diana": Person("Diana", 28, 60, 160, "Tone muscles"),  # Creating a user 'Diana'
        "Eve": Person("Eve", 40, 70, 155, "Maintain health"),  # Creating a user 'Eve'
        "Frank": Person("Frank", 22, 80, 185, "Increase flexibility"),  # Creating a user 'Frank'
        "Grace": Person("Grace", 27, 55, 165, "Lose weight"),  # Creating a user 'Grace'
        "Henry": Person("Henry", 33, 95, 190, "Bulk up"),  # Creating a user 'Henry'
        "Isabella": Person("Isabella", 26, 62, 168, "Run a marathon"),  # Creating a user 'Isabella'
        "Jack": Person("Jack", 45, 90, 175, "Strength training"),  # Creating a user 'Jack'
    }

    # Adding predefined workout histories for some users
    users["Alice"].workout_history = [  # Adding workout history for 'Alice'
        "Running 5km on 2024-12-15",  # Alice's workout
        "Push-up workout (3 sets of 15) on 2024-12-16"  # Alice's workout
    ]
    # You would repeat this for other users if needed...

    return users  # Returning the dictionary of users


# Initialize users
users = initialize_users()  # Calling the function to initialize users


# Menu system
def display_menu():
    print("\n--- Fitness Tracker ---")  # Printing the menu header
    print("1. Add a new user")  # Option to add a new user
    print("2. Log a workout for a user")  # Option to log a workout for a user
    print("3. View user information")  # Option to view user information
    print("4. View workout history")  # Option to view workout history
    print("5. Generate progress report")  # Option to generate progress report
    print("6. Exit")  # Option to exit the application


# Main application
def main():
    while True:  # Infinite loop to display menu until the user exits
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")  # User selects an option

        if choice == "1":  # If user selects option 1
            # Adding new user
            name = input("Enter name: ")  # Prompt for user name
            age = int(input("Enter age: "))  # Prompt for user age
            weight = float(input("Enter weight (kg): "))  # Prompt for user weight
            height = float(input("Enter height (cm): "))  # Prompt for user height
            goal = input("Enter fitness goal: ")  # Prompt for fitness goal
            users[name] = Person(name, age, weight, height, goal)  # Creating a new user
            print(f"User '{name}' has been added.")  # Confirming user addition

        elif choice == "2":  # If user selects option 2
            # Logging a workout for a user
            name = input("Enter the user's name: ")  # Prompt for user name

            if name in users:  # Check if the user exists
                workout_name = input("Enter workout name: ")  # Prompt for workout name
                workout = Workout(workout_name)  # Create a new Workout object

                while True:  # Loop to add multiple exercises to the workout
                    exercise_name = input("Enter exercise name (or 'done' to finish): ").strip()  # Prompt for exercise name

                    if exercise_name.lower() == 'done':  # If the user is done adding exercises
                        break  # Exit the loop

                    # Check if the exercise exists in the exercises dictionary
                    if exercise_name in exercises_dict:
                        exercise = exercises_dict[exercise_name]  # Retrieve the existing exercise
                        print(f"Using existing exercise: {exercise.name} ({exercise.difficulty})")  # Display exercise info
                    else:  # If the exercise doesn't exist in the dictionary
                        print(f"Exercise '{exercise_name}' not found.")  # Notify the user
                        description_of_exercise = input(f"Enter description for {exercise_name}: ").strip()  # Prompt for description

                        while True:  # Loop to ensure valid difficulty input
                            difficulty_of_exercise = input(
                                f"Enter the difficulty for {exercise_name} (Easy, Medium, Hard): ").strip()  # Prompt for difficulty
                            if difficulty_of_exercise in Exercise.VALID_DIFFICULTIES:  # Check if valid difficulty
                                break  # Exit the loop if valid
                            print("Invalid difficulty. Please choose from: Easy, Medium, Hard.")  # Invalid input message

                        exercise = Exercise(exercise_name, description_of_exercise, difficulty_of_exercise)  # Create new exercise

                        # Save the newly created exercise to exercises_dict
                        exercises_dict[exercise_name] = exercise
                        print(f"New exercise '{exercise_name}' added.")  # Confirm exercise addition

                    # Get sets, reps, and rest time for the exercise
                    try:
                        sets = int(input(f"Enter sets for {exercise_name}: "))  # Prompt for sets
                        reps = int(input(f"Enter reps for {exercise_name}: "))  # Prompt for reps
                        rest_time = int(input(f"Enter rest time (seconds) for {exercise_name}: "))  # Prompt for rest time
                    except ValueError:  # If there is a value error with the input
                        print("Invalid input. Please enter valid numbers for sets, reps, and rest time.")  # Error message
                        continue  # Skip the current iteration and continue the loop

                    workout.add_exercise(exercise_name, sets, reps, rest_time)  # Add exercise to the workout

                # Log the workout to the user's progress tracker
                tracker = ProgressTracker(users[name])  # Create a ProgressTracker object for the user
                tracker.log_workout(workout)  # Log the workout
                print(f"Workout '{workout_name}' logged for user '{name}'.")  # Confirm workout logging

            else:  # If the user doesn't exist
                print(f"User '{name}' not found.")  # Error message

        elif choice == "3":  # If user selects option 3
            # Viewing user info
            name = input("Enter the user's name: ")  # Prompt for user name
            if name in users:  # Check if the user exists
                print(users[name].display_info())  # Display user info
            else:  # If the user doesn't exist
                print(f"User '{name}' not found.")  # Error message



        elif choice == "4":  # If user selects option 4

            # Viewing workout history

            name = input("Enter the user's name: ")  # Prompt for user name

            if name in users:  # Check if the user exists

                history = users[name].workout_history  # Get workout history for the user

                print("\nWorkout History:")  # Print the header for workout history

                for workout in history:  # Loop through each workout in the history

                    print(f"Workout: {workout['workout_name']}, Date: {workout['date']}")  # Print workout name and date

                    # Join exercises as strings (assuming 'exercises' is a list of tuples like ('squat', '3 sets of 10'))

                    exercises_str = ", ".join([f"{exercise[0]} ({exercise[1]})" for exercise in
                                               workout['exercises']])  # Convert each tuple into a string

                    print(f"Exercises: {exercises_str}")  # Print the exercises as a string

                    print("---")  # Separator between workouts

            else:  # If the user doesn't exist

                print(f"User '{name}' not found.")  # Error message



        elif choice == "5":  # If user selects option 5
            # Generating progress report
            name = input("Enter the user's name: ")  # Prompt for user name
            if name in users:  # Check if the user exists
                tracker = ProgressTracker(users[name])  # Create a ProgressTracker object for the user
                print(tracker.generate_report())  # Generate and display the progress report
            else:  # If the user doesn't exist
                print(f"User '{name}' not found.")  # Error message

        elif choice == "6":  # If user selects option 6
            # Exiting the application
            print("Exiting the application. Goodbye!")  # Print exit message
            break  # Exit the loop and end the program

        else:  # If the user enters an invalid choice
            print("Invalid choice. Please try again.")  # Error message


if __name__ == "__main__":  # If the script is being run directly
    main()  # Call the main function to start the program
