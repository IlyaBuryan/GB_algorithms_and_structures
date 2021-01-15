"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

"""
Для дека и листа реализовал функции. Результат по времени их выполнения ниже:
1. Добавление элемента в конец. 100 элементов, 100000 запусков
Длинна объектов Лист / Дека - ДО:  999 999
0.744218943
0.45936403400000003
Длинна объектов Лист / Дека - ПОСЛЕ:  10000999 10000999  

2. Удаление элемента в начале. 100 элементов, 10 запусков
Длинна объектов Лист / Дека - ДО:  10000999 10000999
10.058215534999999
4.8137000000281205e-05
Длинна объектов Лист / Дека - ПОСЛЕ:  9999999 9999999 

3. Добавление элемента в начало. 100 элементов, 10 запусков
Длинна объектов Лист / Дека - ДО:  9999999 9999999
10.546592886999997
4.412599999881195e-05
Длинна объектов Лист / Дека - ПОСЛЕ:  10000999 10000999 

Исходя из результатов видно, что выполнение стандартной операции 1. Добавление элемента в конец
практически не различается (дек получился даже немного быстрее)

НО вставка или удаление первых элементов по времени отличаются просто катастрофически. Лист работает намного 
медленнее, чем дэк.

Это показывает, что при необходимости организации дека необходимо использовать встроенный компонент deque, а не list
"""

from collections import deque
import timeit

list_test = [i for i in range(999)]
deque_test = deque([i for i in range(999)])

list_append_code = """
for i in range(100):
    list_test.append(i)
"""

deque_append_code = """
for i in range(100):
    deque_test.append(i)
"""

list_popfirst_code = """
for i in range(100):
    list_test.pop(0)
"""

deque_popleft_code = """
for i in range(100):
    deque_test.popleft()
"""

list_insertfirst_code = """
for i in range(100):
    list_test.insert(i, 0)
"""

deque_insertleft_code = """
for i in range(100):
    deque_test.appendleft(i)
"""

print("Длинна объектов Лист / Дека - ДО: ", len(list_test), len(deque_test))
print(timeit.timeit(list_append_code, setup='from __main__ import list_test', number=100000))
print(timeit.timeit(deque_append_code, setup='from __main__ import deque_test', number=100000))
print("Длинна объектов Лист / Дека - ПОСЛЕ: ", len(list_test), len(deque_test), '\n')

print("Длинна объектов Лист / Дека - ДО: ", len(list_test), len(deque_test))
print(timeit.timeit(list_popfirst_code, setup='from __main__ import list_test', number=10))
print(timeit.timeit(deque_popleft_code, setup='from __main__ import deque_test', number=10))
print("Длинна объектов Лист / Дека - ПОСЛЕ: ", len(list_test), len(deque_test), '\n')

print("Длинна объектов Лист / Дека - ДО: ", len(list_test), len(deque_test))
print(timeit.timeit(list_insertfirst_code, setup='from __main__ import list_test', number=10))
print(timeit.timeit(deque_insertleft_code, setup='from __main__ import deque_test', number=10))
print("Длинна объектов Лист / Дека - ПОСЛЕ: ", len(list_test), len(deque_test), '\n')
