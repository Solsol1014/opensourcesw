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
    