# Задание 1
from itertools import islice


def gen(n):
    for num in range(1, n + 1, 2):
        yield num


num_gen = gen(15)
print(type(num_gen))
print(next(num_gen))
print(*islice(num_gen, 3))
print(next(num_gen))

# Задание 2

numbers_gen = (num for num in range(1, int(input('Введите n: ')) + 1, 2))

print(type(numbers_gen))
print(next(numbers_gen))
print(*islice(numbers_gen, 3))
print(next(numbers_gen))
