"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

"""
Результат выполнения ниже. 
Первые 2 алгоритма достаточно времязатратные, сильный их недостаток в том, что они выполняют вычисления для каждого
элемента, в том числе и повторяющихся.

Ускорение в 3м алгоритме достигается благодаря отбору уникальных элементов в списке и расчета count только для них.
Так же сокращены затраты на операции записи и перезаписи переменных при использовании встроенных функций.


Чаще всего встречается число 4, оно появилось в массиве 400 раз(а)
Чаще всего встречается число 4, оно появилось в массиве 400 раз(а)
Чаще всего встречается число 4, оно появилось в массиве 400 раз(а)
11.515692379
11.59448266
0.06747451200000043
         3322 function calls in 0.023 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.023    0.023 <string>:1(<module>)
        1    0.000    0.000    0.011    0.011 task_4.py:56(func_1)
        1    0.000    0.000    0.012    0.012 task_4.py:68(func_2)
        1    0.000    0.000    0.000    0.000 task_4.py:80(func_3)
        1    0.000    0.000    0.000    0.000 task_4.py:81(<dictcomp>)
        5    0.000    0.000    0.000    0.000 task_4.py:83(<lambda>)
        1    0.000    0.000    0.023    0.023 task_4.py:96(main)
        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     1100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     2205    0.023    0.000    0.023    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}

"""

import timeit
import cProfile

array = [1, 3, 1, 3, 4, 5, 1, 4, 4, 4] * 100


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    """В одну строчку, как говорили на уроке"""
    cash = max({k: array.count(k) for k in set(array)}.items(), key=lambda i: i[1])
    return f'Чаще всего встречается число {cash[0]}, ' \
           f'оно появилось в массиве {cash[1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit.timeit('func_1()', setup='from __main__ import func_1', number=1000))
print(timeit.timeit('func_2()', setup='from __main__ import func_2', number=1000))
print(timeit.timeit('func_3()', setup='from __main__ import func_3', number=1000))


def main():
    func_1()
    func_2()
    func_3()


cProfile.run('main()')
