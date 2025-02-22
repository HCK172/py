from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

# create a question bank of question object
question_bank = []

print(type(question_data))

for question in question_data:
    q = Question(question['text'], question['answer'])
    question_bank.append(q)

print(question_bank)

quizz = QuizzBrain(question_bank)
quizz.next_question()
    
while quizz.still_has_question(): 
    quizz.next_question()

