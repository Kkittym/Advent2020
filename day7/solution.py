mapping = {}
bagtofind = "shiny gold"
with open("input.txt") as f:
    for line in f:
        lineSplit = line.strip()[:-1].split(" bags contain ")
        prim = lineSplit[0]
        contents = []
        for x in lineSplit[1].split(", "):
            if x == "no other bags":
                contents.append(x)
            else:
                contents.append(x[2:].split(" bag")[0])
        mapping[prim] = contents

print (mapping)

# copied from https://www.python.org/doc/essays/graphs/
def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not (start in graph):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

count = 0
for key in mapping:
    if (find_path(mapping, key, bagtofind, [])):
        #print(key)
        count = count+1
print(count-1)
