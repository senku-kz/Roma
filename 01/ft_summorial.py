"""
python ft_summorial.py 5
python ft_summorial.py
python ft_summorial.py -2
"""

import sys

if len(sys.argv) < 2:
    print("Error! Usage: python3 ft_summorial.py <n>")
else:
    n = int(sys.argv[1])
    if n < 0:
        print("Error! n must be >=0")
    else:
        s = 0
        for i in range(n+1):
            s = s + i
        print("The sum is: " + str(s))
