src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Вариант 1

result_1 = [el for el in src if src.count(el) == 1]
print(result_1)

# Вариант 2 (оптимальный)

xmp = set()
tmp = set()
for el in src:
    if el not in tmp:
        xmp.add(el)
    else:
        xmp.discard(el)
    tmp.add(el)

result = [i for i in src if i in xmp]
print(result)
