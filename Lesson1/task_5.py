"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


# Максимально оптимизировал сколько смог и оттестил, все работает.
# Отдельная функция для добавления тарелок с параметром числа тарелок и отдельная для удаления, так же с параметром.
class Plates:
    def __init__(self, stack_volume):
        self.stack = [[]]
        self.stack_volume = stack_volume

    def add_plates(self, number):
        while number:
            if len(self.stack) == 0 or len(self.stack[-1]) == self.stack_volume:
                self.stack.append([])
            while (self.stack_volume - len(self.stack[-1])) > 0 and number > 0:
                self.stack[-1].append(1)
                number -= 1

    def remove_plates(self, number):
        while number and len(self.stack) > 0:
            while len(self.stack[-1]) > 0 and number > 0:
                self.stack[-1].pop()
                number -= 1
            if len(self.stack[-1]) == 0:
                self.stack.pop()

    def print_stack(self):
        print('-----------Стеки тарелок-----------\n'
              '-------Чтобы добавить новые--------\n'
              '-----Вводите a.add_plates(...)-----\n'
              '-------Чтобы удалить текущие-------\n'
              '----Вводите a.remove_plates(...)---\n')
        for i in range(len(self.stack)):
            print(f'Стэк № {i} -- ', *self.stack[i])


if __name__ == '__main__':
    a = Plates(10)

    a.add_plates(1)
    a.add_plates(22)
    a.remove_plates(25)
    a.add_plates(1)
    a.add_plates(10)
    a.remove_plates(5)
    a.add_plates(31)
    a.remove_plates(6)

    a.print_stack()
