from data import question_data
from quiz_brain import QuizBrain
import random


class Main:
    def __init__(self, index):
        self.index = index

    def play(self):
        self.index = random.randint(0, len(question_data) - 1)
        quiz = QuizBrain(self.index)
        return quiz.check_answer()


while True:
    play_again = ""
    score = 0
    while score >= 0:
        print(f"Your Score is: {score}")
        g = Main(0)
        score += g.play()
    while play_again != "y" and play_again != "n":
        play_again = input("Do you want to play again? y/n\n").lower()
    if play_again == "n":
        break
