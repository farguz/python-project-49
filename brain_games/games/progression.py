import random

from brain_games.games.calc import calc_result
from brain_games.games.engine import game


def hide_one_num(progression: list) -> tuple:
    # hide one item in the middle of progression - not first, not last
    hidden_item = random.randint(1, len(progression) - 1)
    hidden_num = int(progression[hidden_item])
    progression[hidden_item] = '..'
    progression = ' '.join(progression)
    return progression, hidden_num


def create_progression() -> tuple:
    # modify const to change difficulty
    RANDOM_LENGTH_START, RANDOM_LENGTH_END = 5, 10
    RANDOM_NUM_START, RANDOM_NUM_END = 1, 100
    RANDOM_STEP_START, RANDOM_STEP_END = 1, 5

    res = []
    length = random.randint(RANDOM_LENGTH_START, RANDOM_LENGTH_END)
    num = random.randint(RANDOM_NUM_START, RANDOM_NUM_END)
    algorythm = random.choice('+-')
    step = random.randint(RANDOM_STEP_START, RANDOM_STEP_END)

    for _ in range(length):
        res.append(str(num))
        # calc_result(num1: int, sign: str, num2: int) -> int:
        num = calc_result(num, algorythm, step)
    
    res, answer = hide_one_num(res)

    return res, str(answer)


def brain_progression(name: str):
    start_text = 'What number is missing in the progression?'
    game(start_text, name, create_progression)
