n = int(input("Insert an integer: "))
print("The words longer than 19 are the following:")
with open('words.txt') as f:
    for line in f:
        word = line.strip()
        if len(word) > n:
            print(word)
