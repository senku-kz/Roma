"""
python ft_palindrome.py kayak
python ft_palindrome.py exam
python ft_palindrome.py are we not drawn onward to new era
python ft_palindrome.py "are we not drawn onward to new era"
python -c 'from ft_palindrome import is_palindrome; print(is_palindrome("kayak"))'
"""

import sys


def is_palindrome(v):
    return v == v[::-1]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
    elif len(sys.argv) > 2:
        print("Error! Insert just 1 string!")
    else:
        s = sys.argv[1]
        if is_palindrome(s):
            print("The string {} is palindrome".format(s))
        else:
            print("The string {} is not palindrome".format(s))
