f = open("input.txt")

highest = 0
for line in f:
    line = line.strip()
    minRow = 0
    maxRow = 127
    minCol = 0
    maxCol = 7
    rowlist = line[:7]
    columnlist = line[-3:]
    for l in rowlist:
        if (l == "F"):
            maxRow = int((maxRow+minRow)/2)
        else:
            minRow = int((maxRow+minRow)/2)+1
    for c in columnlist:
        if (c == "L"):
            maxCol = int((maxCol+minCol)/2)
        else:
            minCol = int((maxCol+minCol)/2)+1
    seatID = minRow*8+minCol
    if (seatID > highest):
        highest = seatID

print(highest)

f.close()


