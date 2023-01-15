from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    quiz_question = Question(text, answer)
    question_bank.append(quiz_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(
    f"You've completed the quiz! Your final score is: {quiz.score}/{quiz.question_number}")
