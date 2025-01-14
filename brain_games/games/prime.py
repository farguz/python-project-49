import random

from brain_games.games.engine import game


def is_prime(number: int) -> str:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def generate_number_prime() -> tuple:
    RANDOM_START, RANDOM_END = 1, 100
    number = random.randint(RANDOM_START, RANDOM_END)
    answer = is_prime(number)
    return number, answer


def brain_prime(name: str):
    start_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game(start_text, name, generate_number_prime)
