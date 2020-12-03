treeMap = []
with open("input.txt") as f:
    treeMap = f.readlines()

treeMap = [x.strip() for x in treeMap]
print(len(treeMap), len(treeMap[0]))

x = 0
y = 0
treeCounter = 0
while(y < len(treeMap)-1):
    x = (x+3) % len(treeMap[0])
    y = y+1
    if (treeMap[y][x] == '#'):
        treeCounter = treeCounter + 1

print(treeCounter)