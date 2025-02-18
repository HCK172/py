## print(logo of the game)
import json
import random

def check_answer(user_choice, a_totalEarning, b_totalEarning):

    if a_totalEarning > b_totalEarning:
         return user_choice == 'a'
    else: 
         return user_choice == 'b'

## get data from the json file
with open('100dayPython/HigherLower/questions.json', 'r') as file: 
    content = file.read()
data = json.loads(content)

M =1_000_000

print(data[1])
## we will have 5 questions 
score = 0
for i in range(5):
    # generate random number to get A & B: 
     account_a = random.choice(data)
     account_b = random.choice(data)
     if account_a == account_b:
        account_b = random.choice(data)
    
     a_totalEarning = account_a['total_earning']
     b_totalEarning = account_b['total_earning']
     print(f'Compare A: {account_a['name']}')
     print(f'Against B: {account_b['name']}')
     print(f'Who made more money? A or B')
     user_choice = input('Enter A or B: ').lower().strip()

     is_correct = check_answer(user_choice, a_totalEarning, b_totalEarning)
     print(is_correct)
     if is_correct: 
        score += 1
        print(f'Your correct! Current score: {score} ')
     else: 
         print(f'You got it wrong! Current score: {score}')


     
    



        

        
        

         
