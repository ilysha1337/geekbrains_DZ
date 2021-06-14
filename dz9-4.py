class Car:
    """Auto"""

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name}: Car go')

    def stop(self):
        print(f'{self.name}: Car stop')

    def turn(self, direction):
        print(f'{self.name}: Car turn {"left" if direction == 1 else "right"}')

    def show_speed(self):
        return f'{self.name}: Car speed :{self.speed}'


class TownCar(Car):
    """City auto"""

    def show_speed(self):
        return f'{self.name}: Car speed :{self.speed}. Exceeding the speed limit' \
            if self.speed > 60 else f"{self.name}: Car speed {self.speed}"


class WorkCar(Car):
    """Work Auto"""

    def show_speed(self):
        return f'{self.name}: Car speed :{self.speed}. Exceeding the speed limit' \
            if self.speed > 40 else f"{self.name}: Car speed {self.speed}"


class SportCar(Car):
    """Sport Auto"""
    pass


class PoliceCar(Car):
    """Police Auto"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_auto = PoliceCar("Police", "blue", 120)
police_auto.go()
print(police_auto.show_speed())
police_auto.turn(0)
police_auto.stop()
print("*" * 20)

Sport_auto = SportCar("F1", "red", 220)
Sport_auto.go()
print(Sport_auto.show_speed())
Sport_auto.turn(0)
Sport_auto.stop()
print("*" * 20)

Work_auto = WorkCar("Work", "black", 40)
Work_auto.go()
print(Work_auto.show_speed())
Work_auto.turn(1)
Work_auto.stop()
print("*" * 20)

Town_auto = TownCar("Town", "pink", 120)
Town_auto.go()
print(Town_auto.show_speed())
Town_auto.turn(1)
Town_auto.stop()
print("*" * 20)
