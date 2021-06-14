class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._ZP = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f'{sum(self._ZP.values())}'


worker = Position('Oleg', 'Milorodov', 'cliner', 15000, 5000)
print(worker.get_full_name())
print(worker.position)
print(worker.get_full_profit())
