"""
python circle.py
python -c 'from circle import Circle; print(Circle((1,1),4))'
"""
from point import Point


class Circle:
    def __init__(self, center, radius):
        self.center = Point(center[0], center[1])
        self.radius = radius

    def __str__(self):
        return "Circle of center ({}, {}) and radius {}".format(self.center.x, self.center.y, self.radius)


if __name__ == "__main__":
    point = (150, 100)
    rds = 75
    circle = Circle(point, rds)
    print(circle)
