import random
import time
import threading
import msvcrt
import sys
import os
operators = ['+', '-', '*']
min_value = 0
max_value = 0

print("Welcome to the Timed mathematical challenges game!")
mode = input("Do you want to set a difficulty for the game? (y/n): ")
#time_lim = 0
if mode.lower() == 'y':
    global time_lim
    time_lim = int(input("Set a time for each question: "))
    min_value = int(input("Input the minimum value: "))  # Convert input to integer
    max_value = int(input("Input the maximum value: "))  # Convert input to integer
elif mode.lower() == 'n':
    print("Default time for each question: 10 seconds")
    print("Default minimum and maximum range: -10 and 5")

    def generate_random_values():
        global min_value, max_value
        min_value = random.randint(-10, 10)
        max_value = random.randint(min_value, 15)
        return min_value, max_value

    min_value, max_value = generate_random_values()
else:
    print("Invalid input. Please enter 'y' or 'n'.")


print("Now you will be presented with a series of math problems.")
time.sleep(0.5)
print("Enter 'n' to skip a problem at a penalty of 10 points.")
print("Enter 'q' to quit the game.")
print("Let's get started!")
time.sleep(0.8)

def generate_problem():
    operator = random.choice(operators)
    left_digit = random.randint(min_value, max_value)
    right_digit = random.randint(min_value, max_value)
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

time_up = False

def timer(stop_timer):
    global time_up
    for remaining in range(time_lim, 0, -1):
        if stop_timer.is_set():
            return
        time.sleep(1)
    stop_timer.set()
    time_up = True

wrong_answers = 0
correct = 0
numbers = 0
skipped = 0
running = True
errors = []

points = 0
start_time = time.time()
while running:
    try:
        problem, answer = generate_problem()
        numbers += 1 
    except:
        continue
    stop_timer = threading.Event()
    timer_thread = threading.Thread(target=timer, args=(stop_timer,))
    timer_thread.start()
    while True:
        try:
            user_answer = input(f"Problem #{numbers}: {problem}: ").rstrip('\n')
            if time_up:
                print("\rTime is up! -5 points! Moving to the next question...")
                points -= 5
                time_up = False
                break
            if user_answer.lower() == 'n':
                skipped += 1
                points -= 10
                stop_timer.set()
                break
            elif user_answer.lower() == 'q':
                if wrong_answers == 0:
                    numbers -= 1
                running = False
                stop_timer.set()
                break
            user_answer = int(user_answer)
            if answer == user_answer:
                print("Congratulations! +10 points")
                correct += 1
                points += 10
                stop_timer.set()
                break
            else:
                print("Ooops! Try again! -5 points")
                points -= 5
                wrong_answers += 1
                errors.append(numbers)
        except ValueError:
            print("Invalid output. Enter an integer. -3 points")
            points-=3
end_time = time.time()
total_time = round(end_time - start_time,3)
print("Game over!")
print(f"You have:\n {correct} correct answers \n {wrong_answers} wrong answers \n {numbers} total questions \n {skipped} skipped questions \n in total {total_time} seconds.")
if len(errors) > 0:
    print(f"You have errors in {' '.join( str(e) for e in sorted(set(errors)))}'s problem")
print(f"Your total game points: {points}")
if points < 0:
    print("You lose the game :(")

os.system("pause")