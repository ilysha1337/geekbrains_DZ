from abc import abstractmethod, ABC


class Clothes(ABC):
    tmp = 0

    def __init__(self, elm):
        self.elm = elm

    @property
    @abstractmethod
    def need(self):
        pass

    def __add__(self, itm):
        Clothes.tmp += self.need + itm.need
        return Costume(0)

    def __str__(self):
        result = Clothes.tmp
        Clothes.tmp = 0
        return "{}".format(result)


class Coat(Clothes):
    @property
    def need(self):
        return round(self.elm / 6.5) + 0.5


class Costume(Clothes):
    @property
    def need(self):
        return round((self.elm + 0.3) / 100)


coat = Coat(22)
costume = Costume(80)
print(coat + costume + coat)
