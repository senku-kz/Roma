from point import Point


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        print("Circle of center ({}, {}) and radius {}".format(self.center.x, self.center.y, self.radius))


if __name__ == "__main__":
    point = Point(150, 100)
    rds = 75
    circle = Circle(point, rds)
    print(circle)
