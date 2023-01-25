"""
python -c 'from ft_min import my_min; print(my_min())'
python ft_min.py 12 -35 8
python ft_min.py 12 -35
"""
import sys


def my_min(va=0, vb=0, vc=0):
    res = 0
    if va < vb and va < vc:
        res = va
    if vb < va and vb < vc:
        res = vb
    if vc < va and vc < vb:
        res = vc
    return res


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Error! Usage: python3 ft_min.py <x> <y> <z>")
    else:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        smallest = my_min(a, b, c)
        print("The min is: " + str(smallest))
