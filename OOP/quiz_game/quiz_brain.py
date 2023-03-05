from question_model import Question


class QuizBrain:
    def __init__(self, index):
        self.index = index
        self.question = Question(self.index).pick_question()

    def get_answer(self, answer):
        """prints the question and takes answer
        takes an empty string as parameter"""
        print(self.question["text"])
        while answer != "true" and answer != "false":
            answer = input("Pick True or False :\n").lower()
        return answer

    def check_answer(self):
        answer = QuizBrain.get_answer(self, "")
        if answer == self.question["answer"].lower():
            print(f"That's correct, the statement is {answer}")
            return 1
        else:
            print("You are wrong! The statement was " + self.question["answer"])
            return -100
