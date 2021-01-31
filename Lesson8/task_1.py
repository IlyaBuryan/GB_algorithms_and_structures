"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import Counter, deque


class Huffman:
    def __init__(self, input_):
        self.input_ = input_
        self.counted_arr = None
        self.counted_arr_new = None
        self.weight = None

    """ Returns counted frequency of symbols in the sorted deque """

    def counter(self):
        self.counted_arr = Counter(self.input_)
        self.counted_arr = deque(sorted(self.counted_arr.items(), key=lambda i: i[1]))
        self.counted_arr_new = self.counted_arr

    """ Returns the dict with inside dicts - unpacked Tree """

    def main_calculation(self):
        while len(self.counted_arr_new) > 1:
            self.weight = self.counted_arr_new[0][1] + self.counted_arr_new[1][1]
            self.counted_arr_new.appendleft((dict([(0, self.counted_arr_new[0][0]), (1, self.counted_arr_new[1][0])]),
                                             self.weight))
            self.counted_arr_new = deque(sorted(self.counted_arr_new, key=lambda i: i[1]))
            self.counted_arr_new.popleft()
            self.counted_arr_new.popleft()
        self.counted_arr_new = self.counted_arr_new[0][0]

    """ Returns the dict with Tree """

    @staticmethod
    def huffman_code(tree, path='', encrypted_table={}):
        if not isinstance(tree, dict):
            encrypted_table[tree] = path
        else:
            Huffman.huffman_code(tree[0], path=f'{path}0')
            Huffman.huffman_code(tree[1], path=f'{path}1')
        return encrypted_table

    """ Execute all functions and print the result """

    def execute_and_print(self):
        self.counter()
        self.main_calculation()
        print(f'Таблица кодировки: {self.huffman_code(self.counted_arr_new)}')


if __name__ == '__main__':
    ex = Huffman('beep boop beer!')
    ex.execute_and_print()
