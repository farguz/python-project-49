from brain_games.cli import welcome_user
from brain_games.games.games_logic import brain_prime
from brain_games.scripts.brain_games import greet


def main():
    greet()
    name = welcome_user()
    brain_prime(name)
