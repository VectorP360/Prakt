from random import sample

letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!\/|#@=+-_*&?'

all_symbols = letters + capital_letters + numbers + symbols

def password_generator(password_length: int): 
    used_letters = False
    used_capital = False
    used_numbers = False
    used_symbols = False


    while not used_letters or not used_capital or not used_numbers or not used_symbols:
        used_letters = False
        used_capital = False
        used_numbers = False
        used_symbols = False

        final_password = "".join(sample(all_symbols, password_length))

        for iteration in final_password:
            if iteration in letters:
                used_letters = True
            if iteration in capital_letters:
                used_capital = True
            if iteration in numbers:
                used_numbers = True
            if iteration in symbols:
                used_symbols = True


    return final_password