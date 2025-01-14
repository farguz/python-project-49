from brain_games.games.utilities import (
    VICTORIES_TO_WIN,
    are_wins_enough,
    ask_answer,
    check_user_answer,
    congratulate,
)


def game(start_text: str, name: str, game_name):
    win_count = 0
    print(start_text)

    while win_count < VICTORIES_TO_WIN:
        
        question, right_answer = game_name()
        print('Question:', question)
        player_answer = ask_answer()

        # check_user_answer(player_answer: int | str,
        # right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = (
        check_user_answer(player_answer, right_answer, win_count, name))
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
    
    if are_wins_enough(win_count):
        congratulate(name)
                


