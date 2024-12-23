from datetime import datetime  # Import the datetime module to work with dates and times

# Define the Person class to represent a user of the fitness tracker
class Person:
    # Constructor to initialize the attributes of the Person
    def __init__(self, name, age, weight, height, goal):
        self.name = name  # The name of the person
        self.age = age  # The age of the person
        self.weight = weight  # The weight of the person (in kilograms)
        self.height = height  # The height of the person (in centimeters)
        self.goal = goal  # The fitness goal of the person (e.g., "Lose weight", "Build muscle")
        self.workout_history = []  # A list to store the person's workout history

    # Method to update the person's weight and print a message
    def update_weight(self, new_weight):
        self.weight = new_weight  # Set the new weight
        print(f"{self.name}'s weight has been updated to {self.weight} kg.")  # Print confirmation

    # Method to update the person's fitness goal and print a message
    def update_goal(self, new_goal):
        self.goal = new_goal  # Set the new goal
        print(f"{self.name}'s goal has been updated to: {self.goal}.")  # Print confirmation

    # Method to log a workout for the person
    def log_workout(self, workout):
        current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date in "YYYY-MM-DD" format
        self.workout_history.append(f"{workout} on {current_date}")  # Append the workout with the current date to the history
        print(f"Workout logged: {workout} on {current_date}")  # Print confirmation of the logged workout

    # Method to display the person's information
    def display_info(self):
        # Return the person's details as a formatted string
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Height: {self.height}cm, Goal: {self.goal}"

    # Method to view the person's workout history
    def view_workout_history(self):
        return self.workout_history  # Return the list of workouts that the person has logged
