"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

from random import sample


# Так как задачка решается в простой сложности. То было непросто придумать как написать в квадратичной :)
# Из разных решений, которые перепробовал это, наверное, самое лучшее со сложностью N^2, как по условию
def first_min_one(a_list: list):
    try:
        k = 0
        for i in range(1, len(a_list)):
            if a_list[k] < a_list[k + 1]:
                a_list.remove(a_list[k + 1])
            else:
                a_list.remove(a_list[k])
        return a_list[0]
    except IndexError:
        print("The list is empty")


# Со сложностью N через цикл
def second_min_one(a_list: list):
    try:
        minimum = a_list[0]
        for i in a_list[1:]:
            if i < minimum:
                minimum = i
        return minimum
    except IndexError:
        print("The list is empty")


# Со сложностью N через min
def second_min_two(a_list: list):
    try:
        return min(a_list)
    except ValueError:
        print("The list is empty")


# Создание списка через генераторное выражение
a_list = [i for i in sample(range(-1000, 1000), 10)]

# Вывод сформированного списка с последующим выводом результатов каждой функции
print(a_list)
print(first_min_one(a_list))
print(second_min_one(a_list))
print(second_min_two(a_list))
