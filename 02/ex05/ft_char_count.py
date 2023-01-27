"""
python ft_char_count.py programming
python ft_char_count.py "this is a test"
python ft_char_count.py
"""

import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error! No string given")
    else:
        s = sys.argv[1]
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        t = dict(sorted(d.items()))
        print("Char count:")
        for k, v in t.items():
            print("{} = {}".format(k, v))
