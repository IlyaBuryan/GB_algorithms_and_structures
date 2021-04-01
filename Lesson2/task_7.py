"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# Возможно переборщил с подробностью вывода. При необходимости
def check(n):
    def in_check(x):
        if x == 1:
            return 1
        else:
            return x + in_check(x - 1)

    if n == 0:
        return 'All statements are true!'
    else:
        rec = in_check(n)
        form = int(n * (n + 1) / 2)
        if rec == form:
            print(f'{" + ".join([str(i) for i in range(1, n + 1)])} = {rec}\n'
                  f'({n} * ({n} + 1) / 2) = {form}\n'
                  f'{form} = {rec} This is: {form == rec}\n')
            return check(n - 1)
        else:
            print(f'The statement is wrong {" + ".join([str(i) for i in range(1, n + 1)])} = {rec}')


print(check(int(input('Enter the number: '))))
