import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def calc_result(num1: int, sign: str, num2: int) -> int:
    res = 0
    if sign == '*':
        res = num1 * num2
    elif sign == '+':
        res = num1 + num2
    elif sign == '-':
        res = num1 - num2
    return res
    
def brain_calc(name: str):
    number_1, number_2, sign = None, None, None
    win_count = 0
    print('What is the result of the expression?')
          
    while win_count < 3:
        number_1 = random.randint(5, 35)
        number_2 = random.randint(0, number_1)
        sign = random.choice('+-*')

        print('Question:', number_1, sign, number_2)
        player_answer = prompt.integer('Your answer: ')
        right_answer = calc_result(number_1, sign, number_2)

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
    brain_calc(name)


if __name__ == '__main()__':
    main()
