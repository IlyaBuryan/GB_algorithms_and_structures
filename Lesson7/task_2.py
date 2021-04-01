"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

"""
В интеренете нашел и разобрал много решений, но, наверное, самым простым мне показалось текущее, с разбивкой на
2 функции. При этом хорошей "фишкой" является то, что функция работает как sorted(), не изменяя изначальный массив.

Алгоритм достаточно быстрый, даже при большом списке.

t сортировки list(100 el):    0.0002279199999999995
t сортировки list(1000 el):   0.0029476460000000017
t сортировки list(10000 el):  0.038544403
"""


import random
import timeit


def merge_sort(L):
    if len(L) < 2:
        return L
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


orig_list1 = [random.random() * 50 for _ in range(100)]
orig_list2 = [random.random() * 50 for _ in range(1000)]
orig_list3 = [random.random() * 50 for _ in range(10000)]

print('t сортировки list(100 el):   ', timeit.timeit("merge_sort(orig_list1)",
                                                     setup="from __main__ import merge_sort, orig_list1", number=1))
print('t сортировки list(1000 el):  ', timeit.timeit("merge_sort(orig_list2)",
                                                     setup="from __main__ import merge_sort, orig_list2", number=1))
print('t сортировки list(10000 el): ', timeit.timeit("merge_sort(orig_list3)",
                                                     setup="from __main__ import merge_sort, orig_list3", number=1))

orig_list1_sorted = merge_sort(orig_list1)
orig_list2_sorted = merge_sort(orig_list2)
orig_list3_sorted = merge_sort(orig_list3)

print('Исходный:         ', orig_list1)
print('Отсортированный:  ', orig_list1_sorted)

print('Исходный:         ', orig_list2)
print('Отсортированный:  ', orig_list2_sorted)

print('Исходный:         ', orig_list3)
print('Отсортированный:  ', orig_list3_sorted)
