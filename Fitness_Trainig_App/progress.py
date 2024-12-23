from datetime import datetime
from workout import Workout  # Import the Workout class to work with workout routines

class ProgressTracker:
    def __init__(self, user):
        # Initialize the ProgressTracker with a user.
        # The user is expected to have a 'workout_history' attribute where workout logs are stored.
        self.user = user

    def log_workout(self, workout: Workout):
        # Log a workout for the user.
        current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date in 'YYYY-MM-DD' format
        workout_details = {
            'workout_name': workout.name,  # Store the name of the workout
            'date': current_date,  # Store the date of the workout
            'exercises': [
                (ex['exercise'].name, ex['sets'], ex['reps'], ex['rest_time'])  # List details of each exercise in the workout
                for ex in workout.exercises
            ]
        }
        # Add the workout details to the user's workout history
        self.user.workout_history.append(workout_details)
        print(f"Workout logged: {workout.name} on {current_date}")

    def generate_report(self):
        # Generate a summary report of the user's completed workouts
        total_workouts = len(self.user.workout_history)  # Count the total number of workouts logged
        return f"{self.user.name} has completed {total_workouts} workouts."  # Return a formatted string with the workout count
