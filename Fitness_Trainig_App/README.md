# 🏋️‍♂️ Fitness Training App

<!DOCTYPE html>
<body>
    <header class="header">
        <img src="https://mir-s3-cdn-cf.behance.net/project_modules/fs/218fc872735831.5bf1e45999c40.gif" alt="Header GIF">
    </header>
</body>
</html>


## Project Overview

The Fitness Training App is a Python project where I applied object-oriented programming (OOP) concepts. The app lets users create and manage workout routines, track their progress, and monitor their fitness journey.

## Learning Objectives

Understand OOP concepts 🧑‍💻: I focused on core OOP ideas like classes, objects, encapsulation, inheritance, and polymorphism.
Design a system 🛠️: I built a system that handles users, exercises, workout routines, and progress tracking.
Organize Python code 📂: I learned how to split the code into different modules, keeping everything clear and reusable.



### Project Structure

├── [user.py](https://github.com/Viktoria-Todorova/Small_Projects/blob/Projects/Fitness_Trainig_App/user.py)           # Contains the User class

├── [exercise.py](https://github.com/Viktoria-Todorova/Small_Projects/blob/Projects/Fitness_Trainig_App/exercise.py)       # Contains the Exercise class

├── [workout.py](https://github.com/Viktoria-Todorova/Small_Projects/blob/Projects/Fitness_Trainig_App/workout.py)        # Contains the Workout class

├── [progress.py](https://github.com/Viktoria-Todorova/Small_Projects/blob/Projects/Fitness_Trainig_App/progress.py)       # Contains the ProgressTracker class

├── [main.py](https://github.com/Viktoria-Todorova/Small_Projects/blob/Projects/Fitness_Trainig_App/main.py)           # Main script to run the application (menu system)

├── README.md         # Project documentation


# Workflow

## Step 1:  🧑‍💻 Set Up the User Profile

I created a User class to represent individual users. The user can input personal information like their name, age, weight, height, and fitness goal. I also provided functionality to update the weight and fitness goal over time.

## Step 2: 🏋️‍♂️ Build the Exercise Library

I created an Exercise class to store information about each exercise. Exercises have a name, description, and difficulty level. These exercises are stored in a dictionary (exercises_dict) and are available for users to choose from when building their workout routines.

## Step 3: 💪 Create Workout Plans

I designed a Workout class that allows users to create workout plans. Users can select exercises from the exercise library, specify the number of sets, reps, and rest time for each exercise, and build a complete routine. The workout plans can be viewed and modified.

## Step 4: 📈 Track Progress

I created a ProgressTracker class to track the user's progress. This class logs every workout, including details like the workout name, date, and the exercises performed. I also implemented functionality for generating a progress report that summarizes the user's workout history.

## Step 5: 🖥️ Add a Menu System

I implemented a simple text-based interface to allow users to interact with the app. Through the menu system, users can:

✅View and edit their profile

✅View available exercises

✅Create or modify workout routines

✅Log workouts and track their progress

## Some skreenshots of the process

![1](https://github.com/user-attachments/assets/301a88a0-2db5-4fc9-b6d7-f3f76ca15828)

![2](https://github.com/user-attachments/assets/45f78691-4257-4156-adf4-944d208ff67b)



# Conclusion 🎉
This project was a great learning experience where I applied object-oriented programming (OOP) principles to build a fitness tracker app. Through the development of the User, Exercise, Workout, and ProgressTracker classes, I was able to design a system that effectively manages user profiles, workout routines, and tracks fitness progress. The app allows users to create custom workouts, monitor their progress over time, and receive reports on their fitness journey.

# Challenges faced 💡
While working on this project, I encountered a few challenges. One of the main difficulties was ensuring that the user’s workout data, including sets, reps, and exercises, was properly stored and linked to the correct user profile. Additionally, creating a smooth, interactive user experience in a text-based environment required careful planning and handling of user inputs to avoid errors and ensure everything ran smoothly.

Despite these challenges, I successfully overcame them through debugging and careful testing. This project helped me deepen my understanding of how to organize and structure code, implement OOP principles, and handle user interactions efficiently.

I'm proud of how the app turned out, and this project has greatly improved my skills in Python and OOP design.
