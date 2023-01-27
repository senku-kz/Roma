"""
python ft_matrix.py 2 3
python ft_matrix.py 2
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error! Usage: python3 ft_matrix.py <n> <m>")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        arr = [[0 for i in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = float(input("Insert the element in position ({}, {}): ".format(i, j)))

        for i in range(n):
            print("[", end="")
            for j in range(m):
                if j != 0:
                    print(", ", end="")
                print(arr[i][j], end="")

            print("]")

        # The sum over rows
        rows_sum = [0 for i in range(n)]
        for i in range(n):
            s = 0
            for j in range(m):
                s = s + arr[i][j]
            rows_sum[i] = s

        print("The sum over rows is:")
        print("[", end="")
        for i in range(n):
            if i != 0:
                print(", ", end="")
            print(rows_sum[i], end="")
        print("]")

        # The sum over columns
        column_sum = [0 for i in range(m)]
        for j in range(m):
            s = 0
            for i in range(n):
                s = s + arr[i][j]
            column_sum[j] = s

        print("The sum over columns is:")
        print("[", end="")
        for j in range(m):
            if j != 0:
                print(", ", end="")
            print(column_sum[j], end="")
        print("]")
