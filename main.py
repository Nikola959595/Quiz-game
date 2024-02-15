from question_model import Question
from quiz_brain import QuizBrain
import requests, json

url = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
text = url.text

quiz_api_data = json.loads(text)

question_data = quiz_api_data["results"]

question_bank = []

for item in question_data:
    formatted = item["question"].replace("&quot;","'")
    next_question = Question(formatted,item["correct_answer"])
    question_bank.append(next_question)

print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if not quiz.still_has_questions():
    print("You've completed the quiz!")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")