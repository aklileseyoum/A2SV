from collections import defaultdict
vertex = int(input())
operations = int(input())
graph = defaultdict(list)

for _ in range(operations):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        graph[operation[1]].append(operation[2])
        graph[operation[2]].append(operation[1])
    elif operation[0] == 2:
        answer = graph[operation[1]]
        if not answer:
            continue
        for i in answer:
            print(i, end=" ")
        print()