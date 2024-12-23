# Define the Exercise class to represent an exercise with a specific name, description, and difficulty
class Exercise:
    # Valid difficulties as a class-level constant (shared among all instances of the Exercise class)
    VALID_DIFFICULTIES = ["Easy", "Medium", "Hard"]

    def __init__(self, name, description, difficulty):
        # Check if the difficulty is a valid string. If not, raise a ValueError
        if difficulty not in Exercise.VALID_DIFFICULTIES:
            raise ValueError(
                f"Invalid difficulty level: {difficulty}. Choose from {', '.join(Exercise.VALID_DIFFICULTIES)}."
            )

        self.name = name  # Store the name of the exercise
        self.description = description  # Store the description of the exercise
        self.difficulty = difficulty  # Store the difficulty as a string

    # Method to return a string representation of the exercise in a readable format
    def display_exercise(self):
        return f"{self.name} - {self.description} ({self.difficulty})"


# Define multiple Exercise objects with different names, descriptions, and difficulty levels
exercise1 = Exercise("Push-up", "A basic exercise where you lower and raise your body using your arms.", "Medium")
exercise2 = Exercise("Plank", "Hold a plank position to strengthen your core and shoulders.", "Hard")
exercise3 = Exercise("Jumping Jacks",
                     "A full-body aerobic exercise involving jumping with arms and legs moving outward.", "Easy")
exercise4 = Exercise("Burpees", "A full-body exercise involving a squat, jump, and push-up.", "Hard")
exercise5 = Exercise("Lunges",
                     "A leg exercise where one leg is positioned forward with knee bent while the other remains stationary.",
                     "Medium")
exercise6 = Exercise("Mountain Climbers", "A cardio and strength exercise mimicking a climbing motion.", "Medium")
exercise7 = Exercise("Pull-up", "An upper-body exercise where you pull yourself up using a bar.", "Hard")
exercise8 = Exercise("Sit-up", "An abdominal exercise where you lift your upper body from a lying position.", "Easy")
exercise9 = Exercise("Bicep Curl", "A strength training exercise targeting the biceps with a dumbbell or barbell.",
                     "Easy")
exercise10 = Exercise("Deadlift", "A compound strength exercise where you lift a loaded barbell from the ground.",
                      "Hard")
exercise11 = Exercise("High Knees", "A cardio exercise where you run in place lifting your knees as high as possible.",
                      "Easy")
exercise12 = Exercise("Side Plank", "A core exercise where you support your body on one side.", "Medium")
exercise13 = Exercise("Tricep Dips", "An exercise using a chair or bar to strengthen the triceps.", "Medium")
exercise14 = Exercise("Russian Twist", "A core exercise involving rotation of the torso from side to side.", "Medium")
exercise15 = Exercise("Squat Jump", "A plyometric exercise combining a squat and a jump.", "Hard")

# Add all the Exercise instances to a dictionary, using the exercise name as the key
exercises_dict = {
    exercise.name: exercise for exercise in [
        exercise1, exercise2, exercise3, exercise4, exercise5,
        exercise6, exercise7, exercise8, exercise9, exercise10,
        exercise11, exercise12, exercise13, exercise14, exercise15
    ]
}


# Utility function to filter exercises by difficulty
def filter_by_difficulty(difficulty):
    # This function filters the exercises by the given difficulty level (Easy, Medium, or Hard)
    return [exercise.display_exercise() for exercise in exercises_dict.values() if exercise.difficulty == difficulty]


# Main execution block that runs if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Example usage: filter and print exercises by different difficulty levels

    # Filter and print exercises that are categorized as "Easy" difficulty
    print("\nEasy Difficulty Exercises:")
    for exercise in filter_by_difficulty("Easy"):
        print(exercise)

    # Filter and print exercises that are categorized as "Medium" difficulty
    print("\nMedium Difficulty Exercises:")
    for exercise in filter_by_difficulty("Medium"):
        print(exercise)

    # Filter and print exercises that are categorized as "Hard" difficulty
    print("\nHard Difficulty Exercises:")
    for exercise in filter_by_difficulty("Hard"):
        print(exercise)
