    testcases = int(input())
    for testcase in range(testcases):
        size = int(input())
        array = list(map(int, input().split()))
        array.sort()
        answer = "YES"
        for idx in range(len(array)-1):
            idx2 = idx + 1
            if abs(array[idx] - array[idx2]) > 1:
                answer = "NO"
                break
            
        print(answer)
