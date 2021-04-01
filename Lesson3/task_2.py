"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

# Сделал через класс, чтобы просто потренироваться в работе с ооп
import hashlib


class Check:

    def __init__(self):
        self.password = hashlib.pbkdf2_hmac(hash_name='sha256',
                                            password=input('Input the password: ').encode(),
                                            salt=b'The best salt ever',
                                            iterations=99999)
        print('Saved string: ', self.password.hex())

    def check_pass(self):
        self.new_pass = hashlib.pbkdf2_hmac(hash_name='sha256',
                                            password=input('Input NEW password: ').encode(),
                                            salt=b'The best salt ever',
                                            iterations=99999)
        if self.password == self.new_pass:
            print('Correct password!')
        else:
            print('You will not pass!')


if __name__ == '__main__':
    ex = Check()
    ex.check_pass()
