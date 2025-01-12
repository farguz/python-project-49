from brain_games.games.utilities import (
    VICTORIES_TO_WIN,
    are_wins_enough,
    ask_answer_int,
    ask_answer_str,
    calc_gcd,
    check_user_answer,
    congratulate,
    create_progression,
    generate_expression,
    generate_number_even,
    generate_number_prime,
)


def game(start_text: str, name: str = 'PLAYER'):
    win_count = 0

    print(start_text)

    while win_count < VICTORIES_TO_WIN:
        match start_text:
            case 'What is the result of the expression?':
                question, right_answer = generate_expression()
                print('Question:', question)
                player_answer = ask_answer_int()

            case 'What number is missing in the progression?':
                question, right_answer = create_progression()
                print('Question:', ' '.join(question))
                player_answer = ask_answer_int()

            case 'Answer "yes" if given number is prime. \
Otherwise answer "no".':
                question, right_answer = generate_number_prime()
                print('Question:', question)
                player_answer = ask_answer_str()

            case 'Find the greatest common divisor of given numbers.':
                question, right_answer = calc_gcd()
                print('Question:', question)
                player_answer = ask_answer_int()

            case 'Answer "yes" if the number is even, otherwise answer "no".':
                question, right_answer = generate_number_even()
                print('Question:', question)
                player_answer = ask_answer_str()

            case _:
                pass
        
        # check_user_answer(player_answer: int | str,
        # right_answer: int | str, win_count: int, name: str) -> tuple
        correctness_flag, win_count = (
        check_user_answer(player_answer, right_answer, win_count, name))
        
        # if answer is incorrect the game is over
        if not correctness_flag:
            break
    
    if are_wins_enough(win_count):
        congratulate(name)
                


