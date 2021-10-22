# Вариант 1
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    content = f.read().replace('"', "").split("\n")
    new_list = []
    for i in content:
        tmp = i.split(" ")
        result = (tmp[0], tmp[5], tmp[6])
        new_list.append(result)
print(new_list)

# Вариант 2

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    result = ((i.split()[0], i.split()[5], i.split()[6]) for i in f)
    for i in result:
        print(i)
