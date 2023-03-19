import numpy as np
from os import system

# defining global variables
help_message = 'This is a game where you are trying to guess a integer randomly selected by computer, after every ' \
               'unsuccessful guess your score is reduced and you are given a new random clue \n'
win_num = np.random.randint(1, 101, 1)
score = 1000
list_of_guesses = []


def get_a_number() -> int:
    """Function that gets the input from a player and returns it"""
    while True:
        num = input("Guess an integer between 1 and 100, type help to get info, type exit to quit ")
        system('cls')
        if num == 'exit':
            exit()
        if num == 'help':
            print(help_message)
            continue
        try:
            num = int(num)
        except:
            print('This is not a integer\n')
            continue
        if type(num) == int and 1 <= num <= 100:
            break
        else:
            print('Incorrect integer\n')
    return num


def give_a_clue(guessed_number: int):
    """Function that prints out one of four random clues

    First type of clue - is guessed number bigger or smaller than winning number
    Second type of clue - is guessed number in random range from winning number
    Third type of clue - is guessed number multiplied by 3 bigger or smaller than winning number
    Fourth type of clue - is guessed number divided by 2 bigger or smaller than winning number

    Parameters:
    guessed_number (int): Number that player guessed
    """
    clue_number = np.random.randint(1, 5, 1)
    if clue_number == 1:
        if guessed_number > win_num:
            print('Your guess is bigger than the winning number\n')
        else:
            print('Your guess is smaller than the winning number\n')
    if clue_number == 2:
        range_of_numbers = np.random.randint(5, 40, 1)
        if guessed_number in np.arange(start=win_num - range_of_numbers, stop=win_num + range_of_numbers + 1):
            print('Your guess is in range of {} from winning number\n'.format(range_of_numbers))
        else:
            print('Your guess is not in range of {} from winning number\n'.format(range_of_numbers))
    if clue_number == 3:
        if 3 * guessed_number > win_num:
            print('Yours guess multiplied by 3 is bigger than the winning number\n')
        else:
            print('Yours guess multiplied by 3 is smaller than the winning number\n')
    if clue_number == 4:
        if guessed_number / 2 < win_num:
            print("Your guess divided by 2 is smaller than the winning number\n")
        else:
            print("Your guess divided by 2 is bigger than the winning number\n")


# game module
while True:
    guess = get_a_number()
    if win_num == guess:
        print('Congratulation you\'ve won, your score is {}'.format(score))
        input("Type anything to quit")
        exit()
    list_of_guesses.append(guess)
    score -= 100
    give_a_clue(guess)
    print('list of previously guessed numbers {}\n'.format(list_of_guesses))
