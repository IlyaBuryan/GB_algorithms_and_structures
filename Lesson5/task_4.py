"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

"""
Исходя из результатов, которые показывают, что большой разницы между Dict / OrderedDict нет. Более того
по моим замерам OrderedDict даже получился чуть медленнее. А так же того факта, что текущий Dict запоминает порядок. 

Можно сделать вывод, что применять OrderedDict смысла сейчас уже особого не имеет,  
так как все уже решено в новых версиях Python.

Реализовал 3 метода со следующими результатами по времени:

1. Вставка пар ключ - значение
Длинна объектов Dict / OrderedDict - ДО:  999 999
0.095246899 Dict
0.13756017499999998 OrderedDict
Длинна объектов Dict / OrderedDict - ПОСЛЕ:  999997 999997 

2. Удаление пар ключ - значение
Длинна объектов Dict / OrderedDict - ДО:  999997 999997
0.007513705000000037 Dict
0.015373120000000018 OrderedDict
Длинна объектов Dict / OrderedDict - ПОСЛЕ:  900097 900097 

2. Поиск максимума среди ключей
Длинна объектов Dict / OrderedDict - ДО:  900097 900097
1.557262464 Dict
2.1907983 OrderedDict
Длинна объектов Dict / OrderedDict - ПОСЛЕ:  900097 900097 
"""

from collections import OrderedDict
import timeit

common_dict = {i: i * i for i in range(999)}
ordered_dict = OrderedDict({i: i * i for i in range(999)})

common_dict_insert = """
for i in range(1001, 999999):
    common_dict[i] = i
"""

ordered_dict_insert = """
for i in range(1001, 999999):
    ordered_dict[i] = i
"""

common_dict_pop = """
for i in range(999):
    common_dict.popitem()
"""

ordered_dict_pop = """
for i in range(999):
    ordered_dict.popitem()
"""

common_dict_max = """
max(common_dict)
"""

ordered_dict_max = """
max(ordered_dict)
"""

print("Длинна объектов Dict / OrderedDict - ДО: ", len(common_dict), len(ordered_dict))
print(timeit.timeit(common_dict_insert, setup='from __main__ import common_dict', number=1), 'Dict')
print(timeit.timeit(ordered_dict_insert, setup='from __main__ import ordered_dict', number=1), 'OrderedDict')
print("Длинна объектов Dict / OrderedDict - ПОСЛЕ: ", len(common_dict), len(ordered_dict), '\n')

print("Длинна объектов Dict / OrderedDict - ДО: ", len(common_dict), len(ordered_dict))
print(timeit.timeit(common_dict_pop, setup='from __main__ import common_dict', number=100), 'Dict')
print(timeit.timeit(ordered_dict_pop, setup='from __main__ import ordered_dict', number=100), 'OrderedDict')
print("Длинна объектов Dict / OrderedDict - ПОСЛЕ: ", len(common_dict), len(ordered_dict), '\n')

print("Длинна объектов Dict / OrderedDict - ДО: ", len(common_dict), len(ordered_dict))
print(timeit.timeit(common_dict_max, setup='from __main__ import common_dict', number=100), 'Dict')
print(timeit.timeit(ordered_dict_max, setup='from __main__ import ordered_dict', number=100), 'OrderedDict')
print("Длинна объектов Dict / OrderedDict - ПОСЛЕ: ", len(common_dict), len(ordered_dict), '\n')
