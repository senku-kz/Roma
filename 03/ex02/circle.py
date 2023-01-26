"""
python circle.py
python -c 'from circle import Circle; print(Circle((1,1),4))'

python circle.py 1.5 1.5
python circle.py 0.5 0.4
python -c 'from circle import Circle,Point; print(Circle((0,0),2).contains(Point(1,1)))'
"""
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = Point(center[0], center[1])
        self.radius = radius

    def __str__(self):
        return "Circle of center ({}, {}) and radius {}".format(self.center.x, self.center.y, self.radius)

    def contains(self, point: Point):
        length = (point.x ** 2 + point.y ** 2) ** 0.5
        if length > abs(self.radius):
            return False
        return True


if __name__ == "__main__":
    point_obj = Point(float(sys.argv[1]), float(sys.argv[2]))
    circle_center = (0, 0)
    circle_radius = 1
    circle = Circle(circle_center, circle_radius)
    print("The Point ({}, {}) lies in the Circle of center ({}, {}) and radius {}".format(point_obj.x,
                                                                                         point_obj.y,
                                                                                         circle.center.x,
                                                                                         circle.center.y,
                                                                                         circle.radius))
