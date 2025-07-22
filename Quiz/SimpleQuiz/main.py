# Make a simple quiz application in Python where users 
# can answer questions, options and get a score.

import random
from questions import questions
def main():
    score=0
    # cerating a list named checklist to keep track of asked questions
    chklist=[]
    print("Welcome to the Quiz!")
    for i in range(5):
        choice=random.choice(questions)
        # to check if the question is already asked
        # if it is, we will choose another one
        while choice in chklist:
            choice=random.choice(questions)
        # add the choice to the checklist
        # so that we don't repeat the same question
        chklist.append(choice)
        print(f"Question {i+1}")
        print(choice[0])
        ans=input("Enter your answer: ").lower()
        if ans==choice[1]:
                score+=1
        
            
    print("Your Score is: ",score)
main()