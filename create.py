quiz_questions = ["What is 2+2", "What is 4+4", "What is 5+1"]

def quiz_question(new_question):
    for i in range(len(quiz_questions)):
        input_str = "Want to start with this question " + new_question  + "or this question"  + new_question  + "or this question" + quiz_questions[i] + " "
        