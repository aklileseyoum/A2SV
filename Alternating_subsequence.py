    testcases = int(input())
    for testcase in range(testcases):
        size = int(input())
        array = list(map(int, input().split()))
        max_size = 1
        if array[0] > 0:
            flag = 0
        else:
            flag = 1
        maximum = array[0]
        answer = 0
        
        for num in array:
            if num > 0 and flag == 0:
                if maximum < num:
                    maximum = num
            elif num < 0 and flag == 0:
                flag = 1
                answer += maximum
                maximum = num
            elif num > 0 and flag == 1:
                flag = 0
                answer += maximum
                maximum = num
            elif num < 0 and flag == 1:
                if maximum < num:
                    maximum = num
          
        answer += maximum          
        print(answer)
