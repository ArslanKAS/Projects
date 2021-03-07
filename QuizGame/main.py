from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    question_bank.append(Question(x['question'], x['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your Final score is: {quiz.score}/{quiz.question_no}")
