"""
python -c 'from ft_sum_list import sum_list; print(sum_list([-1,2,5]))'
"""


def sum_list(v_lst):
    s = 0
    for v in v_lst:
        s = s + v
    return s


if __name__ == "__main__":
    lst = []
    while True:
        n = int(input("Insert integer: "))
        if n == 0:
            break
        lst.append(n)
    print("The sum is: " + str(sum_list(lst)))
