f = open("input.txt")


firstLine = f.readline().strip()
letterSet = set(firstLine)
sum = 0
for line in f:
    line = line.strip()
    if line == '':
        sum = sum + len(letterSet)
        nextline = f.readline().strip()
        letterSet = set(nextline)
    else:
        letterSet.intersection_update(set(line))

f.close()

print(sum)