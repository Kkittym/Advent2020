f = open("input.txt", "r")
goodcount = 0
for line in f:
    line = line.strip().split(" ")
    limits = [int(x) for x in line[0].split("-")]
    character = line[1][0]
    password = line[2]
    if (password.count(character) >= limits[0] and password.count(character) <= limits[1]):
        goodcount = goodcount+1
f.close()
print("goodcount =", goodcount)