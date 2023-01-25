"""
python ft_ext_pos.py 2 3 1 5 -3 -1 4
python ft_ext_pos.py
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
    else:
        lst = sys.argv[1:]
        min_idx = 0
        max_idx = 0
        for i in range(1, len(lst)):
            if int(lst[min_idx]) > int(lst[i]):
                min_idx = i
            if int(lst[max_idx]) < int(lst[i]):
                max_idx = i
        print("The min is {1} and its position is {0}".format(min_idx, lst[min_idx]))
        print("The max is {1} and its position is {0}".format(max_idx, lst[max_idx]))
