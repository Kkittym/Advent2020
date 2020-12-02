content = []

with open("input.txt") as f:
    content = f.readlines()

content = [int(x.strip()) for x in content] 

for i in range(0, len(content)):
    for j in range(i+1, len(content)):
        for k in range(j+1, len(content)):
            if (content[i] + content[j] + content[k]) == 2020:
                print ('i=' + str(i) + ', j=' + str(j) + ', k=' + str(k) + ', content[i]=' + str(content[i]) + ', content[j]=' + str(content[j]) + ', content[k]=' + str(content[k]) + ', sum=' + str(content[i] + content[j] + content[k]) + ', multiply=' + str(content[i] * content[j] * content[k]))
                break
