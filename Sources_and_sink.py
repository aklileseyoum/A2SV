from collections import defaultdict
vertexs = int(input())
graph = defaultdict(list)
for vertex in range(vertexs):
    row = list(map(int, input().split()))
    
    for idx in range(len(row)):
        if row[idx] == 1:
            graph[vertex+1].append(idx+1)
        
source = []
sink = []
values = []
for key, value in graph.items():
    values += value
    
for vertex in range(vertexs):
    if graph[vertex+1]:
        if (vertex+1) not in values:
            source.append(vertex+1)
    else:
        if (vertex+1) not in values:
            source.append(vertex+1)
        sink.append(vertex+1)
        
print(len(source), end = " ")
for each in source:
    print(each, end = " ")
print()
print(len(sink), end = " ")
for each in sink:
    print(each, end = " ")