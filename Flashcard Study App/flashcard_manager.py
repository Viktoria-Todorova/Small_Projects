import random
from flashcard import Flashcard  # Importing the Flashcard class from the flashcard module

class FlashcardManager:
    # Constructor to initialize the FlashcardManager with an empty collection of flashcards
    def __init__(self):
        # Flashcards will be stored in a dictionary where the question is the key and the Flashcard object is the value
        self.flashcards = {}

    # Method to add a new flashcard to the collection
    def add_flashcard(self, question, answer):
        """Add a new flashcard to the collection."""
        # Check if the question is already in the flashcards dictionary
        if question not in self.flashcards:
            # Create a new Flashcard object and add it to the dictionary with the question as the key
            self.flashcards[question] = Flashcard(question, answer)
        else:
            # If the question already exists, print a message indicating that the flashcard is already there
            print("Flashcard with this question already exists.")

    # Method to edit an existing flashcard's question and/or answer
    def edit_flashcard(self, question, new_question, new_answer):
        """Edit an existing flashcard's question and/or answer."""
        # Check if the question exists in the flashcards dictionary
        if question in self.flashcards:
            # Create a new Flashcard with the new question and answer
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            # If the new question is different from the original, delete the old flashcard
            if new_question != question:
                del self.flashcards[question]
            print(f"Flashcard edited: {new_question}")
        else:
            # If the question doesn't exist, print a message indicating the flashcard was not found
            print("Flashcard not found!")

    # Method to delete a flashcard by its question
    def delete_flashcard(self, question):
        """Delete a flashcard by its question."""
        # Check if the question exists in the flashcards dictionary
        if question in self.flashcards:
            # Delete the flashcard with the specified question
            del self.flashcards[question]
            print(f"Flashcard deleted: {question}")
        else:
            # If the question doesn't exist, print a message indicating the flashcard was not found
            print("Flashcard not found!")

    # Method to list all flashcards in the collection
    def list_flashcards(self):
        """List all flashcards in the collection."""
        # If there are no flashcards, print a message indicating the collection is empty
        if not self.flashcards:
            print("No flashcards to display!")
        # Loop through all flashcards and print their questions
        for question, flashcard in self.flashcards.items():
            print(flashcard.display_question())  # Display the question of each flashcard

    # Method to randomly pick a flashcard for review
    def review_flashcard(self):
        """Randomly pick a flashcard for review."""
        # Check if there are any flashcards
        if self.flashcards:
            # Pick a random question from the flashcards dictionary
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]
            # Print the question and ask the user to press Enter to show the answer
            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            # Print the answer of the selected flashcard
            print(flashcard.display_answer())
        else:
            # If there are no flashcards, print a message indicating the collection is empty
            print("No flashcards to review!")

    # Method to load predefined flashcards into the collection
    def load_predefined_flashcards(self):
        # List of predefined flashcards, with each tuple containing a question and its corresponding answer
        predefined_flashcards = [
            # Science Flashcards
            ("What is the chemical symbol for gold?", "Au"),
            ("Who developed the theory of general relativity?", "Albert Einstein"),
            ("What planet is known as the Red Planet?", "Mars"),
            ("What is the powerhouse of the cell?", "Mitochondria"),
            ("What is the most common gas in Earth's atmosphere?", "Nitrogen"),

            # History Flashcards
            ("Who was the first president of the United States?", "George Washington"),
            ("In which year did World War II end?", "1945"),
            ("What was the name of the ship that famously sank after hitting an iceberg in 1912?", "Titanic"),
            ("Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart"),
            ("What ancient civilization built the pyramids of Giza?", "Ancient Egyptians"),

            # Geography Flashcards
            ("What is the longest river in the world?", "Nile River"),
            ("Which country is both an island and a continent?", "Australia"),
            ("What is the capital city of Japan?", "Tokyo"),
            ("Which country has the most pyramids in the world?", "Sudan"),
            ("What is the tallest mountain in the world?", "Mount Everest"),

            # Literature Flashcards
            ("Who wrote the play *Romeo and Juliet*?", "William Shakespeare"),
            ("What is the title of the first book in the *Harry Potter* series?", "Harry Potter and the Sorcerer's Stone"),
            ("Which novel begins with the line, “Call me Ishmael”?", "Moby-Dick"),
            ("Who wrote *1984* and *Animal Farm*?", "George Orwell"),
            ("What famous novel features the characters Gatsby, Daisy, and Nick?", "The Great Gatsby"),

            # Technology Flashcards
            ("Who is known as the father of the computer?", "Charles Babbage"),
            ("What programming language is named after a type of coffee?", "Java"),
            ("What does 'HTTP' stand for in a website address?", "HyperText Transfer Protocol"),
            ("What was the first video game ever created?", "Tennis for Two"),
            ("Who founded the company Microsoft?", "Bill Gates and Paul Allen"),

            # Random Fun Facts Flashcards
            ("What is the only fruit that has seeds on the outside?", "Strawberry"),
            ("How many bones are in the adult human body?", "206"),
            ("What is the national animal of Scotland?", "Unicorn"),
            ("What is the rarest blood type in the world?", "Rh-null"),
            ("What is the most expensive spice in the world by weight?", "Saffron"),

            # Space & Astronomy Flashcards
            ("What is the closest planet to the Sun?", "Mercury"),
            ("Which planet is known for having a ring system?", "Saturn"),
            ("What is the name of the galaxy that contains our solar system?", "The Milky Way"),
            ("How many moons does Jupiter have?", "79"),
            ("What is the phenomenon that occurs when the moon passes directly between the Earth and the Sun?", "Solar Eclipse"),

            # Art & Culture Flashcards
            ("Who painted the *Mona Lisa*?", "Leonardo da Vinci"),
            ("What type of art is Pablo Picasso known for?", "Cubism"),
            ("What is the most famous work by Vincent van Gogh?", "Starry Night"),
            ("Who wrote *The Divine Comedy*?", "Dante Alighieri"),
            ("What famous museum is located in Paris, France?", "The Louvre"),
        ]

        # Adding predefined flashcards to the collection
        for question, answer in predefined_flashcards:
            self.add_flashcard(question, answer)  # Adds each predefined flashcard to the manager
