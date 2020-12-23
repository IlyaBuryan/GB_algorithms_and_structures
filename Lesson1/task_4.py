"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

# Key - логин, values - простой словарь из пароля и статуса
gen_d = {'Marina': [96891, 0],
         'Olga': [18534, 0],
         'Denis': [96093, 0],
         'Alex': [67985, 0],
         'Andrey': [97792, 0],
         'Victoria': [58192, 0],
         'Semen': [25534, 0],
         'Amalia': [86573, 0],
         'Victor': [70386, 0]}


# Решение 1 - Сложность решения линейная O(N)
# Решение сложнее второго по причине инструкции "in list", которая линейная
def chech_entrance():
    print('Greetings!')  # O(1)
    try:
        user = input('Login: ')  # O(1) - предполагается ограничение на длину символов
        if user in list(gen_d.keys()):  # O(N)
            password = int(input('Password: '))  # O(1) - предполагается ограничение на длину символов
            if gen_d[user][0] == password:  # O(1)
                gen_d[user][1] = 1  # O(1)
                print('Successfully logged')  # O(1)
            else:
                print('The password is incorrect. Try again.')  # O(1)
        else:
            if input('There is no such user\n'
                     'If you want to register then type "yes": ') == 'yes':  # O(1)
                log = input('Login: ')  # O(1) - предполагается ограничение на длину символов
                try:
                    pas = int(input('Password: '))  # O(1) - предполагается ограничение на длину символов
                    if pas // 10000 < 1:  # O(1)
                        raise Exception  # O(1)
                    gen_d[log] = [pas, 1]  # O(1)
                except:
                    print('Try again and type minimum 5 numbers password')  # O(1)
            else:
                print('Goodluck!')  # O(1)
    except:
        print("Wrong input")  # O(1)


print('До запуска функции', gen_d)
chech_entrance()
print('После запуска функции', gen_d)


# Решение 2 - Сложность решения константная O(1)
# Алгоритм проще первого потому что используются операции только простой сложности
def chech_entrance_two():
    print('Greetings!')  # O(1)
    user = input('Login: ')  # O(1) - предполагается ограничение на длину символов
    try:
        if gen_d[user]:  # O(1) - проверка логина вместо перебора списка, как в первом случае
            try:
                password = int(input('Password: '))  # O(1) - предполагается ограничение на длину символов
                if gen_d[user][0] == password:  # O(1)
                    gen_d[user][1] = 1  # O(1)
                    print('Successfully logged')  # O(1)
                else:
                    print('The password is incorrect. Try again.')  # O(1)
            except:
                print("Wrong input")  # O(1)
    except:
        if input('There is no such user\n'
                 'If you want to register then type "yes": ') == 'yes':  # O(1)
            log = input('Login: ')  # O(1) - предполагается ограничение на длину символов
            try:
                pas = int(input('Password: '))  # O(1) - предполагается ограничение на длину символов
                if pas // 10000 < 1:  # O(1)
                    raise Exception  # O(1)
                gen_d[log] = [pas, 1]  # O(1)
            except:
                print('Try again and type minimum 5 numbers password')  # O(1)
        else:
            print('Goodluck!')  # O(1)


print('До запуска функции', gen_d)
chech_entrance_two()
print('После запуска функции', gen_d)
