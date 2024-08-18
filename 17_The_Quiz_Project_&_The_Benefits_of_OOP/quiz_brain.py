class QuizBrain:
    
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.player_score = 0
        self.question_list = question_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(player_answer, current_question.answer)
        
    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            self.player_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.player_score}/{self.question_number}")
        print("\n")
        

