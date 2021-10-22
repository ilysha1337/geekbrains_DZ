def getDigitSum(num):
    sum = 0
    for i in str(num):
        sum = sum + int(i)
    return sum

cube7 = 0
cube17_7 = 0
for i in range(1, 1001, 2):
    i = i ** 3
    if getDigitSum(i) % 7 == 0:
        cube7 = cube7 + i
    i = i + 17
    if getDigitSum(i) % 7 == 0:
        cube17_7 = cube17_7 + i

print("Cubes devided by 7 sum: {}".format(cube7))
print("Cubes plus 17 devided by 7 sum: {}".format(cube17_7))