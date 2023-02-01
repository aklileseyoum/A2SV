size, target = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
if target == 0:
    if min(array) > 1:
        print(min(array)-1)
    else:
        print(-1)
elif target < size:
    if array[target - 1] == array[target]:
        print(-1)
    else:
        print(array[target - 1])
else:
    print(array[-1])
