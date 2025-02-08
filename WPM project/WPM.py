import curses
import random
import time
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typeing Test!!!")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getkey()

def print_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}")
    
    for i,char in enumerate(current):
        color = curses.color_pair(1)
        if char != target[i]:
            color = curses.color_pair(2)
        stdscr.addstr(0,i, char, color)
def load():
    try:    
        with open('database.txt', 'r') as file:
            lines = file.readlines()
            return random.choice(lines).strip()
        
    except FileNotFoundError:
        with open('database.txt', 'w') as file:
            file.write("")
            
def wpm(stdscr):
    target_text = load()
    current_text = []
    total_chars = 0
    mistakes = 0
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while True:
        elapsed_time = max(time.time() - start_time, 1)
        correct_chars = total_chars - mistakes
        wpm = round((correct_chars / (elapsed_time / 60)) / 5)
        stdscr.clear()
        
        print_text(stdscr, target_text, current_text, wpm)
          
        stdscr.refresh()
        
        
        if correct_chars == len(target_text):
            break
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        if key in('BACKSPACE', '\b', '\x7f'):
            if len(current_text) > 0:
                if current_text[-1] != target_text[len(current_text)-1]:
                    mistakes -= 1
                current_text.pop()
                total_chars -= 1
        elif len(current_text) < len(target_text):
            current_text.append(key)
            total_chars += 1
            if key != target_text[len(current_text)-1]:
                mistakes += 1
    return wpm

def main(stdscr):
    curses.curs_set(0) # Make cursor invisible

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    start_screen(stdscr)   
    words = wpm(stdscr)
    print(f"Your total Words Per Minute score is: {words}")
wrapper(main)


input()