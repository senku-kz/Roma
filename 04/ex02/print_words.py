filename = input("Insert file name: ")

try:
    with open(filename) as f:
        n = int(input("Insert an integer: "))
        print("The words longer than {} are the following: ".format(n))
        for line in f:
            word = line.strip()
            if len(word) > n:
                print(word)
except FileNotFoundError:
    print("Error! The specified file does not exist!")
