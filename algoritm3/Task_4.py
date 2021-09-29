"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
url : хеш-url
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib
from uuid import uuid4

url_storage = {}


def url_cash():
    url = input('Введите url-адрес: ')
    salt = uuid4().hex
    url_hash = hashlib.sha256(salt.encode() + url.encode('utf-8')).hexdigest()
    if url_storage.get(url_hash):
        print(url_storage[url_hash])
    else:
        url_storage.setdefault(url_hash, url)


url_cash()
print(url_storage)