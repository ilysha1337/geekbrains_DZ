from requests import get, utils


# Урок 4 задание 2. Версия 2

def conv_val(valute):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")

    encode = utils.get_encoding_from_headers(response.headers)

    content = response.content.decode(encoding=encode).split("<Valute")
    for i in content:
        if valute in i:
            result = i.split('<Value>')
            result = result[1].split("</Value>")
            return result[0]


if __name__ == "__main__":

    get_float = (conv_val(valute=input("Введите код валюты: ").upper()))

    try:
        print(float(get_float.replace(',', '.')))
        print(type(float(get_float.replace(',', '.'))))

    except AttributeError:
        print(None)
