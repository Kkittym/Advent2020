import re

content = []
with open("input.txt") as f:
    content = f.readlines()

content = [x.strip().split(" ") for x in content]
content = [x for subList in content for x in subList]
# print(content)

needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
data = []
goodCount = 0
isValid = True
# Reg ex pattern for hair colour
hairPattern = re.compile("^#[a-f0-9]{6}$")
# Eye colour set:
eyeCol = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
# Reg ex pattern for passport id
passPattern = re.compile("^[0-9]{9}$")

for x in content:
    if (x == ''):
        print(data)
        if set(needed).issubset(data) and isValid:
            goodCount = goodCount +1
        data = []
        isValid = True
        continue

    if not isValid:
        continue

    x = x.split(":")
    data.append(x[0])

    print(x)

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if x[0] == "byr":
        if (x[1] < "1920") or (x[1] > "2002"):
            isValid = False
    
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif x[0] == "iyr":
        if (x[1] < "2010") or (x[1] > "2020"):
            isValid = False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif x[0] == "eyr":
        if (x[1] < "2020") or (x[1] > "2030"):
            isValid = False

    # hgt (Height) - a number followed by either cm or in:
    elif x[0] == "hgt":
        # If cm, the number must be at least 150 and at most 193.
        if (x[1][-2:] == 'cm'):
            if (x[1][:-2] < "150") or (x[1][:-2] > "193"):
                isValid = False
        # If in, the number must be at least 59 and at most 76.
        elif (x[1][-2:] == 'in'):
            if (x[1][:-2] < "59") or (x[1][:-2] > "76"):
                isValid = False
        else:
            isValid = False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif x[0] == "hcl": 
        if not bool(hairPattern.match(x[1])):
            isValid = False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    elif x[0] == "ecl":
        if not (x[1] in eyeCol):
            isValid = False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif x[0] == "pid": 
        if not bool(passPattern.match(x[1])):
            isValid = False

print(goodCount)