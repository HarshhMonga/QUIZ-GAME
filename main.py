from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_text = i["question"]
    question_ans = i["correct_answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've Completed The Quiz")
print(f"Your Final Score is {quiz.score}/{quiz.question_number}")
