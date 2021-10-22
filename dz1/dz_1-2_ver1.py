
cube7 = 0
for i in range(1, 1001, 2):
    i = i ** 3
    sum = 0
    tmp = i
    while tmp != 0:
        sum = sum + tmp % 10
        tmp = tmp // 10
    if sum % 7 == 0:
        cube7 = cube7 + i

print(cube7)

cube17_7 = 0
for i in range(1, 1001, 2):
    i = (i ** 3) + 17
    sum = 0
    tmp = i
    while tmp != 0:
        sum = sum + tmp % 10
        tmp = tmp // 10
    if sum % 7 == 0:
        cube17_7 = cube17_7 + i

print(cube17_7)