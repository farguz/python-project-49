from brain_games.games.engine import game


def brain_prime(name: str):
    start_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game(start_text, name)
