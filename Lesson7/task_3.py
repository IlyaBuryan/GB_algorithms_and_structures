"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

"""
Задачу решил 3 способами:
1. Как обсуждали на уроке через рекурсию 
2. Вариант через Гномью сотрировку, мы ее не учили, а название заинтересовало, решил посмотреть что это
3. Вариант скорее для просто интереса, так как мало кода:)

замеряв время совсем не удивился, что встроенная функция самая быстрая. 
Но точно удивился увидев, что через удаление min / max (вариант 3) оказалось самым быстрым

t Проверочная:-------------- 0.0009915439999996778
t Через рекурсию             0.9578555519999998
t Через гномью сортировку:   6.304070691
t Через удаление min / max:  0.6754566060000009
"""

import random
from statistics import median
import timeit
from sys import setrecursionlimit

setrecursionlimit(8002)

orig_list1 = [random.randint(0, 9999) for _ in range(8001)]


def median_search(list_in, n=0):
    left = []
    right = []
    median = list_in[n]
    for i in range(len(list_in)):
        current_el = list_in[i]
        if i != n:
            if current_el <= median:
                left.append(current_el)
            elif current_el >= median:
                right.append(current_el)

    if len(left) == len(right):
        return median
    else:
        return median_search(list_in, n + 1)


def gnome(list_in):
    i = 1
    size = len(list_in)
    while i < size:
        if list_in[i - 1] <= list_in[i]:
            i += 1
        else:
            list_in[i - 1], list_in[i] = list_in[i], list_in[i - 1]
            if i > 1:
                i -= 1
    return list_in[(len(list_in) - 1) // 2]


def median_search_del(list_in: list):
    for i in range(len(list_in) // 2):
        list_in.pop(list_in.index(max(list_in)))
        list_in.pop(list_in.index(min(list_in)))
    return list_in[0]


print('Масив: ', orig_list1)
print('Проверочная:--------------', median(orig_list1.copy()))
print('Через рекурсию:           ', median_search(orig_list1.copy()))
print('Через гномью сортировку:  ', gnome(orig_list1.copy()))
print('Через удаление min / max: ', median_search_del(orig_list1.copy()))

print('t Проверочная:--------------', timeit.timeit('median(orig_list1.copy())',
                                                    setup='from __main__ import median, orig_list1', number=1))
print('t Через рекурсию            ', timeit.timeit('median_search(orig_list1.copy())',
                                                    setup='from __main__ import median_search, orig_list1', number=1))
print('t Через гномью сортировку:  ', timeit.timeit('gnome(orig_list1.copy())',
                                                    setup='from __main__ import gnome, orig_list1', number=1))
print('t Через удаление min / max: ', timeit.timeit('median_search_del(orig_list1.copy())',
                                                    setup='from __main__ import median_search_del, orig_list1',
                                                    number=1))
