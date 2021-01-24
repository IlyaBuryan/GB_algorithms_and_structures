"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

"""
Сортировка по убыванию реализована путем изменения знака сравнения с больше на меньше.

Реализована идея для доработки с break. перед каждым проходом ставим переменную check_var в значение True.
Если случается хоть 1 замена ее значение меняется на False. 
После цикла проверяем значение check_var и если оно осталось True (то есть не было ни одной перестановки), то
реализуется break. (в интернете найдено несколько вариантов этого улучшения)

Замеры разницы во времени показывают, что это улучшение дает небольшое и нестабильное сокращение времени работы 
сортировки.

Результат: разница между старой функцией без break и новой функцией с break (на сколько вторая быстрее первой).
Выигрыш растет с ростом массива сортировки:
List(100)    -7.256899999999802e-05
List(1000)   -0.0028207399999999883
List(10000)  -0.11669404200000155

Но все равно, оптимизацию, полагаю, стоит использовать
"""

import timeit
import random


def bubble_sort_old(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]: # для сортировки по убыванию изменен только знак
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        check_var = True  # New
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:  # для сортировки по убыванию изменен только знак
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                check_var = False  # New
        if check_var:  # New
            break  # New
        n += 1

    return lst_obj


orig_list1 = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print('List(100)   ', timeit.timeit("bubble_sort_old(orig_list1.copy())",
                                   setup="from __main__ import bubble_sort_old, orig_list1", number=1) -
                      timeit.timeit("bubble_sort(orig_list1.copy())",
                                   setup="from __main__ import bubble_sort, orig_list1", number=1))

orig_list2 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print('List(1000)  ', timeit.timeit("bubble_sort_old(orig_list2.copy())",
                                   setup="from __main__ import bubble_sort_old, orig_list2", number=1) -
                      timeit.timeit("bubble_sort(orig_list2.copy())",
                                   setup="from __main__ import bubble_sort, orig_list2", number=1))

orig_list3 = [random.randint(-100, 100) for _ in range(10000)]

# замеры 10000
print('List(10000) ', timeit.timeit("bubble_sort_old(orig_list3.copy())",
                                   setup="from __main__ import bubble_sort_old, orig_list3", number=1) -
                      timeit.timeit("bubble_sort(orig_list3.copy())",
                                   setup="from __main__ import bubble_sort, orig_list3", number=1))

print('Исходный:        ', orig_list1)
print('Отсортированный: ', bubble_sort(orig_list1.copy()))
print('Исходный:        ', orig_list2)
print('Отсортированный: ', bubble_sort(orig_list2.copy()))
print('Исходный:        ', orig_list3)
print('Отсортированный: ', bubble_sort(orig_list3.copy()))
