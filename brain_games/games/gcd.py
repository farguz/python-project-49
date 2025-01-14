import random

from brain_games.games.engine import game


def calc_gcd() -> tuple:
    RANDOM_START, RANDOM_END = 1, 100
    num1 = random.randint(RANDOM_START, RANDOM_END)
    num2 = random.randint(RANDOM_START, RANDOM_END)
    
    # НОД не может превышать половины бОльшего числа
    # за исключением случая когда числа равны
    if num1 == num2:
        return str(num1) + ' ' + str(num2), str(num1)
    
    for i in range(max(num1, num2) // 2 + 1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return str(num1) + ' ' + str(num2), str(i)


def brain_gcd(name: str):
    start_text = 'Find the greatest common divisor of given numbers.'
    game(start_text, name, calc_gcd)  
