"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

"""
Написал в ООП, чтобы потренироваться и не делать простую перегрузку.

Использовал 2 изученных типа namedtuple и defaultdict. На выходе необходимый формат. 
"""

from collections import namedtuple, defaultdict


class Numbers:
    def __init__(self):
        self.pattern = namedtuple('Numbers', 'Number1 Number2')
        self.save = self.pattern(Number1=list(input('Введите 1-е число в 16-ричном формате: ')),
                                 Number2=list(input('Введите 2-е число в 16-ричном формате: ')))
        self.num_sum = defaultdict(str)
        self.num_mul = defaultdict(str)

    def in_num(self):
        for i in hex(int("".join(self.save.Number1), 16) + int("".join(self.save.Number2), 16))[2:]:
            self.num_sum[i.upper()] = ''
        for i in hex(int("".join(self.save.Number1), 16) * int("".join(self.save.Number2), 16))[2:]:
            self.num_mul[i.upper()] = ''

    def print(self):
        print('Число 1: ', self.save.Number1)
        print('Число 2: ', self.save.Number2, '\n')
        print('Сумма: ', list(self.num_sum.keys()))
        print('Произведение: ', list(self.num_mul.keys()))


if __name__ == '__main__':
    ex = Numbers()
    ex.in_num()
    ex.print()
