from requests import get, utils
import re

# Урок 4 задание 2. Версия 1

def conv_val(valute):
    for i in content:
        if valute in i:
            result = re.split(r"</Value>", re.split(r"<Value>", i).pop(1)).pop(0)
            return result


response = get("http://www.cbr.ru/scripts/XML_daily.asp")

encode = utils.get_encoding_from_headers(response.headers)

content = response.content.decode(encoding=encode).split("<Valute")

get_float = (conv_val(valute=input("Введите код валюты: ").upper()))

try:
    print(float(get_float.replace(',', '.')))
    print(type(float(get_float.replace(',', '.'))))

except AttributeError:
    print(None)
