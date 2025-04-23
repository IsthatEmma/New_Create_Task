quiz_questions = ["What is 2 + 2?", "What is 4 + 4?", "What is 7 x 2?", "What color is the sky?"]
quiz_answers = ["4", "8", "14", "Blue"]  

def quiz_question(new_question):
    for i in range(len(quiz_questions)):
        user_answer = input(new_question[i] + " ")
        if user_answer == quiz_answers[i]:
            print("correct")
        else:
            print("incorrect")

continue_playing = True

while continue_playing:
    play_quiz = input("Hello! Want to play my quiz, Yes or No: ")
    if play_quiz == "Yes":
        print("Awesome! Let's start")
        quiz_question(quiz_questions)
    else: 
        print("Okay bye! :)")
        continue_playing = False