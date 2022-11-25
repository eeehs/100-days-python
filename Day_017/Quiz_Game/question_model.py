from data import question_data

class Question():
    
    def __init__(self, text , answer):
        self.text = text
        self.answer = answer

A_Question = Question("2+3=5", "True")

#print(A_Question.text)  
