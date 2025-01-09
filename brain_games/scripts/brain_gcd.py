import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def calc_gcd(num1: int, num2: int) -> int:
    # НОД не может превышать половины бОльшего числа
    # за исключением случая когда числа равны
    if num1 == num2:
        return num1
    
    for i in range(max(num1, num2) // 2 + 1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


def brain_gcd(name: str):
    number_1, number_2 = None, None
    win_count = 0
    print('Find the greatest common divisor of given numbers.')
          
    while win_count < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)

        print('Question:', number_1, number_2)
        player_answer = prompt.integer('Your answer: ')
        right_answer = calc_gcd(number_1, number_2)

        if player_answer != right_answer:
            print(f"'{player_answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
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
    brain_gcd(name)


if __name__ == '__main()__':
    main()
