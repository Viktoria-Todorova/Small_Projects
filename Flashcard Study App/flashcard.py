
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_question(self):
        return f"{self.question}"

    def display_answer(self):
        return f"{self.answer}"