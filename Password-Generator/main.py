from random import choice, shuffle
from pyperclip import copy

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

ASCII_TEXT = """
    ____     ___    _____   _____ _       __   ____     ____     ____           ______    ______    _   __    ______    ____     ___   ______   ____     ____
   / __ \   /   |  / ___/  / ___/| |     / /  / __ \   / __ \   / __ \         / ____/   / ____/   / | / /   / ____/   / __ \   /   | /_  __/  / __ \   / __ |
  / /_/ /  / /| |  \__ \   \__ \ | | /| / /  / / / /  / /_/ /  / / / /        / / __    / __/     /  |/ /   / __/     / /_/ /  / /| |  / /    / / / /  / /_/ /
 / ____/  / ___ | ___/ /  ___/ / | |/ |/ /  / /_/ /  / _, _/  / /_/ /        / /_/ /   / /___    / /|  /   / /___    / _, _/  / ___ | / /    / /_/ /  / _, _/
/_/      /_/  |_|/____/  /____/  |__/|__/   \____/  /_/ |_|  /_____/         \____/   /_____/   /_/ |_/   /_____/   /_/ |_|  /_/  |_|/_/     \____/  /_/ |_|

"""
print(ASCII_TEXT)


def random_char(password_len, letters_len, numbers_len, symbols_len):
    if password_len == (letter_len + number_len + symbol_len):
        letter_gen = [choice(letters) for _ in range(letters_len)]
        number_gen = [choice(numbers) for _ in range(numbers_len)]
        symbol_gen = [choice(symbols) for _ in range(symbols_len)]

        password_list = letter_gen + number_gen + symbol_gen
        shuffle(password_list)
        password = ''.join(password_list)
        return password
    else:
        print('Length of password is not equal to the number of letters, numbers and symbols.')

pass_len = int(input('Length of the Password: '))
letter_len = int(input('Number of letters needed: '))
number_len = int(input('Number of numbers needed: '))
symbol_len = int(input('Number of symbols needed: '))

password = random_char(pass_len, letter_len, number_len, symbol_len)
if password:
    print(password)
    while True:
        next_step = input("If you want to copy to your clipboard enter 'copy' or 'again' to Generate password again or 'exit' to exit: ").lower()
        if next_step == 'copy':
            copy(password)
            print('✅Done')
        elif next_step == 'again':
            password = random_char(pass_len, letter_len, number_len, symbol_len)
            print(password)

        elif next_step == 'exit':
            print('Thank You!')
            break
        else:
            print('Wrong input try again!')


