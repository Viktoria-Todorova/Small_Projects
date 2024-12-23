# Importing the Exercise class and exercises_dict from the exercise.py file.
# The Exercise class represents an exercise, and exercises_dict is a dictionary containing all exercises.
from exercise import Exercise, exercises_dict

class Workout:
    def __init__(self, name):
        # Initialize the workout with a name and an empty list of exercises
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise_name, sets, reps, rest_time):
        # Find the exercise by name in exercises_dict
        exercise = exercises_dict.get(exercise_name)

        # If the exercise is found, add it to the workout's exercise list with additional details (sets, reps, rest time)
        if exercise:
            self.exercises.append({'exercise': exercise, 'sets': sets, 'reps': reps, 'rest_time': rest_time})
        else:
            # If the exercise is not found, print an error message
            print(f"Exercise '{exercise_name}' not found in the database!")

    def remove_exercise(self, exercise_name):
        # Remove an exercise from the workout by its name
        self.exercises = [ex for ex in self.exercises if ex['exercise'].name != exercise_name]

    def view_workout(self):
        # Display the workout details: workout name and each exercise's details (name, difficulty, sets, reps, rest time)
        print(f"\nWorkout: {self.name}")
        print("-" * 30)
        for idx, ex in enumerate(self.exercises, 1):
            difficulty = ex['exercise'].difficulty
            print(
                f"{idx}. {ex['exercise'].name} ({difficulty}): {ex['sets']} sets, {ex['reps']} reps, {ex['rest_time']} seconds rest")
        print("-" * 30)


# Define specific workout routines for different muscle groups

# Chest workout routine
def chest_routine():
    # Create a new Workout instance for Chest
    chest_workout = Workout("Chest Routine")
    # Add exercises to the chest workout
    chest_workout.add_exercise("Push-up", sets=3, reps=12, rest_time=60)
    chest_workout.add_exercise("Bicep Curl", sets=3, reps=15, rest_time=60)
    chest_workout.add_exercise("Plank", sets=3, reps=1, rest_time=30)
    return chest_workout

# Back workout routine
def back_routine():
    # Create a new Workout instance for Back
    back_workout = Workout("Back Routine")
    # Add exercises to the back workout
    back_workout.add_exercise("Pull-up", sets=4, reps=8, rest_time=90)
    back_workout.add_exercise("Deadlift", sets=3, reps=10, rest_time=120)
    back_workout.add_exercise("Row", sets=3, reps=10, rest_time=90)
    return back_workout

# Legs workout routine
def legs_routine():
    # Create a new Workout instance for Legs
    legs_workout = Workout("Legs Routine")
    # Add exercises to the legs workout
    legs_workout.add_exercise("Squats", sets=4, reps=15, rest_time=90)
    legs_workout.add_exercise("Lunges", sets=3, reps=12, rest_time=60)
    legs_workout.add_exercise("Deadlift", sets=3, reps=10, rest_time=120)
    return legs_workout

# Shoulders workout routine
def shoulders_routine():
    # Create a new Workout instance for Shoulders
    shoulders_workout = Workout("Shoulders Routine")
    # Add exercises to the shoulders workout
    shoulders_workout.add_exercise("Shoulder Press", sets=3, reps=12, rest_time=90)
    shoulders_workout.add_exercise("Lateral Raise", sets=3, reps=12, rest_time=60)
    shoulders_workout.add_exercise("Front Raise", sets=3, reps=12, rest_time=60)
    return shoulders_workout

# Arms workout routine (Biceps and Triceps)
def arms_routine():
    # Create a new Workout instance for Arms
    arms_workout = Workout("Arms Routine")
    # Add exercises to the arms workout
    arms_workout.add_exercise("Bicep Curl", sets=4, reps=15, rest_time=60)
    arms_workout.add_exercise("Tricep Dips", sets=3, reps=12, rest_time=60)
    arms_workout.add_exercise("Hammer Curl", sets=3, reps=12, rest_time=60)
    return arms_workout

# Core workout routine
def core_routine():
    # Create a new Workout instance for Core
    core_workout = Workout("Core Routine")
    # Add exercises to the core workout
    core_workout.add_exercise("Sit-up", sets=3, reps=20, rest_time=60)
    core_workout.add_exercise("Plank", sets=3, reps=1, rest_time=30)
    core_workout.add_exercise("Russian Twist", sets=3, reps=20, rest_time=60)
    return core_workout


# Example Usage:
if __name__ == "__main__":
    # Get a chest workout routine and view it
    my_chest_routine = chest_routine()
    my_chest_routine.view_workout()

    # Get a back workout routine and view it
    my_back_routine = back_routine()
    my_back_routine.view_workout()

    # Get a legs workout routine and view it
    my_legs_routine = legs_routine()
    my_legs_routine.view_workout()

    # Get a shoulders workout routine and view it
    my_shoulders_routine = shoulders_routine()
    my_shoulders_routine.view_workout()

    # Get an arms workout routine and view it
    my_arms_routine = arms_routine()
    my_arms_routine.view_workout()

    # Get a core workout routine and view it
    my_core_routine = core_routine()
    my_core_routine.view_workout()
