from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.games.games_logic import brain_prime


def main():
    greet()
    name = welcome_user()
    brain_prime(name)
