#завернул все в бесконеный цикл для удобства проверки программы
while True:
    try:
        percents = int(input("Введите процент от 1 до 20: "))
    except ValueError:
        print("Нужно было ввести число!")

    if percents == 1:
        result = 'т'
    elif percents == 2 or percents == 3 or percents == 4:
        result = 'та'
    else:
        result = 'тов'

    print('{} процен'.format(percents) + result)
