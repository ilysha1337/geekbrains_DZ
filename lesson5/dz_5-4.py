# вариант 1
def super_function(new_list):
    for num in new_list:
        yield num


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
i = 1
numbers = super_function(src)
while i < len(src):
    tmp = next(numbers)
    if src[i] > tmp:
        result.append(src[i])
    i += 1
print(result)

# Вариант 2

new_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [new_list[i] for i in range(1, len(new_list)) if new_list[i - 1] < new_list[i]]
print(result)
