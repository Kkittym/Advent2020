mapping = {}
bagToCount = "1 shiny gold"
with open("input.txt") as f:
    for line in f:
        lineSplit = line.strip()[:-1].split(" bags contain ")
        prim = lineSplit[0]
        contents = []
        for x in lineSplit[1].split(", "):
            if x == "no other bags":
                contents.append(x)
            else:
                contents.append(x.split(" bag")[0])
        mapping[prim] = contents

def count_children(graph, start):
    if (graph[start[2:]] == ['no other bags']):
        return int(start[0])
    count = 1
    for x in graph[start[2:]]:
        countchildren = count_children(graph, x)
        count = count + countchildren
    return count*int(start[0])
    

print(count_children(mapping, bagToCount)-1)
