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

#Right 1 Down 1
x = 0
y = 0
treeCounter11 = 0
while(y < len(treeMap)-1):
    x = (x+1) % len(treeMap[0])
    y = y+1
    if (treeMap[y][x] == '#'):
        treeCounter11 = treeCounter11 + 1

#Right 3 Down 1
x = 0
y = 0
treeCounter31 = 0
while(y < len(treeMap)-1):
    x = (x+3) % len(treeMap[0])
    y = y+1
    if (treeMap[y][x] == '#'):
        treeCounter31 = treeCounter31 + 1

#Right 5 Down 1
x = 0
y = 0
treeCounter51 = 0
while(y < len(treeMap)-1):
    x = (x+5) % len(treeMap[0])
    y = y+1
    if (treeMap[y][x] == '#'):
        treeCounter51 = treeCounter51 + 1

#Right 7 Down 1
x = 0
y = 0
treeCounter71 = 0
while(y < len(treeMap)-1):
    x = (x+7) % len(treeMap[0])
    y = y+1
    if (treeMap[y][x] == '#'):
        treeCounter71 = treeCounter71 + 1

#Right 1 Down 2
x = 0
y = 0
treeCounter12 = 0
while(y < len(treeMap)-2):
    x = (x+1) % len(treeMap[0])
    y = y+2
    print(y)
    if (treeMap[y][x] == '#'):
        treeCounter12 = treeCounter12 + 1

print(treeCounter11, treeCounter31, treeCounter51, treeCounter71, treeCounter12, treeCounter11*treeCounter31*treeCounter51*treeCounter71*treeCounter12)