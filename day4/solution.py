conten = []
with open("input.txt") as f:
    content = f.readlines()

content = [x.strip().split(" ") for x in content]
content = [x[:3] for subList in content for x in subList]

needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
data = []
goodCount = 0
for x in content:
    if (x == ''):
        if set(needed).issubset(data):
            goodCount = goodCount +1
        data = []
    else:
        data.append(x)

if (data != []):
    if set(needed).issubset(data):
        goodCount = goodCount +1

print(goodCount)