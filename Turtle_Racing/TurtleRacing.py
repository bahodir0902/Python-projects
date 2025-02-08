import turtle
import time
import random
#import os

COLORS = ['red', 'green', 'blue', 'yellow', 'pink', 'brown', 'gray', 'black', 'cyan', 'orange']
WIDTH, HEIGHT = 500,500

def get_num_of_turtles():
    while True:
        num = input("Enter how many turtles do you want to be raced? (2-10): ")
        if num.isdigit():
            num = int(num)
            if 2 <= num <= 10:
                break
            else:
                print("The number of turtles should be in range 2-10.")
                continue
        else:
            print("Invalid input. Enter an integer.")
            
    return num

def create_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing game")
    
def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        turtles.append(racer)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT// 2 + 20)
        racer.pendown()
    return turtles
    
def race(colors):
    turtles = create_turtles(colors)
    start_time = time.time()
    while True:
        for racer in turtles:
            distance = random.randrange(1,15)
            racer.forward(distance)
            x,y = racer.pos()
            if y >= (HEIGHT // 2 - 10):
                end_time = time.time()
                total_time = end_time - start_time
                total_time = round(total_time, 3)
                return colors[turtles.index(racer)], total_time

    
racers = get_num_of_turtles()
create_screen()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner, timer = race(colors)
print(f"The winner of the turtle racing game is the turtle with color '{winner}' in {timer} seconds")



turtle.mainloop()

#os.system("pause")