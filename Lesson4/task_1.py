"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit

num = [i for i in range(999)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Замер выполнен и дает результат 0.812267635
print(timeit.timeit('func_1(num)', setup='from __main__ import func_1, num', number=10000))


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# Замер новой функции дает более быстрый результат 0.662561069. В среднем быстрее.
# Оптимизация достигнута благодаря list comprehension с фильтрацией через if
# Сделал так, чтобы избежать отдельной операции записи в созданный список
print(timeit.timeit('func_2(num)', setup='from __main__ import func_2, num', number=10000))

# Пробовал и другие способы, но они не оказались быстрее...
