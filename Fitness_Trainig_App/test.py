exercise = Exercise("squat","lowers their hips from a standing position and then stands back up","Easy")
print(exercise.display_exercise())



class Exercise:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display_exercise(self):
        return f"{self.name} ({self.difficulty}): {self.description}"


def get_exercises():
    name = input("What is the name of the exercise? ")
    description = input("Description of the exercise: ")
    difficulty = input("What is the difficulty of the exercise? ")

    return Exercise(name, description, difficulty)

exercises_dict = {}

# Loop to add multiple exercises
while True:
    current_exercise = get_exercises()
    exercises_dict[current_exercise.name] = current_exercise

    # Display exercise details
    print(current_exercise.display_exercise())

    # Ask the user if they want to add another exercise
    another = input("Do you want to add another exercise? [y/n]: ").lower()
    if another != 'y':
        break

# Display all stored exercises
print("\nStored Exercises:")
for exercise_name, exercise in exercises_dict.items():
    print(exercise.display_exercise())