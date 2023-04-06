from collections import defaultdict

size = int(input())
graph = defaultdict(list)

for i in range(size):
    row = list(map(int, input().split()))
    
    for j in range(len(row)):
        if row[j] == 1:
            graph[i+1].append(j + 1)
            
for key, value in graph.items():
    print(len(value), end = " ")
    for each in value:
        print(each, end = " ")
        
    print()