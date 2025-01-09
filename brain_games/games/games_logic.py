import random
import prompt

from brain_games.games.engine import check_user_answer, congratulate


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


def calc_gcd(num1: int, num2: int) -> int:
    # НОД не может превышать половины бОльшего числа
    # за исключением случая когда числа равны
    if num1 == num2:
        return num1
    
    for i in range(max(num1, num2) // 2 + 1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


def hide_one_num(progression: list) -> tuple:
    hidden_item = random.randint(1, len(progression) - 1)
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


def calc_result(num1: int, sign: str, num2: int) -> int:
    res = 0
    if sign == '*':
        res = num1 * num2
    elif sign == '+':
        res = num1 + num2
    elif sign == '-':
        res = num1 - num2
    return res


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

        # check_user_answer(player_answer: int | str, right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = check_user_answer(player_answer, right_answer, win_count, name)
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)


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

        # check_user_answer(player_answer: int | str, right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = check_user_answer(player_answer, right_answer, win_count, name)
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)


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

        # check_user_answer(player_answer: int | str, right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = check_user_answer(player_answer, right_answer, win_count, name)
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)


def brain_progression(name: str):
    win_count = 0
    length = random.randint(5, 10)
    print('What number is missing in the progression?')
              
    while win_count < 3:
        progression, right_answer = create_progression(length)
        print('Question:', ' '.join(progression))
        player_answer = prompt.integer('Your answer: ')

        # check_user_answer(player_answer: int | str, right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = check_user_answer(player_answer, right_answer, win_count, name)
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)


def brain_prime(name: str):
    win_count = 0
    right_answer = None
    player_answer = None
    number = None
    correctness_flag = None
    
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while win_count < 3:
        number = random.randint(1, 100)
        print('Question:', number)
        player_answer = prompt.string('Your answer: ')
        right_answer = is_prime(number)

        # check_user_answer(player_answer: int | str, right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = check_user_answer(player_answer, right_answer, win_count, name)
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)
