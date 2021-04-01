"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import timeit
from memory_profiler import memory_usage, profile
from random import choice
from string import ascii_lowercase
from pympler import asizeof


# Создан декоратор для замера времени и памяти выполнения входящей функции
def time_execution(fun):
    def inside_fun():
        start_time = timeit.default_timer()
        start_memory = memory_usage()
        fun()
        end_time = timeit.default_timer()
        end_memory = memory_usage()
        return f'Время: {end_time - start_time} сек. || Память: {end_memory[0] - start_memory[0]} Мб.'

    return inside_fun


"""
Версия Python - 3.7 
Разрядность системы - 64

1. Выполнен анализ двух функций, разворачивающих число (результаты ниже).

Вторая функция не только быстрее по времени, но и эффективнее по памяти. 
Неэффективность первого решения заключается в созданиях переменных на каждом шаге цикла.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    96     19.2 MiB     19.2 MiB           1   @time_execution
    97                                         @profile
    98                                         def revers_1(enter_num, revers_num=0):
    99     20.2 MiB      0.0 MiB       32359       while enter_num != 0:
   100     20.2 MiB      0.7 MiB       32358           num = enter_num % 10
   101     20.2 MiB      0.0 MiB       32358           revers_num = (revers_num + num / 10) * 10
   102     20.2 MiB      0.3 MiB       32358           enter_num //= 10
   103     20.2 MiB      0.0 MiB           1       return revers_num
Время: 4.0287409389999995 сек. || Память: 1.234375 Мб.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   105     20.2 MiB     20.2 MiB           1   @time_execution
   106                                         @profile
   107                                         def revers_2(enter_num):
   108     20.2 MiB      0.0 MiB           1       enter_num = str(enter_num)
   109     20.3 MiB      0.0 MiB           1       revers_num = enter_num[::-1]
   110     20.3 MiB      0.0 MiB           1       return int(revers_num)
Время: 0.1255177439999997 сек. || Память: 0.0625 Мб.
"""
enter_num = 123456789 ** 3999


@time_execution
@profile
def revers_1(enter_num=123456789 ** 3999, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@time_execution
@profile
def revers_2(enter_num=123456789 ** 3999):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return int(revers_num)


print(revers_1())
print(revers_2())
"""
Версия Python - 3.7 
Разрядность системы - 64

Во рассмотрел имитацию фильтрации списка + важность зачистки параметра, если он более не требуется.

В первом алгоритме помимо большой нагрузке на память для создания списка, память еще и нагружена операцией .append
Во втором же алгоритме удалось снизить затраты памяти за счет применения фильтра с лямбда функцией + после
удален ненужный элемент, так что это облегчает дальнейшее выполнение кода.


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   106     19.3 MiB     19.3 MiB           1   @time_execution
   107                                         @profile
   108                                         def filter_1():
   109     27.1 MiB      7.7 MiB           1       n1 = list(range(200000))
   110     27.1 MiB      0.0 MiB           1       b1 = []
   111     28.1 MiB      0.0 MiB      200001       for i in n1:
   112     28.1 MiB      0.0 MiB      200000           if i % 2 == 0:
   113     28.1 MiB      1.0 MiB      100000               b1.append(i)
   114     28.1 MiB      0.0 MiB           1       return b1
Время: 10.472295461 сек. || Память: 0.44921875 Мб.


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   117     19.5 MiB     19.5 MiB           1   @time_execution
   118                                         @profile
   119                                         def filter_2():
   120     27.1 MiB      7.5 MiB           1       n2 = list(range(200000))
   121     27.1 MiB      0.0 MiB      400001       b2 = list(filter(lambda x: x % 2 == 2, n2))
   122     19.6 MiB     -7.5 MiB           1       del n2
   123     19.6 MiB      0.0 MiB           1       return b2
Время: 8.443688721000001 сек. || Память: 0.06640625 Мб.
"""


@time_execution
@profile
def filter_1():
    n1 = list(range(200000))
    b1 = []
    for i in n1:
        if i % 2 == 0:
            b1.append(i)
    # какой-то код


@time_execution
@profile
def filter_2():
    n2 = list(range(200000))
    b2 = list(filter(lambda x: x % 2 == 2, n2))
    del n2
    # какой-то код


print(filter_1())
print(filter_2())

"""
В последнем примере мне подробнее захотелось посмотреть на разницу в использовании памяти: list - string. 
Потому что еще с основ помню, как говорилось, что string легче list.

Для этого в первой функции сделал подсчет количества букв "а" в списке, а во второй функции перевел list в string
с последующим удалением list.

В результате удалось выполнить такой же подсчет, только задействовав меньше памяти. Дополнительно разницу в раммере
можно заметить воспользовавшись asizeof библиотеки pympler.
Знаит string легче, и этот тип даннх можно эффективно использовать в некоторых ситуациях.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   174     54.1 MiB     54.1 MiB           1   @time_execution
   175                                         @profile
   176                                         def list_w():
   177     55.6 MiB      1.5 MiB      100003       gen_list = [choice(ascii_lowercase) for i in range(100000)]
   178     55.6 MiB      0.0 MiB           1       count_num = 0
   179     55.6 MiB      0.0 MiB      100001       for i in gen_list:
   180     55.6 MiB      0.0 MiB      100000           if i == 'a':
   181     55.6 MiB      0.0 MiB        3871               count_num += 1
   182     55.6 MiB      0.0 MiB           1       print(count_num)
Время: 7.8314694959999995 сек. || Память: 0.42578125 Мб.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   184     54.1 MiB     54.1 MiB           1   @time_execution
   185                                         @profile
   186                                         def string_w():
   187     55.6 MiB      1.5 MiB      100003       gen = [choice(ascii_lowercase) for i in range(100000)]
   188     55.6 MiB      0.0 MiB           1       gen_string = ''.join(gen)
   189     54.2 MiB     -1.4 MiB           1       del gen
   190     54.2 MiB      0.0 MiB           1       count_num = 0
   191     54.2 MiB      0.0 MiB      100001       for i in gen_string:
   192     54.2 MiB      0.0 MiB      100000           if i == 'a':
   193     54.2 MiB      0.0 MiB        3853               count_num += 1
   194     54.2 MiB      0.0 MiB           1       print(count_num)
Время: 7.820635463 сек. || Память: 0.09375 Мб.
"""


@time_execution
@profile
def list_w():
    gen_list = [choice(ascii_lowercase) for i in range(100000)]
    count_num = 0
    for i in gen_list:
        if i == 'a':
            count_num += 1
    print(count_num)


@time_execution
@profile
def string_w():
    gen = [choice(ascii_lowercase) for i in range(100000)]
    gen_string = ''.join(gen)
    print(asizeof.asizeof(gen))
    print(asizeof.asizeof(gen_string))
    del gen
    count_num = 0
    for i in gen_string:
        if i == 'a':
            count_num += 1


print(list_w())
print(string_w())
