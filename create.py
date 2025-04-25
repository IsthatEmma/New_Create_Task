import random
import time  

quiz_questions = ["What is 2 + 2?", "What is 4 + 4?", "What is 7 x 2?", "What color is the sky?"]
answer_key = ["4", "8", "14", "Blue"]  

def quiz_question(new_question):
    for i in range(len(quiz_questions)):
        print(new_question[i]) 
        time.sleep(3.5)  

        user_answer = input(" ")  
        if user_answer == answer_key[i]:
            print("Correct! Hooray :D")
        else:
            print("incorrect sorry :(")
        time.sleep(2.5)  

continue_playing = True

while continue_playing:
    play_quiz = input("Hello! Want to play my quiz, Yes or No: ")
    if play_quiz=="Yes": 
        print("Hooray, Awesome! Let's start")
        time.sleep(1)  
        quiz_question(quiz_questions)
    else: 
        print("Okay bye! :)")
        continue_playing = False
        break

    play_again = input("Want to play again? Yes/No")
    if play_again == "Yes":
        print("Okay!")
        time.sleep(2)
        continue
       
    else: 
     if play_again =="No":
        print("Okay! Thanks for playing my mini quiz!")
        break

