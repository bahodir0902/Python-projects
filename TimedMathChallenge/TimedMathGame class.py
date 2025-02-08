import random
import time
import threading
import os

class TimedMathChallenges:
    def __init__(self):
        self.__operators = ['+', '-', '*']
        self.__min_value, self.__max_value, self.__time_lim  = self.__set_difficulty()
        self.__wrong_answers = 0
        self.__correct = 0
        self.__numbers = 0
        self.__skipped = 0
        self.__running = True
        self.__errors = []
        self.__points = 0
        self.__total_time = 0
       
    
    def __set_difficulty(self):
        mode = input("Do you want to set a difficulty for the game? (y/n): ")
        if mode.lower() == 'y':
            self.__time_lim = int(input("Set a time for each question: "))
            self.__min_value = int(input("Input the minimum value: "))  
            self.__max_value = int(input("Input the maximum value: "))
            return self.__min_value, self.__max_value, self.__time_lim
        elif mode.lower() == 'n':
            print("Default time for each question: 10 seconds")
            print("Default minimum and maximum range: -10 and 15")
            self.__time_lim = 10
            self.__min_value = random.randint(-10, 10)
            self.__max_value = random.randint(self.__min_value, 15)
            return self.__min_value, self.__max_value, self.__time_lim
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


    def __generate_problem(self):
        operator = random.choice(self.__operators)
        left_digit = random.randint(self.__min_value, self.__max_value)
        right_digit = random.randint(self.__min_value, self.__max_value)
        if operator == '-' and right_digit < 0:
            problem = f"{left_digit} + {abs(right_digit)}"
        elif operator == '+':
            if right_digit < 0:
                problem = f"{left_digit} - {abs(right_digit)}"
            else:
                problem = f"{left_digit} + {right_digit}"
        else:
            problem = f"{left_digit} {operator} {right_digit}"
        answer = eval(problem)
        return problem, answer

    def __timer(self, stop_timer):
        for remaining in range(self.__time_lim, 0, -1):
            if stop_timer.is_set():
                return
            time.sleep(1)
        stop_timer.set()

    def play(self):
        print("Welcome to the Timed mathematical challenges game!")
        time.sleep(0.3)
        print("You will be presented with a series of math problems.")
        time.sleep(0.3)
        print("You have 10 seconds to solve each problem.")
        time.sleep(0.3)
        print("Enter 'n' to skip a problem at a penalty of 10 points.")
        print("Enter 'q' to quit the game.")
        print("Let's get started!")
        time.sleep(0.55)
        start_time = time.time()
        while self.__running:
            try:
                problem, answer = self.__generate_problem()
                self.__numbers += 1
            except:
                continue
            stop_timer = threading.Event()
            timer_thread = threading.Thread(target=self.__timer, args=(stop_timer,))
            timer_thread.start()
            while True:
                try:
                    user_answer = input(f"Problem #{self.__numbers}: {problem}: ").rstrip('\n')
                    if stop_timer.is_set():
                        print("\rTime is up! -5 points! Moving to the next question...")
                        self.__points -= 5
                        stop_timer.clear()
                        break
                    if user_answer.lower() == 'n':
                        self.__skipped += 1
                        self.__points -= 10
                        stop_timer.set()
                        break
                    elif user_answer.lower() == 'q':
                        if self.__wrong_answers == 0:
                            self.__numbers -= 1
                        self.__running = False
                        stop_timer.set()
                        break
                    user_answer = int(user_answer)
                    if answer == user_answer:
                        print("Congratulations! +10 points")
                        self.__correct += 1
                        self.__points += 10
                        stop_timer.set()
                        break
                    else:
                        print("Ooops! Try again! -5 points")
                        self.__points -= 5
                        self.__wrong_answers += 1
                        self.__errors.append(self.__numbers)
                except ValueError:
                    print("Invalid output. Enter an integer. -3 points")
                    self.__points -= 3

        end_time = time.time()
        self.__total_time = round(end_time - start_time, 3)
        print("\nGame over!")
    def show_statistics(self):
        print(f"You have:\n {self.__correct} correct answers \n {self.__wrong_answers} wrong answers \n {self.__numbers} total questions \n {self.__skipped} skipped questions \n in total {self.__total_time} seconds.")
        if len(self.__errors) > 0:
            print(f"You have errors in {' '.join(str(e) for e in sorted(set(self.__errors)))}'s problem")
        print(f"Your total game points: {self.__points}")
        if self.__points < 0:
            print("You lose the game :(")


game = TimedMathChallenges()
game.play()
game.show_statistics()
os.system("pause")
