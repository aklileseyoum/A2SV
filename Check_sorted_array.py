size = int(input())
array = list(map(int, input().split()))
array.sort()
maximum = max(array)
if maximum > (array[-2] + array[-3]):
    print("NO")
else:
    array[-1], array[-2] = array[-2], array[-1]
    print("YES")
    for i in array:
        print(i,end=" ")
