filename= "newfile.txt"
lines = 0
words = 0
chars = 0
with open(filename,"r") as file:
    for line in file:
        wordsList = line.split()
        lines += 1
        words += len(wordsList)
        chars += len(line)


print("Lines:" ,lines)
print("Words: ",words)
print("Characters:",chars)
