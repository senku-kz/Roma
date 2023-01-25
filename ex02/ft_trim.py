"""
python ft_trim.py a b c d
python ft_trim.py a b
python ft_trim.py a
python -c 'from ft_trim import trim; print(trim([1,2,3,4]))'
"""
import sys


def trim(lst):
    print("The new list is:", lst[1:len(lst)-1])
    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error! You must insert at least 2 values")
    else:
        arr = sys.argv[1:]
        trim(arr)
