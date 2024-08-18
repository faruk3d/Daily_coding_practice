from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []
for item in question_data:
    text = item.get("text")
    answer = item.get("answer")
    question = Question(text, answer)
    question_list.append(question)

quiz = QuizBrain(question_list)
while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score is: {quiz.player_score}/{quiz.question_number}")