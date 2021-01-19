"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

from random import choice
from string import ascii_lowercase
from pympler import asizeof
import json
from objgraph import *

"""
1 - Первый механизм, который наглядно видеть - это грамотное использование типов данных, соответствющих решаемым
задачам. Если можно решить задачу более легким типом данных, например, строкой, а не листом или тем более словарем
то нужно это делать.

В примере ниже видно, что string с теми же самыми данными в 8 раз легче, чем list.
"""

gen = [choice(ascii_lowercase) for i in range(100000)]
gen_string = ''.join(gen)
print('Размер list: ', asizeof.asizeof(gen))
print('Размер string: ', asizeof.asizeof(gen_string))

"""
2 - Из первого механизма следует второй, что для долгосрочного хранения редкоиспользуемых объектов можно 
серилизовать их в json, так тот же dict будет занимать в несколько раз меньшее место.
"""

gen_dict = {i: i * 2 for i in range(100000)}
dumped_dict = json.dumps(gen_dict)

print(type(gen_dict))
print(type(dumped_dict))

print('Размер list: ', asizeof.asizeof(gen_dict))
print('Размер json: ', asizeof.asizeof(dumped_dict))

"""
3 - В сложных проектах или при использовании ООП, может быть достаточно полезен модуль objgraph.

При знакомстве с ним нашел несколько потенциально очень полезных возможностей.
Так же имеются и некоторые другие функции.
"""


class Createlists:
    def __init__(self):
        list_1 = []
        list_2 = [2, 'fdf']


if __name__ == "__main__":
    a = Createlists()
    b = Createlists()

# Можно узнать сколько экземпляров класса было создано
print(count('Createlists'))

# Можно посмотреть какие типы и сколько отслеживает GB
print(typestats())

"""
# Можно в режиме реального времени смотреть сколько и каких объектов было создано
===============================================================
Type             Old_ids  Current_ids      New_ids Count_Deltas
===============================================================
list                 318          320           +2           +2
Createlists            2            3           +1           +1
===============================================================
"""
get_new_ids(limit=0)
get_new_ids(limit=0)
a1 = [0, 1, 2]
b1 = [3, 4, 5]
c = Createlists()
get_new_ids(limit=2)
