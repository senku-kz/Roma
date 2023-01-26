"""
python point.py
python -c 'from point import Point; print(Point(1,1).x)'
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    a = [float(i) for i in input("Insert the coordinates of the first point: ").split(',')]
    b = [float(i) for i in input("Insert the coordinates of the second point: ").split(',')]
    point_a = Point(a[0], a[1])
    point_b = Point(b[0], b[1])

    d = ((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2) ** 0.5
    print("Their distance is: ", d)
