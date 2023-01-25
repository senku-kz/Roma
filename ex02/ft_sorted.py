"""
python ft_sorted.py 5 4 2 1
python ft_sorted.py 5 2 4 0
python ft_sorted.py 5
"""
import sys


def is_equal(arr1, arr2):
    # Linearly compare elements
    for idx in range(len(arr1)):
        if arr1[idx] != arr2[idx]:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error! You must insert at least 2 numbers")
    else:
        arr = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
        arr_sorted = sorted(arr, reverse=True)
        if is_equal(arr, arr_sorted):
            print("The inserted sequence is sorted!")
        else:
            print("The inserted sequence is not sorted!")
            print("The correct order is", arr_sorted)
