import tkinter as tk
import random
from flashcard import Flashcard
from flashcard_manager import FlashcardManager

class FlashcardApp(tk.Tk):
    def __init__(self, flashcard_manager):
        super().__init__()
        self.flashcard_manager = flashcard_manager
        self.title("Flashcard Study App")
        self.geometry("400x300")

        # Set the background color of the window
        self.configure(bg='lightblue')  # Change window background color

        # Create a frame to hold the question and answer
        self.card_frame = tk.Frame(self, relief="solid", borderwidth=2, bg='#D3A6FF')
        self.card_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create a label for displaying the flashcard question
        self.question_label = tk.Label(self.card_frame, text="Question: ", font=("Helvetica", 12, "bold"), fg="blue", bg='#D3A6FF', wraplength=350, anchor="w")
        self.question_label.pack(pady=(10, 0), fill="both", expand=True)

        # Create a label for displaying the answer (center the text)
        self.answer_label = tk.Label(self.card_frame, text="Answer: ", font=("Helvetica", 10), fg="blue", bg='pink',
                                     wraplength=350, anchor="center", justify="center")
        self.answer_label.pack(pady=(5, 10), fill="both", expand=True)

        # Create a button to show the answer
        self.show_answer_button = tk.Button(self, text="Show Answer", command=self.show_answer, fg="blue", bg='pink')
        self.show_answer_button.pack(pady=(10, 20))

        # Create a button to load a new random flashcard
        self.new_flashcard_button = tk.Button(self, text="Next Flashcard", command=self.load_flashcard, fg="blue", bg='pink')
        self.new_flashcard_button.pack(pady=(5, 20))

        # Initialize with a random flashcard
        self.load_flashcard()

    def load_flashcard(self):
        """Load a random flashcard and display the question."""
        if self.flashcard_manager.flashcards:
            # Pick a random flashcard
            question = random.choice(list(self.flashcard_manager.flashcards.keys()))
            flashcard = self.flashcard_manager.flashcards[question]

            # Set the question text
            self.question_label.config(text=f"Question: {flashcard.display_question()}")
            self.answer_label.config(text="Answer: ")  # Clear answer initially
        else:
            self.question_label.config(text="No flashcards available!")
            self.answer_label.config(text="")

    def show_answer(self):
        """Show the answer to the current flashcard."""
        # Find the question that is currently being shown
        current_question = self.question_label.cget("text").replace("Question: ", "")

        if current_question:
            # Get the corresponding flashcard
            flashcard = self.flashcard_manager.flashcards.get(current_question)
            if flashcard:
                # Update the answer label with the correct answer
                self.answer_label.config(text=f"Answer: {flashcard.display_answer()}")

def main():
    # Create an instance of FlashcardManager
    manager = FlashcardManager()

    # Load predefined flashcards
    manager.load_predefined_flashcards()

    # Start the Tkinter app
    app = FlashcardApp(manager)
    app.mainloop()

if __name__ == "__main__":
    main()
