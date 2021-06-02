from sys import argv

with open("bakery.csv", 'a', encoding='utf-8') as f_add:
    with open("bakery.csv", 'r', encoding='utf-8') as f_read:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace('.', '').isdigit()]:
            if len(argv) == 3:
                first, lost = map(int, argv[1:])
                print(*(tmp for i, tmp in enumerate(f_read) if first - 1 <= lost), sep='')
            if ',' in argv[1] or '.' in argv[1]:
                if round(float(argv[1].replace(',', '.')), 3) <= 99999,99:
                    print(f"{round(float(argv[1].replace(',', '.')), 3):>010}", file=f_add)
                else:
                    print('Сумма должна быть меньше 99999,99!')
            else:
                print(*(tmp for i, tmp in enumerate(f_read) if i >= int(argv[1]) - 1))
        else:
            print(f_read.read())
