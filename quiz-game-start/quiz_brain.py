class QuizzBrain: 
    def __init__(self, question_list):
        self.q_num = 0
        self.q_list = question_list


    def still_has_question(self):
        has_question = True
        if self.q_num < len(self.q_list):
            return True
        else:
            False
    
    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1 
        user_answer = input(f"Q. {self.q_num} : {current_question.q_text} (True/False): ")
        

    def check_answer(self):
