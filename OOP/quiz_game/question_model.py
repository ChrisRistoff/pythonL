from data import question_data

# from krsnhrstv/Python/OOP_and_GUI/quiz_game/data.py


class Question:
    def __init__(self, index):
        self.question_data = question_data
        self.index = index

    def pick_question(self):
        question = self.question_data[self.index]
        return question

def main():
    question = Question(0)
    print(question.pick_question())
