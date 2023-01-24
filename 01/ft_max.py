import sys
if len(sys.argv) < 4:
    print("Error! Usage: python3 ft_max.py <x> <y> <z>")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    if a > b and a > c:
        print("The max is:", a)
    if b > a and b > c:
        print("The max is:", b)
    if c > a and c > b:
        print("The max is:", c)
