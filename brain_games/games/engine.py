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