import random
from flashcard import Flashcard

class FlashcardManager:
    def __init__(self):
        # Flashcards will be stored in a dictionary with the question as the key
        self.flashcards = {}

    def add_flashcard(self, question, answer):
        """Add a new flashcard to the collection."""
        if question not in self.flashcards:
            self.flashcards[question] = Flashcard(question, answer)

        else:
            print("Flashcard with this question already exists.")

    def edit_flashcard(self, question, new_question, new_answer):
        """Edit an existing flashcard's question and/or answer."""
        if question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != question:
                del self.flashcards[question]
            print(f"Flashcard edited: {new_question}")
        else:
            print("Flashcard not found!")

    def delete_flashcard(self, question):
        """Delete a flashcard by its question."""
        if question in self.flashcards:
            del self.flashcards[question]
            print(f"Flashcard deleted: {question}")
        else:
            print("Flashcard not found!")

    def list_flashcards(self):
        """List all flashcards in the collection."""
        if not self.flashcards:
            print("No flashcards to display!")
        for question, flashcard in self.flashcards.items():
            print(flashcard.display_question())

    def review_flashcard(self):
        """Randomly pick a flashcard for review."""
        if self.flashcards:
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]
            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            print(flashcard.display_answer())
        else:
            print("No flashcards to review!")

    # Load predefined flashcards
    def load_predefined_flashcards(self):
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
            self.add_flashcard(question, answer)
