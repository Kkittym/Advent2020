f = open("input.txt")

seatIDs = []
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
    seatIDs.append(seatID)

seatIDs.sort()
for i in range(0, len(seatIDs)-1):
    if (seatIDs[i]+1 != seatIDs[i+1]):
        print(seatIDs[i], seatIDs[i+1])


f.close()


