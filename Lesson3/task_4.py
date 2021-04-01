"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


class Web:
    def __init__(self):
        self.cash = {}

    def get_url(self, url_var):
        self.url_var = url_var
        hash_obj = hashlib.sha256(self.url_var.encode() + 'Some salt'.encode()).hexdigest()
        if hash_obj not in self.cash:
            self.cash[hash_obj] = 'Some data'
            print(f'{self.url_var} added to cash')
        else:
            print(f'URL {self.url_var} is already in cash')

    def print_cash(self):
        for k, v in self.cash.items():
            print(f'{k} {v}')


if __name__ == '__main__':
    a = Web()
    a.get_url('https://yandex.ru/')
    a.get_url('https://yandex.ru/')
    a.get_url('https://mail.ru/')
    a.get_url('https://mail.ru/')
    a.get_url('https://geekbrains.ru/')

    a.print_cash()
