# Make a simple quiz application in Python where users 
# can answer questions, options and get a score.
import random
from questions import questions
def main():
    score=0
    selected_questions=random.sample(questions, 5)
    print("Welcome to the Quiz!")
    for i in range(len(selected_questions)):
        print(f"Question {i+1}")
        print(selected_questions[i]["question"])
        print(selected_questions[i]["Options"])
        ans=input("Enter (A, B, C,D):").upper()
        if ans==selected_questions[i]["Answer"]:
            score+=1
        
            
    print("Your Score is: ",score)
main()
        