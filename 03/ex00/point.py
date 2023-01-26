"""
python point.py
python -c 'from point import Point; print(Point(1,1).x)'
"""


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def get_distance(self):
        return ((self.x[0] - self.y[0]) ** 2 + (self.x[1] - self.y[1]) ** 2) ** 0.5


if __name__ == "__main__":
    x = [float(i) for i in input("Insert the coordinates of the first point: ").split(',')]
    y = [float(i) for i in input("Insert the coordinates of the second point: ").split(',')]
    point = Point(x, y)
    print("Their distance is: ", point.get_distance())
