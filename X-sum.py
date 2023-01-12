from collections import defaultdict
testcases = int(input())
for testcase in range(testcases):
    size = list(map(int, input().split()))
    chess = [[0] * size[1] for _ in range(size[0])]
    for i in range(len(chess)):
        chess[i] = list(map(int, input().split()))
    
    right = defaultdict(int)
    left=defaultdict(int)
    for row in range(size[0]):
        for col in range(size[1]):
            index = row - col
            right[index] += chess[row][col]
            index2 = row + col
            left[index2] += chess[row][col]
            
            
    comp = 0
    for row in range(size[0]):
        for col in range(size[1]):
            answer = 0
            index = row - col
            answer += right[index]
            index2 = row + col
            answer += left[index2]
            answer -= chess[row][col]
            
            comp = max(answer, comp)
                
    print(comp)
