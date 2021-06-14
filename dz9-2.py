class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, weigth=25, thickness=5):
        return f"{self._length} m * {self._width} m * {weigth} kg * {thickness} sm = {(self._length * self._width * weigth * thickness / 1000)} tn"


result_road = Road(5000, 20)
print(result_road.get_mass())
