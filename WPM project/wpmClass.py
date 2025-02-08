import curses
import time
import random
from curses import wrapper

class SpeedTypingTest:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.target_text = self.load()
        self.current_text = []
        self.total_chars = 0
        self.mistakes = 0
        self.wpm = 0
        self.start_time = time.time()

    def start_screen(self):
        self.stdscr.clear()
        self.stdscr.addstr("Welcome to Speed Typing Test!!!")
        self.stdscr.addstr("\nPress any key to continue...")
        self.stdscr.refresh()
        self.stdscr.getkey()

    def print_text(self):
        # Get the size of the terminal window
        height, width = self.stdscr.getmaxyx()
    
        self.stdscr.addstr(0, 0, self.target_text)
        for i, char in enumerate(self.current_text):
            color = curses.color_pair(1)
            if char != self.target_text[i]:
                color = curses.color_pair(2)
            self.stdscr.addstr(i // width, i % width, char, color)
    
        # Calculate the line where the WPM should be printed
        wpm_line = len(self.target_text) // width + 1
    
        # Print the WPM on a new line after the sentence
        self.stdscr.addstr(wpm_line, 0, f"WPM: {self.wpm}")





    def calculate_wpm(self):
        elapsed_time = max(time.time() - self.start_time, 1)
        correct_chars = self.total_chars - self.mistakes
        self.wpm = round((correct_chars / (elapsed_time / 60)) / 5)

    
    '''def load(self):
        try:    
            with open('database.txt', 'r') as file:
                lines = file.readlines()
                return random.choice(lines).strip()
            
        except FileNotFoundError:
            with open('database.txt', 'w') as file:
                file.write("") '''
                    
    def load(self):
        try:    
            with open('database.txt', 'r') as file:
                content = file.read()
                sentences = content.split('.')
                # Remove any empty strings from the list of sentences
                sentences = [sentence for sentence in sentences if sentence]
                return random.choice(sentences).strip()
                    
        except FileNotFoundError:
            with open('database.txt', 'w') as file:
                file.write("")

          
    def run(self):
        self.stdscr.nodelay(True)
        while True:
            self.calculate_wpm()
            self.stdscr.clear()
            self.print_text()
            self.stdscr.refresh()
            
            if self.total_chars - self.mistakes == len(self.target_text):
                break
            try:
                key = self.stdscr.getkey()
            except:
                continue
            
            if ord(key) == 27:
                break
            if key in('BACKSPACE', '\b', '\x7f'):
                if len(self.current_text) > 0:
                    if self.current_text[-1] != self.target_text[len(self.current_text)-1]:
                        self.mistakes -= 1
                    self.current_text.pop()
                    self.total_chars -= 1
            elif len(self.current_text) < len(self.target_text):
                self.current_text.append(key)
                self.total_chars += 1
                if key != self.target_text[len(self.current_text)-1]:
                    self.mistakes += 1

        return self.wpm

def main(stdscr):
    curses.curs_set(0) # Make cursor invisible
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    game = SpeedTypingTest(stdscr)
    game.start_screen()
    words = game.run()
    print(f"Your total Words Per Minute score is: {words}")

wrapper(main)

input()