import random
import time  

quiz_questions = ["What is 2 + 2?", "What is 4 + 4?", "What is 7 x 2?", "What color is the sky?"]
quiz_answers = ["4", "8", "14", "Blue"]  

def quiz_question(new_question):
    for i in range(len(quiz_questions)):
        print(new_question[i]) 
        time.sleep(1)  
        user_answer = input("Your answer: ")  
        if user_answer == quiz_answers[i]:
            print("correct")
        else:
            print("incorrect")
        time.sleep(1)  

continue_playing = True

while continue_playing:
    play_quiz = input("Hello! Want to play my quiz, Yes or No: ")
    if play_quiz=="Yes": 
        print("Awesome! Let's start")
        time.sleep(1)  
        quiz_question(quiz_questions)
    else: 
        print("Okay bye! :)")
        continue_playing = False

    play_again = input("Want to play again? Y/N")
    if play_again == "Y":
        print(continue_playing)

    else: 
     if play_again =="N":
        print("Okay! Thanks for playing my mini quiz!")

