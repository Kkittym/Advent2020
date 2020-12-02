content = []

with open("input.txt") as f:
    content = f.readlines()

content = [int(x.strip()) for x in content] 
print(content)
print(len(content))

for i in range(0, len(content)):
    for j in range(i+1, len(content)):
        if (content[i] + content[j]) == 2020:
            print ('i=' + str(i) + ', j=' + str(j) + ', content[i]=' + str(content[i]) + ', content[j]=' + str(content[j]) + ', sum=' + str(content[i] + content[j]) + ', multiply=' + str(content[i] * content[j]))
            break

