"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

"""
После попытки запуска профилировки на функциях с рекурсией: вычисления факториала 
и разворота числа столкнулся с проблемой многократного вывода профиля. 

Решить данную проблему удалось путем простого добавления необходимой для замера функции в функцию-обертку.

При этом удобно, что в колонке "Occurences" показывается число вызовов строк.


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    68     19.2 MiB     19.2 MiB           1   @profile
    69                                         def wrapper_fact(n):
    70     19.2 MiB      0.0 MiB          11       def factorial(n):
    71     19.2 MiB      0.0 MiB          10           if n == 1:
    72     19.2 MiB      0.0 MiB           1               return 1
    73                                                 else:
    74     19.2 MiB      0.0 MiB           9               return n * factorial(n - 1)
    75                                         
    76     19.2 MiB      0.0 MiB           1       return factorial(n)
3628800


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    82     19.2 MiB     19.2 MiB           1   @profile
    83                                         def wrapper_reverse(n):
    84     19.2 MiB      0.0 MiB           6       def recursive_reverse(number):
    85     19.2 MiB      0.0 MiB           5           if number == 0:
    86     19.2 MiB      0.0 MiB           1               return ''
    87     19.2 MiB      0.0 MiB           4           return f'{str(number % 10)}{recursive_reverse(number // 10)}'
    88                                         
    89     19.2 MiB      0.0 MiB           1       return recursive_reverse(n)
4321
"""

from memory_profiler import profile


@profile
def wrapper_fact(n):
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    return factorial(n)


print(wrapper_fact(10))


@profile
def wrapper_reverse(n):
    def recursive_reverse(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse(number // 10)}'

    return recursive_reverse(n)


print(wrapper_reverse(1234))
