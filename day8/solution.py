content = []
with open("input.txt") as f:
    content = f.readlines()

content = [x.strip().split(" ") for x in content] 
#print(content)

indexesVisited = []
i = 0
accumulator = 0
while i < len(content):
    #print(content[i])
    if (i in indexesVisited):
        break
    indexesVisited.append(i)
    instruction = content[i][0]
    if (instruction == 'nop'):
        i += 1
    elif (instruction == 'acc'):
        accumulator = accumulator + int(content[i][1])
        i += 1
    elif (instruction == 'jmp'):
        i = i + int(content[i][1])
    else:
        print('Failure?')

print(accumulator)