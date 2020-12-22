content = []
with open("input.txt") as f:
    content = f.readlines()

content = [x.strip().split(" ") for x in content] 

def run(program):
    indexesVisited = []
    i = 0
    accumulator = 0
    while i < len(program):
        if (i in indexesVisited):
            return None
        indexesVisited.append(i)
        instruction = program[i][0]
        if (instruction == 'nop'):
            i += 1
        elif (instruction == 'acc'):
            accumulator = accumulator + int(program[i][1])
            i += 1
        elif (instruction == 'jmp'):
            i = i + int(program[i][1])
        else:
            print('Failure?')
    return accumulator

a = None
for i in range(0,len(content)):
    instruction = content[i][0]
    copy = content.copy()
    if (instruction == 'nop'):
        copy[i] = ['jmp', content[i][1]]
        a = run(copy)
    elif (instruction == 'jmp'):
        copy[i] = ['nop', content[i][1]]
        a = run(copy)
    else:
        continue
    if a == None:
        continue
    break


print(a)