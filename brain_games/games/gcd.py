from brain_games.games.engine import check_user_answer, congratulate


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

        # check_user_answer(player_answer: int | str,
        # right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = (
        check_user_answer(player_answer, right_answer, win_count, name))
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
 
    if win_count == 3:
        congratulate(name)