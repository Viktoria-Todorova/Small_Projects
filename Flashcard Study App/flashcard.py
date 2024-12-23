class Flashcard:
    # The constructor (__init__) initializes the Flashcard object with a question and an answer.
    def __init__(self, question, answer):
        self.question = question  # The question is stored in the instance variable 'self.question'
        self.answer = answer      # The answer is stored in the instance variable 'self.answer'

    # This method is used to get and display the question of the flashcard
    def display_question(self):
        return f"{self.question}"  # Returns the stored question, using f-string formatting

    # This method is used to get and display the answer of the flashcard
    def display_answer(self):
        return f"{self.answer}"  # Returns the stored answer, using f-string formatting
