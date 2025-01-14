import random

from brain_games.games.engine import game


def generate_number_even() -> tuple:
    RANDOM_START, RANDOM_END = 1, 100
    number = random.randint(RANDOM_START, RANDOM_END)
    answer = is_even(number)
    return number, answer


def is_even(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
    

def brain_even(name: str):
    start_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    game(start_text, name, generate_number_even)  
