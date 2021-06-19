class Matrix:
    def __init__(self, new_list):
        self.new_list = new_list

    def __str__(self):
        return "\n".join(map(str, self.new_list))

    def __add__(self, other):
        result = []
        for i in range(len(self.new_list)):
            result.append([])
            for tmp in range(len(self.new_list[0])):
                result[i].append(self.new_list[i][tmp] + other.new_list[i][tmp])
        return "\n".join(map(str, result))


x = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 3, 4, 1, 2]]
y = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [1, 3, 2, 5, 4]]

mtx_one = Matrix(x)
mtx_two = Matrix(y)
print(f'M1\n{mtx_one}\n{"*" * 20}')
print(f'M2\n{mtx_two}\n{"*" * 20}')
print(f'sum(M1 and M2)\n{mtx_one + mtx_two}')
