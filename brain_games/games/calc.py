from brain_games.games.engine import check_user_answer, congratulate


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

        # check_user_answer(player_answer: int | str,
        # right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = (
        check_user_answer(player_answer, right_answer, win_count, name))
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)
