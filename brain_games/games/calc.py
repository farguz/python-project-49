import random

from brain_games.games.engine import game


def generate_expression() -> tuple:
    # 1st number from 5 to 35, 2nd from 0 to number #1. For easy solutions
    RANDOM_START, RANDOM_END, RANDOM_START_2 = 5, 35, 0
    number_1 = random.randint(RANDOM_START, RANDOM_END)
    number_2 = random.randint(RANDOM_START_2, number_1)
    sign = random.choice('+-*')
    expression = str(number_1) + ' ' + sign + ' ' + str(number_2)
    answer = calc_result(number_1, sign, number_2)
    return expression, str(answer)


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
    start_text = 'What is the result of the expression?'
    game(start_text, name, generate_expression)
