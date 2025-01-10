from brain_games.games.engine import check_user_answer, congratulate
from brain_games.games.calc import calc_result


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


def brain_progression(name: str):
    win_count = 0
    length = random.randint(5, 10)
    print('What number is missing in the progression?')
              
    while win_count < 3:
        progression, right_answer = create_progression(length)
        print('Question:', ' '.join(progression))
        player_answer = prompt.integer('Your answer: ')

        # check_user_answer(player_answer: int | str,
        # right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = (
        check_user_answer(player_answer, right_answer, win_count, name))
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)
