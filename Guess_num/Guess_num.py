import random
import time

BLUE = "\033[34m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
class guess:
    def __init__(self):
        self.sequence = []
        self.first_term = 0
        self.difference = 0
        self.ratio = 0
        self.score = 0
        self.mistakes = 0
        self.questions_num = 0
        self.total_time = 0
        self.skipped = 0
        self.corrects = 0
        self.errors = []
        
    def create(self):
        self.category = random.randint(0, 1)
        if(self.category == 0):
            self.first_term = random.randint(4, 50)
        else:
            self.first_term = random.randint(2, 7)
        self.difference = random.randint(5, 40)
        self.ratio = random.randint(2, 7)
        
            
    def last_term(self):
        if (self.category == 0):
            return self.sequence[-1] + self.difference
        else:
            return self.sequence[-1] * self.ratio
    
    def start_term(self):
        self.sequence.append(self.first_term)
    
    def next_term(self):
        if (self.category == 0):
            self.sequence.append(self.sequence[-1] + self.difference)  
        else:
            self.sequence.append(self.sequence[-1] * self.ratio)  
            

    def play(self):
        print("Welcome to the game 'Find Next Number!'")
        time.sleep(1)
        start_time = time.time()
        running = True
        print("What is the next number in this sequence?")
        while(running):
            self.sequence.clear()
            self.create()
            self.start_term()
            self.questions_num +=1
            for _ in range(4):
                self.next_term()

            print(f"Question #{self.questions_num}: ", end="")
            for i in self.sequence:
                print(i , end=" ")
            
            user_answer = input().lower()
            if (user_answer == "q"):
                break;
            if (user_answer == "n"):
                print(f"{RED}Skipped.{RESET} -3 points")
                self.skipped += 1
                self.score -= 3
                self.sequence.clear()
                continue
            try:
                user_answer_int = int(user_answer)
            except:
                print("Invalid input. Try again.")
                self.questions_num -= 1
               
                continue
      
            if(user_answer_int == self.last_term()):
                print(f"{GREEN}Correct!{RESET} +5 points")
                self.score += 5
                self.corrects += 1
            else:
                print(f"{RED}Incorrect!{RESET} -5 points, the next term was {BLUE}{self.last_term()}{RESET}")
                self.score -=5
                self.mistakes += 1
                self.errors.append(self.questions_num)
                
        self.total_time = round(time.time() - start_time, 2)
    

        
    def show_statistics(self):
        print (f"Your total score for quiz is: {BLUE} {self.score}{RESET} points")
        print(f"You got: \n {self.corrects} correct answers \n {self.mistakes} mistakes \n {self.skipped} skipped questions  \n {self.questions_num} total questions \n in {self.total_time} seconds")
        if len(self.errors) > 0:
            print(f"You have errors in {' '.join(str(e) for e in sorted(set(self.errors)))}'s problem")
        if(self.score < 0):
            print(f"{RED}You lose the game :(  {RESET}")

    def reset(self):
        self.first_term = 0
        self.difference = 0
        self.ratio = 0
        self.score = 0
        self.mistakes = 0
        self.questions_num = 0
        self.total_time = 0
        self.skipped = 0
        self.corrects = 0
        
    
game = guess()
game.play()
game.show_statistics()
        
        
        
        
        
        