class Point:
    coordx = 0
    coordy = 0

    def __init__(self, coordx=0, coordy=0):
        self.coordx = coordx
        self.coordy = coordy

    def move(self, dx, dy):
        self.coordx += dx
        self.coordy += dy

    def show(self):
        print("x: {}, y: {}".format(self.coordx, self.coordy))

class Box(Point):
    p1 = Point(0, 1)
    p2 = Point(1, 0)

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def show(self):
        self.p1.show()
        self.p2.show()

p1 = Point(1, 2)
p1.show()
p2 = Point(3, 4)
p2.show()

b = Box(p1, p2)
b.move(1, 1)
b.show()