class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {question.text}. (True/False)?: ")
        if answer.lower() == question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, that's wrong!")
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")