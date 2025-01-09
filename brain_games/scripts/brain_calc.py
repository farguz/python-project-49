from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.games.games_logic import brain_calc


def main():
    greet()
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main()__':
    main()
