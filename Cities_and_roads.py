from collections import defaultdict

size = int(input())
graph = defaultdict(list)

for i in range(size):
    row = list(map(int, input().split()))
    
    for j in range(len(row)):
        if row[j] == 1:
            graph[i].append(j)
     
   
answer = 0   
for key, value in graph.items():
    answer += len(value)
    
print(answer // 2)