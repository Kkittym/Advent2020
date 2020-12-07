f = open("input.txt")

letterSet = set()
sum = 0
for line in f:
    line = line.strip()
    if line == '':
        sum = sum + len(letterSet)
        letterSet = set()
    else:
        letterSet.update(set(line))

f.close()

print(sum)