class Question:
    def __init__(self, qustion_text, question_answer):
        self.text = question_text
        self.answer = question_answer



class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! ")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


question_data = {"response_code":0,"results":[{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"Video streaming website YouTube was purchased in it&#039;s entirety by Facebook for US$1.65 billion in stock.","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"Dihydrogen Monoxide is a dangerous chemical.","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"medium","category":"General Knowledge","question":"Albert Einstein had trouble with mathematics when he was in school.","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"French is an official language in Canada.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"medium","category":"General Knowledge","question":"There are 86400 seconds in a day.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"The disease cancer in itself is not contagious.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"&quot;27 Club&quot; is a term used to refer to a list of famous actors, musicians, and artists who died at the age of 27.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"A pasodoble is a type of Italian pasta sauce.","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"The mitochondria is the powerhouse of the cell.","correct_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"medium","category":"General Knowledge","question":"The vapor produced by e-cigarettes is actually water.","correct_answer":"False","incorrect_answers":["True"]}]}

question_bank = []
for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
