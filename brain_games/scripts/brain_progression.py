from brain_games.cli import welcome_user
from brain_games.games.progression import brain_progression
from brain_games.scripts.brain_games import greet


def main():
    greet()
    name = welcome_user()
    brain_progression(name)


if __name__ == '__main()__':
    main()
