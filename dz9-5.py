class Stationery:
    def __init__(self, title="paint"):
        self.title = title

    def draw(self):
        print(f"now drawing with {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"now drawing with {self.title} pen")


class Pencil(Stationery):
    def draw(self):
        print(f"now drawing with {self.title} pencil")


class Handle(Stationery):
    def draw(self):
        print(f"now drawing with {self.title} handle")


stationery = Stationery("any color")
stationery.draw()
handle = Handle("yellow")
handle.draw()
pencil = Pencil("blue")
pencil.draw()
pen = Pen("rainbow")
pen.draw()
