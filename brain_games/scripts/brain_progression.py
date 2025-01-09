import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_calc import calc_result
from brain_games.scripts.brain_games import greet


def hide_one_num(progression: list) -> tuple:
    hidden_item = random.randint(1, len(progression))
    hidden_num = int(progression[hidden_item])
    progression[hidden_item] = '..'
    return progression, hidden_num


def create_progression(length: int) -> tuple:
    res = []
    num = random.randint(1, 100)
    algorythm = random.choice('+-')
    step = random.randint(1, 5)

    for i in range(length):
        res.append(str(num))
        # calc_result(num1: int, sign: str, num2: int) -> int:
        num = calc_result(num, algorythm, step)
    
    res, answer = hide_one_num(res)

    return res, answer


def brain_progression(name: str):
    win_count = 0
    length = random.randint(5, 10)
    print('What number is missing in the progression?')
              
    while win_count < 3:
        progression, right_answer = create_progression(length)
        print('Question:', ' '.join(progression))
        player_answer = prompt.integer('Your answer: ')

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
    brain_progression(name)


if __name__ == '__main()__':
    main()
