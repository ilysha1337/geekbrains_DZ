class Cell:
    def __init__(self, num):
        self.num = num

    def new_func(self, elm):
        return '\n'.join(["+" * elm for i in range(self.num // elm)]) + "\n" + "+" * (self.num % elm)

    def __str__(self):
        return "{}".format(self.num)

    def __add__(self, itm):
        return Cell(self.num + itm.num)

    def __sub__(self, itm):
        return Cell(self.num - itm.num) if self.num - itm.num > 0 else 'Err'

    def __mul__(self, itm):
        return Cell(self.num * itm.num)

    def __floordiv__(self, itm):
        return Cell(self.num // itm.num)


one_cell = Cell(23)
two_cell = Cell(22)

print(one_cell.new_func(10))
print(one_cell * two_cell)
print(one_cell - two_cell)
print(one_cell + two_cell)
print(one_cell // two_cell)
