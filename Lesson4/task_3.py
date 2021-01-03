"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

"""
Результаты ниже:
1. Первая рекурсивная функция самая неэффективная по времени. Хоть каждый отдельный вызов и занимает немного времени,
но этих вызовов происходит по числу длинны самого числа. Глубина рекурсии становится очень большой. Из-за этого
очень высокие затраты по времени: рекурсивная сложность.
2. Второе решение хоть и быстрее но не на много. Оно сильно нагружено математическими операциями + постоянно
происходит перезапись неизменяемого объекта revers_num , что нагружает использование памяти.
3. Третье решение в линейной сложности очень быстрое по сравнению с предыдущими, потому что лишено их недостатков. 
Более того использует уже встроенные функции и операции str и [::-1], что как мы учили всегда эффективнее.

6.08257047
5.280786056999999
0.06824615799999911
         2030 function calls (7 primitive calls) in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
   2024/1    0.007    0.000    0.007    0.007 task_3.py:20(revers)
        1    0.005    0.005    0.005    0.005 task_3.py:30(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
        1    0.000    0.000    0.012    0.012 task_3.py:51(main)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

import timeit
import cProfile
from sys import setrecursionlimit

setrecursionlimit(10000)


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return int(revers_num)


enter_num = 123456789 ** 250

print(timeit.timeit('revers(enter_num)', setup='from __main__ import revers, enter_num', number=1000))
print(timeit.timeit('revers_2(enter_num)', setup='from __main__ import revers_2, enter_num', number=1000))
print(timeit.timeit('revers_3(enter_num)', setup='from __main__ import revers_3, enter_num', number=1000))


def main():
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)


cProfile.run('main()')
