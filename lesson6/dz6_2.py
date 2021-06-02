from collections import Counter
from time import perf_counter
start = perf_counter()
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    result = ((i.split()[0], i.split()[5], i.split()[6]) for i in f)
    my_list = []
    for i in result:
        my_list.append(i[0])
    spam = Counter(my_list)
    print("spam IP: {}".format(spam))
print(perf_counter() - start)