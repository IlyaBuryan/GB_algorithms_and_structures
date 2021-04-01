"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""


# Решил сделать через ООП, чтобы потренироваться. Задействован defaultdict.
# Проверок ввода не добавлял, сконцентрировавшись только на функции.


from collections import defaultdict


class Companies:

    def __init__(self):
        try:
            self.companies_num = int(input('Введите количество предприятий для расчета прибыли: '))
        except:
            print("Вы ввели не число! Попробуйте еще раз")
            self.__init__()
        self.income_base = defaultdict(list)
        self.calculated_income_base = defaultdict(int)
        self.Totally_average = 0
        self.more_average_inc = []
        self.less_average_inc = []

    def write_companies(self):
        for _ in range(self.companies_num):
            self.name = input('Введите название предприятия: ')
            self.income = list(map(int, input('Через пробел введите прибыль данного предприятия за каждый '
                                              'квартал (Всего 4 квартала): ').split()))
            self.income_base[self.name] = self.income

    def calc_year_income(self):
        for k, v in self.income_base.items():
            self.calculated_income_base[k] = sum(v)
        self.Totally_average = sum(self.calculated_income_base.values()) / len(self.income_base)

    def print_total(self):
        print(f'Средняя годовая прибыль всех предприятий: '
              f'{round(sum(self.calculated_income_base.values()) / len(self.calculated_income_base), 2)}')

    def print_more_less_average_income(self):
        for k, v in self.calculated_income_base.items():
            if v > self.Totally_average:
                self.more_average_inc.append(k)
            elif v < self.Totally_average:
                self.less_average_inc.append(k)
        if self.more_average_inc:
            print(f'Предприятия, с прибылью выше среднего значения: {"  |  ".join(self.more_average_inc)}')
        if self.less_average_inc:
            print(f'Предприятия, с прибылью ниже среднего значения: {"  |  ".join(self.less_average_inc)}')


if __name__ == '__main__':
    a = Companies()
    a.write_companies()
    a.calc_year_income()
    a.print_total()
    a.print_more_less_average_income()
