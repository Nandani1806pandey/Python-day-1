# from Day33_python import question_data
from quiz_brain import Quiz_Brain
from question_model import Question
from UI import quizInterface
import requests
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    quiz = Quiz_Brain(question_bank)
    quiz_ui = quizInterface()
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")