sizes = list(map(int, input().split()))
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
answer = []
idx1 = 0
idx2 = 0
while idx1 < len(array1) and idx2 < len(array2):
    if array1[idx1] > array2[idx2]:
        answer.append(array2[idx2])
        idx2 += 1
    else:
        answer.append(array1[idx1])
        idx1 += 1
 
maximum = max(answer)      
while idx1 < len(array1):
    if array1[idx1] >= maximum:
        answer.append(array1[idx1])
    idx1 += 1
 
while idx2 < len(array2):
    if array2[idx2] >= maximum:
        answer.append(array2[idx2])
    idx2 += 1
            
for num in answer:
    print(num, end=" ")
