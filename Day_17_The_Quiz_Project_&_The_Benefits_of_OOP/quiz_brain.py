class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        
        
        
        
        # for question in self.question_list:
        #     print(f"Q.{self.question_number + 1}: {question.text}. (True/False)?")
        #     player_answer = input("True or False? ")
        #     self.question_number += 1
        #     if self.question_number != len(self.question_list):
        #         if player_answer == question.answer:
        #             print("Correct!")
        #         else:
        #             print("Not correct.")
        #     else:
        #         print("Quiz Done.")
                
