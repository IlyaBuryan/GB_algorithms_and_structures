"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random


def random_num(t=1, n=random.randrange(0, 101)):
    print(n)
    if t == 11:
        return 'This was the last try!'
    else:
        try:
            ask = int(input('Enter the number from 0 to 100: '))
            if ask == n:
                return 'Congratulations! You guessed'
            else:
                print('Your number is HIGHER') if ask > n else print('Your number is LOWER')
                print(f'Number of attemps left: {10 - t}\n')
                return random_num(t + 1)
        except:
            print('Please enter the numbers')
            return random_num(t)


print(random_num())
