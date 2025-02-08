import random
import time

class Question:
    def __init__(self):
        self.question = ""
        self.options = [""] * 4
        self.answer = ""

    def __str__(self):
        options_str = '\n'.join([f"{chr(65+i)}) {option}" for i, option in enumerate(self.options)])
        return f"{self.question}?\n{options_str}"

    
class Quiz(Question):
    
    
    def __init__(self):
       
        self.category = input("Enter a rubric for the game (g for geography, a for arts and culture, h for history, s for sports): ").lower()
        self.rubric = self.select_rubric()
        self.questions = []
        self.num = 0
            
        
        
    def welcome(self):
        pass
    
    def select_rubric(self):
        if self.category == 'g':
            self.rubric = "geography.txt"
        elif self.category == 'a':
            self.rubric = "arts.txt"
        elif self.category == 'h':
            self.rubric = "history.txt"
        elif self.category == 's':
            self.rubric = "sports.txt"
        return self.rubric
    
    def load(self):
        try:
            with open(self.rubric, "r") as file:
                i = 0
                lines = file.readlines()
                while i < len(lines):
                    q = Question()
                    if i < len(lines):
                        q.question = lines[i].strip()
                        i+=1
                    for j in range(4):
                        if i < len(lines):
                            q.options[j] = lines[i].strip()
                            i+=1
                    if i < len(lines):
                        q.answer = lines[i].strip()
                        i+=1
                    
                    self.questions.append(q)
        except Exception as e:
            print("An error occurred:", str(e))
            return ""


            
    
    def play(self):
       # print(list(self.questions))
       self.num += 1
       for elem in self.questions:
           print(f"Question #{self.num} {elem}")
           print()
    
    def show_statistics(self):
        pass
    def reset(self):
        pass
    

game = Quiz()
game.welcome()
game.load()
game.play()
game.reset()