import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def is_even(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def brain_even(name: str):
    win_count = 0
    right_answer = None
    player_answer = None
    number = None
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while win_count < 3:
        number = random.randint(1, 100)
        print('Question:', number)
        player_answer = prompt.string('Your answer: ')
        right_answer = is_even(number)

        if player_answer != right_answer:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
             print('Correct!')
             win_count += 1
    
    if win_count == 3:
        print(f'Congratulations, {name}!')


def main():
    greet()
    name = welcome_user()
    brain_even(name)


if __name__ == '__main()__':
    main()
