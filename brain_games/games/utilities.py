import random

import prompt

VICTORIES_TO_WIN = 3


def calc_result(num1: int, sign: str, num2: int) -> int:
    res = 0
    if sign == '*':
        res = num1 * num2
    elif sign == '+':
        res = num1 + num2
    elif sign == '-':
        res = num1 - num2
    return res


def is_prime(number: int) -> str:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def is_even(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def hide_one_num(progression: list) -> tuple:
    # hide one item in the middle of progression - not first, not last
    hidden_item = random.randint(1, len(progression) - 1)
    hidden_num = int(progression[hidden_item])
    progression[hidden_item] = '..'
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

    for i in range(length):
        res.append(str(num))
        # calc_result(num1: int, sign: str, num2: int) -> int:
        num = calc_result(num, algorythm, step)
    
    res, answer = hide_one_num(res)

    return res, answer


def check_user_answer(player_answer: int | str, right_answer: int | str,
                      win_count: int, name: str) -> tuple:
    '''
    The function checks the user's answer.
    If it is correct, increases the win counter by 1.
    ''' 
    flag = True
    if player_answer != right_answer:
        print(f"'{player_answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {name}!")
        flag = False
    else:
        print('Correct!')
        win_count += 1
    return flag, win_count


def congratulate(name: str):
    print(f'Congratulations, {name}!')


def are_wins_enough(win_count: int) -> bool:
    if win_count == VICTORIES_TO_WIN:
        return True
    else:
        return False
    

def ask_answer_int() -> int:
    player_answer = prompt.integer('Your answer: ')
    return player_answer


def ask_answer_str() -> str:
    player_answer = prompt.string('Your answer: ')
    return player_answer

    
def generate_expression() -> tuple:
    # 1st number from 5 to 35, 2nd from 0 to number #1. For easy solutions
    RANDOM_START, RANDOM_END, RANDOM_START_2 = 5, 35, 0
    number_1 = random.randint(RANDOM_START, RANDOM_END)
    number_2 = random.randint(RANDOM_START_2, number_1)
    sign = random.choice('+-*')
    expression = str(number_1) + ' ' + sign + ' ' + str(number_2)
    answer = calc_result(number_1, sign, number_2)
    return expression, answer


def generate_number_prime() -> tuple:
    RANDOM_START, RANDOM_END = 1, 100
    number = random.randint(RANDOM_START, RANDOM_END)
    answer = is_prime(number)
    return number, answer


def generate_number_even() -> tuple:
    RANDOM_START, RANDOM_END = 1, 100
    number = random.randint(RANDOM_START, RANDOM_END)
    answer = is_even(number)
    return number, answer


def calc_gcd() -> tuple:
    RANDOM_START, RANDOM_END = 1, 100
    num1 = random.randint(RANDOM_START, RANDOM_END)
    num2 = random.randint(RANDOM_START, RANDOM_END)
    
    # НОД не может превышать половины бОльшего числа
    # за исключением случая когда числа равны
    if num1 == num2:
        return str(num1) + ' ' + str(num2), num1
    
    for i in range(max(num1, num2) // 2 + 1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return str(num1) + ' ' + str(num2), i
