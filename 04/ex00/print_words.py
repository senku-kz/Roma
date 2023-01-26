n = int(input("Insert an integer: "))
print("The words longer than {} are the following: ".format(n))
with open('words.txt') as f:
    for line in f:
        word = line.strip()
        if len(word) > n:
            print(word)
