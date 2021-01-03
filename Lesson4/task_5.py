"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

"""
Долго просидел с этим заданием

При прямом применении решета столкнулся с проблемой, что не знаю заранее какой длинны массив сформировать.
Формулы не нашел как примерно вычислить :( тогда бы задача решалась элементарно через list comprehension
А дополнять список в процессе выполнения мешает то, что числа зануляем последовательно, да и не эффективно это.

Если даже формировать массив длинной n^2, все равно получается быстрее наивного алгоритма при больших n. 

Но дальше придумал другой вариант, который на очень маленьких n проигрывает наивному. Но с ростом n
победа нового алгоритма становится все сильнее и сильнее. В его основу так же положил идею Решета Эратосфена. 

Алгоритм быстрее за счет сокращения числа проверок делителей. А значит чем больше надо проверять, тем эффективнее.
"""

import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


i1 = 5
i2 = 50
i3 = 500
i4 = 600

print(simple(i1))
print(simple(i2))
print(simple(i3))
print(simple(i4))


def erat_fun(n):
    """С идеей «Решета Эратосфена»"""
    prime = [2, 3]
    i = 4
    while len(prime) < n:
        if all(map(lambda k: i % k != 0, prime)):
            prime.append(i)
        i += 1
    return prime[-1]


print(erat_fun(i1))
print(erat_fun(i2))
print(erat_fun(i3))
print(erat_fun(i4))

print('t первого / t второго', timeit.timeit('simple(i1)', setup='from __main__ import simple, i1', number=100) /
      timeit.timeit('erat_fun(i1)', setup='from __main__ import erat_fun, i1', number=100))
print('t первого / t второго', timeit.timeit('simple(i2)', setup='from __main__ import simple, i2', number=100) /
      timeit.timeit('erat_fun(i2)', setup='from __main__ import erat_fun, i2', number=100))
print('t первого / t второго', timeit.timeit('simple(i3)', setup='from __main__ import simple, i3', number=100) /
      timeit.timeit('erat_fun(i3)', setup='from __main__ import erat_fun, i3', number=100))
print('t первого / t второго', timeit.timeit('simple(i4)', setup='from __main__ import simple, i4', number=100) /
      timeit.timeit('erat_fun(i4)', setup='from __main__ import erat_fun, i4', number=100))
