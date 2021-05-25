from requests import get, utils
import datetime


# Урок 4 задание 3
def conv_val(valute):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")

    encode = utils.get_encoding_from_headers(response.headers)

    content = response.content.decode(encoding=encode).split("<Valute")
    data_result = []
    data = content[0].split('"')
    data_result.append(data[5])
    for i in content:
        if valute in i:
            result = i.split('<Value>')
            result = result[1].split("</Value>")
            data_result.append(result[0])
            return data_result


if __name__ == "__main__":
    get_float = (conv_val(valute=input("Введите код валюты: ").upper()))
    print(float(get_float[1].replace(',', '.')))
    date = get_float[0].split(".")
    print(datetime.date(int(date[2]), int(date[1]), int(date[0])))
