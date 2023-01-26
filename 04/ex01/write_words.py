n = int(input("Insert an integer: "))
print("The words longer than {} have been written on \"long_words.txt\"".format(n))

fw = open("long_words.txt", "w")
with open('words.txt') as f:
    for line in f:
        word = line.strip()
        if len(word) > n:
            fw.write(word)
            fw.write("\n")
fw.close()
