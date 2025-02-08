import random
import os

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000
ROWS = 3
COLS = 3

symbols = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}
symbols_value = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_win(columns, lines, bet,value):
    points = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            points += value[symbol] * bet
            winning_line.append(line + 1)
            
    return points, winning_line

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for key,value in symbols.items():
        for _ in range(value):
            all_symbols.append(key)
    colums = []  
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        colums.append(column)
    return colums

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()
        
def put_balance():
    while True:
        amount = input("How much do you want to put in slot machine? $")
        if amount.isdigit():
            amount = int(amount)
            if amount < 0:
                print("The balance should be greater than 0.")
            else:
                break
        else:
            print("Invalid input. Try again!")
    return amount

def get_lines():
    while True:
        lines = input("How many lines do you want to put? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"The balance should be greater than 1 and less than {MAX_LINES}.")
        else:
            print("Invalid input. Try again!")
    return lines


def put_bet():
    while True:
        amount = input("How much do you want to put a bet? $")
        if amount.isdigit():
            amount = int(amount)
            if not (MIN_BET <= amount <= MAX_BET):
                print(f"The balance should be greater than {MIN_BET} and less than {MAX_BET}.")
            else:
                break
        else:
            print("Invalid input. Try again!")
    return amount

def game(balance):
    while True:
        lines = get_lines()
        bet = put_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"Invalid numbers! You don't have enough balance, the total bet should be less than {balance}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machine(slots)
    win, win_line = check_win(slots, lines, bet, symbols_value)
    print(f"You won ${win}.")
    if win_line:
        print("You won on lines", *win_line)
    return win - total_bet

balance = put_balance()

while True:
    print(f"Current balance is ${balance}")
    spin = input("Press enter to spin a slot machine(q to quit the game).")
    if spin.lower() == 'q':
        break
    balance += game(balance)
    if balance < 0:
        break
print(f"You left with {balance}")



os.system("pause")
