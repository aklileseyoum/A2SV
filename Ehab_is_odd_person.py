size = int(input())
array = list(map(int, input().split()))
remainder = -1
cant = 0
for num in array:
    if remainder == -1:
        remainder = num%2
    elif (remainder == 0 and num%2 == 1) or (remainder == 1 and num%2 == 0):
        cant = 1
if cant == 1:
    array.sort()
for num in array:
    print(num, end=" ")
    
