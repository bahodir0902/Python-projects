import string
import random

def generate_password(password_length, include_numbers=True, include_special_chars=True):
    all_possible_letters = string.ascii_letters
    all_possible_digits = string.digits
    all_possible_special_chars = string.punctuation
    
    pool_of_possible_chars = all_possible_letters
    if include_numbers:
        pool_of_possible_chars += all_possible_digits
    if include_special_chars:
        pool_of_possible_chars += all_possible_special_chars
    
    generated_password = ""
    does_password_meet_criteria = False
    does_password_have_number = False
    does_password_have_special_char = False
    
    while not does_password_meet_criteria:
        generated_password = ""
        for _ in range(password_length):
            new_char = random.choice(pool_of_possible_chars)
            generated_password += new_char
            
            if new_char in all_possible_digits:
                does_password_have_number = True
            elif new_char in all_possible_special_chars:
                does_password_have_special_char = True
                
        does_password_meet_criteria = True
        if include_numbers:
            does_password_meet_criteria = does_password_have_number
        if include_special_chars:
            does_password_meet_criteria = does_password_meet_criteria and does_password_have_special_char

    return generated_password

print(generate_password(500000))
