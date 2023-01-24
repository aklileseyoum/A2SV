    sizes = list(map(int, input().split()))
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
     
    idx = 0
    for num in array2:
        while idx < len(array1) and array1[idx] < num:
            idx += 1
            
        print(idx, end=" ")
