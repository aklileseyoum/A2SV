# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
nums = list(map(int, input().split()))
group_A = []
group_B = []
for i in range(nums[0]):
    word = input()
    group_A.append(word)
for i in range(nums[1]):
    word = input()
    group_B.append(word)
dictionary = defaultdict(list)

for i in range(len(group_A)):
    dictionary[group_A[i]].append(i+1)
    
for i in group_B:
    if i in dictionary:
        listt = dictionary[i]
        print(*listt)
    else:
        print(-1)
