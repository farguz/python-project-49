from brain_games.games.engine import check_user_answer, congratulate


def is_prime(number: int) -> str:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


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

        # check_user_answer(player_answer: int | str,
        # right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = (
        check_user_answer(player_answer, right_answer, win_count, name))
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)
