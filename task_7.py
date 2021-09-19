class DequeClass:
    def __init__(self):
        self.element = []

    def is_empty(self):
        return self.element == []

    def add_to_front(self, element):
        self.element.append(element)

    def add_to_rear(self, elem):
        self.element.insert(0, elem)

    def remove_from_front(self):
        return self.element.pop()

    def remove_from_rear(self):
        return self.element.pop(0)

    def size(self):
        return len(self.element)


def examination(string):
    objectStr = DequeClass()
    string = string.replace(' ', '').lower()
    # Убираем пробелы и приводим все к одному регистру,
    # чтобы слова начинающие с большой буквы тоже играли в нашу игру. Можно еще в функцию examination добавить флаг
    # чтобы настраивать значения с верхним и нижним регистром типо lower = True/False)

    for i in string:
        objectStr.add_to_rear(i)

    result = True

    while objectStr.size() > 1 and result:
        front = objectStr.remove_from_front()
        rear = objectStr.remove_from_rear()
        if front != rear:
            result = False

    return result


print(examination("молоко делили ледоколом"))
print(examination("молоё1ко делили лед6околом"))
print(examination("Два авд"))
print(examination("Два авД"))
print(examination("ТопоТ"))
print(examination("Топот"))
