quiz_questions = [
    "What is 2 + 2?",
    "What is 4 + 4?",
    "What is 7 x 2?",
    "What color is the sky?"
]

def quiz_question(new_question):
    input(new_question) ("Press enter to move on")

keep_playing = True

while keep_playing:
    play_quiz = input("Would you like to play my quiz? (Y/N): ")
    if play_quiz.upper() == "Y":
        print("Okay, let's start!\n")
        for question in quiz_questions:
            quiz_question(question) 
        print("\nThanks for playing!")
    else:
        print("Okay, maybe next time!")
        keep_playing = False
