import re


def parse(email):
    p_mail = re.compile(r"(?P<login>([\w]+))@(?P<domen>[^&]+\.\w+)", re.IGNORECASE)
    if not p_mail.match(email):
        reise
        ValueError("Неверный имеил: {}".format(email))
    print(p_mail.match(email).groupdict())


for i in ['someone@geekbrains.ru', 'dosasosa@geekbrains.ru', 'sometime@gmail.com']:
    try:
        parse(i)
    except ValueError:
        print('Error')
